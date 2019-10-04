# -*- coding: utf-8 -*-
import telebot

bot = telebot.TeleBot('981943532:AAHI9aAZkRG4Q0UuNIy2wKtve_y9QFMf9FU')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Д')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message('Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')

bot.polling(none_stop=True)
