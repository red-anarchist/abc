# -*- coding: utf-8 -*-
import telebot

bot = telebot.TeleBot('981943532:AAHI9aAZkRG4Q0UuNIy2wKtve_y9QFMf9FU')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message('Привет!')

@bot.message_handler(content_types=['text'])
def send_text(message):

    if message.text.lower() == 'привет':
        bot.send_message('Здарова!')
    elif message.text.lower() == 'пока':
        bot.send_message('Прощай, создатель')
    elif message.text[0] == '!':
        bot.send_message('хочет '+send_message[1:-1])

bot.polling(none_stop=True)
