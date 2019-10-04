# -*- coding: utf-8 -*-
import telebot

bot = telebot.TeleBot('942081274:AAF4q7sOVQYb_q9uF_bg6OXuFnFMzL1u4a8')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')

bot.polling(none_stop=True)
