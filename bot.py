from requests import get
from fake_useragent import UserAgent as fua
from bs4 import BeautifulSoup as BS
from telebot import TeleBot

bot = TeleBot("5217885808:AAFG8xIybc4y7ZBMQQX_U6EO03yCXkM_xK4")
site = "https://shikimori.one/"

ua = fua()
header = {"User-Agent":ua.chrome}

@bot.message_handler(commands=["start"])
def start(mes):
	bot.send_message(mes.chat.id, "Привет! Я могу получать некоторые данные с сайта Shikimori.")

@bot.message_handler(content_types=["text"])
def main1(mes):
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
				bot.send_message(mes.chat.id, f"Имя: {info['name']}\nПросмотрено: {info['comp']}")

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
		INFO["comp"] = bar.find_all('div')[0].text

		return INFO

bot.polling()
