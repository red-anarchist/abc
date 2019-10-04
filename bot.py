# -*- coding: utf-8 -*-
import telebot

bot = telebot.TeleBot('981943532:AAHI9aAZkRG4Q0UuNIy2wKtve_y9QFMf9FU')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message('Привет!')

@bot.message_handler(content_types=['text'])
def text(m):
	if m.text.lower[:6]=='!кража':
		bot.send_message(m, m.from_user.first_name+" совершает кражу"+m.text[5:])

bot.polling(none_stop=True)
