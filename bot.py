import telebot

bot = telebot.TeleBot('1032705208:AAHL8Ut4k7iybsTEMszWVFB2JA8_Hw7GsBQ')

@bot.message_handler(content_types=['text'])

def get_text_messages(message):
	if message.text == 'Удивите меня':
		bot.delete_message(message.chat.id, message.message_id)

bot.polling(none_stop=True)
