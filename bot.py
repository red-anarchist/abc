from requests import get
from fake_useragent import UserAgent as fua
from bs4 import BeautifulSoup as BS
from telebot import TeleBot

bot = TeleBot("5231845055:AAHVisbLBnWbFAoniKXeNoixZCnjnxw42vo")
site = "https://shikimori.one/"

ua = fua()
header = {"User-Agent":ua.chrome}

@bot.message_handler(commands=["start"])
def start(mes):
	bot.send_message(mes.chat.id, "Привет! Я могу получать некоторые данные с сайта Shikimori.")

@bot.message_handler(content_types=["text"])
def main1(mes):
	print("подкл")
	txm = mes.text
	if txm.split()[0].lower() in ["пользователь", "юзер", "user", "!!"]:
		print("юз")
		try:
			print(txm, txm.split())
			if txm.split()[1] in ["+", "i", "me", "я"]:
				usnm = mes.from_user.username
			else:
				usnm = txm.split()[1]
		except IndexError:
			bot.send_message(mes.chat.id, "Вы неправильно что-то ввели.")
		else:
			print(usnm)
			info = get_user_information(usnm)
			if info is None:
				bot.send_message(mes.chat.id, "Пользователь не найден.")
			else:
				bot.send_message(mes.chat.id, f"Имя: {info['name']}\nПросмотрено: {info['comp']}")

def connect(link, mes):
	responce = get(link)
	print(type(responce.status_code), responce.status_code)
	if responce.status_code == 200:
		return True
	elif responce.status_code == 404:
		bot.send_message(mes.chat.id, "Странно, но сайт не найден.")
		return False

def get_user_information(user):
	INFO = {}
	a = site+user
	responce = get(a, headers=header).text
	print(site+user)
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
		INFO["comp"] = bar.find_all('div')[0].text

		return INFO

bot.polling()
