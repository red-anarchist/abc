from requests import get
from fake_useragent import UserAgent as fua
from bs4 import BeautifulSoup as BS
from telebot import TeleBot

bot = TeleBot("5217885808:AAFG8xIybc4y7ZBMQQX_U6EO03yCXkM_xK4")
site = "https://shikimori.one/"

TITLE_TYPES = {
	"animes":"a",
	"mangas":"m",
	"ranobe":"r"
}

reverse_tt = {
	"a":"animes",
	"m":"mangas",
	"r":"ranobe"
}

ua = fua()
header = {"User-Agent":ua.chrome}

@bot.message_handler(commands=["start"])
def start(mes):
	bot.send_message(mes.chat.id, "Привет! Я могу получать некоторые данные с сайта Shikimori.")

@bot.message_handler(content_types=["text"])
def main(mes):
	txm = mes.text
	if txm.split()[0].lower() in ["пользователь", "юзер", "user", "!!"]:
		try:
			if txm.split()[1] in ["+", "i", "me", "я"]:
				usnm = mes.from_user.username
			else:
				usnm = txm.split()[1]
		except IndexError:
			bot.send_message(mes.chat.id, "Вы неправильно что-то ввели.")
		else:
			info = get_user_information(usnm)
			if info is None:
				bot.send_message(mes.chat.id, "Пользователь не найден.")
			else:
				bot.send_message(mes.chat.id, f"Имя: {info['name']}\
					                          \nПросмотрено: {info['comp']}\
					                          \nЗапланировано: {info['plan']}\
					                          \nБрошено: {info['drop']}")

	if txm.split()[0].lower() in ["f", "find", "поиск", "??"]:
		try:
			if txm.split()[1].lower() in ["anime", "аниме", "a", "а"]:
				find_type = "animes"
			elif txm.split()[1].lower() in ["manga", "манга", "m", "м"]:
				find_type = "mangas"
			elif txm.split()[1].lower() in ["ranobe", "ранобе", "r", "р"]:
				find_type = "ranobe"
			elif txm.split()[1].lower() in ["character", "персонаж", "ch", "c", "п"]:
				#find_type = "characters"
				bot.send_message(mes.chat.id, "В разработке...")
				return
			elif txm.split()[1].lower() in ["people", "person", "человек", "p", "ч"]:
				#find_type = "people"
				bot.send_message(mes.chat.id, "В разработке...")
				return
			else:
				bot.send_message(mes.chat.id, "Вы неправильно что-то ввели.")
				return
		except IndexError:
			bot.send_message(mes.chat.id, "Вы неправильно что-то ввели.")
		else:
			try:
				RESULTS_AMT = int(txm.split()[2])
				REQUEST_TEXT_TAB = 3
			except ValueError:
				RESULTS_AMT = 5
				REQUEST_TEXT_TAB = 2
			except IndexError:
				bot.send_message(mes.chat.id, "Вы неправильно что-то ввели.")
				return
			find_text = ""
			for word in txm.split()[REQUEST_TEXT_TAB:]:
				find_text = find_text + word + " "

			finds_results = find(find_type, find_text, RESULTS_AMT)

			markup = types.InlineKeyboardMarkup(row_width=1)
			buttons = []
			for name, id_ in finds_results.items():
				buttons.append(types.InlineKeyboardButton(text=name, callback_data=id_))
			markup.add(*buttons)
			bot.send_message(mes.chat.id, "Это всё, что мне удалось найти по твоему запросу, Величество.", reply_markup=markup)

def get_user_information(user):
	INFO = {}
	a = site+user
	responce = get(a, headers=header).text
	soup = BS(responce, "lxml")
	try:
		sec = soup.find("section", class_="l-page").find("div")
	except AttributeError:
		pass
	else:
		head = sec.find_all("div")[0]
		c_info = head.find("div", class_="c-info")
		c_lists_info = c_info.find("div", class_="c-lists-info")
		b_stats_bar_anime = c_lists_info.find("div", class_="b-stats_bar anime")
		bar = b_stats_bar_anime.find("div", class_="bar")

		INFO["name"] = head.find("div", class_="c-brief").find("header").find("h1").text
		try:
			INFO["comp"] = bar.find_all('div')[0].text
		except AttributeError:
			INFO["comp"] = None
		try:
			INFO["plan"] = bar.find_all('div')[1].text
		except:
			INFO["plan"] = None
		try:
			INFO["drop"] = bar.find_all('div')[2].text
		except:
			INFO["drop"] = None

		return INFO

