# -*- coding: utf-8 -*-
import telebot

bot = telebot.TeleBot("876526827:AAGWgaPYbiFWLF9PDdoGI8ZeMzJtqoJCVtE")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.reply_to(message, message.text)

bot.polling(none_stop = True)