def find(find_type, find_text, amt_reqs):
	res_text = f"{site}{find_type}/autocomplete/v2?search={find_text}"
	responce = get(res_text, headers=header).text
	soup = BS(responce, "lxml")
	
	sec = soup.find("section")
	d = sec.find("div")
	results_div = d.find_all("div", class_="b-db_entry-variant-list_item")
	results_div = results_div[0:amt_reqs]
	result_dict = {}
	for title_div in results_div:
		title_name = title_div.get("data-text")
		title_id = title_div.get("data-id")
		try:
			title_url = int(title_div.get("data-url").replace(f"{site}{find_type}/", "")[0])
		except ValueError:
			title_id = title_div.get("data-url").replace(f"{site}{find_type}/", "")[0] + title_id
		title_id = TITLE_TYPES[find_type] + title_id

		result_dict[title_name] = title_id
	return result_dict

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	if call.message:
		t_type = reverse_tt[call.data[0]]
		t_id = call.data[1:]

		res_text = f"{site}{t_type}/{t_id}"
		if t_type == "animes":
			result = get_anime_information(res_text, call)
		elif t_type == "mangas":
			result = get_manga_information(res_text, call)
		elif t_type == "ranobe":
			result = get_ranobe_information(res_text, call)
		if result is None:
			return

		text = ""
		for a, b in result.items():
			text = text + f"{a} {b}\n"

		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text)

def get_anime_information(res_text, call):
	result = {}
	responce = get(res_text, headers=header).text
	soup = BS(responce, "lxml")
	try:
		sec = soup.find("section")
		d = sec.find("div")
		head = d.find("header")
		result["Название:"] = head.find("h1").text
	except AttributeError:
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Ошибка!")
		return None
	result.update(get_left_info(soup))

	return result

def get_manga_information(res_text, call):
	result = {}
	responce = get(res_text, headers=header).text
	soup = BS(responce, "lxml")
	try:
		sec = soup.find("section")
		d = sec.find("div")
		head = d.find("header")
		result["Название:"] = head.find("h1").text
	except AttributeError:
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Ошибка!")
		return None
	result.update(get_left_info(soup))
	return result

def get_ranobe_information(res_text, call):
	result = {}
	responce = get(res_text, headers=header).text
	soup = BS(responce, "lxml")
	try:
		sec = soup.find("section")
		d = sec.find("div")
		head = d.find("header")
		result["Название:"] = head.find("h1").text
	except AttributeError:
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Ошибка!")
		return None
	result.update(get_left_info(soup))
	return result

def get_left_info(soup):
	result = {}
	sec = soup.find("section")
	d = sec.find("div")
	head = d.find("header")
	cc = d.find("div", class_="menu-slide-inner")
	cc = cc.find("div", class_="l-content")
	cc = cc.find("div", class_="block")
	cc = cc.find("div", class_="b-db_entry")
	cc = cc.find("div", class_="c-about")
	cc = cc.find("div", class_="cc")
	c_info_left = cc.find("div", class_="c-info-left")
	left_info = c_info_left.find("div", class_="block")
	left_info = left_info.find("div")
	left_info = left_info.find_all("div", class_="line-container")
	for line_c in left_info[0:-1]:
		line = line_c.find("div")
		line = line.find_all("div")
		key = line[0]
		if key.text == "Альтернативные названия:":
			return result
		value = line[1]
		if len(value.find_all()) > 0:
			try:
				if "b-anime_status_tag" in value.find_all()[0].get("class"):
					value = value.find("span").get("data-text") + value.text
				elif "b-tag" in value.find_all()[0].get("class"):
					genres = ""
					for a in value.find_all():
						if "genre-ru" in a.get("class"):
							genres = genres + a.text + " "
					value = genres
				elif "b-tooltipped" in value.find_all()[0].get("class"):
					value = value.find("span").text
			except TypeError:
				value = value.find("span").text
		else:
			value = value.text
		result[key.text] = value
	return result

bot.polling()
