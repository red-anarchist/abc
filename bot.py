import telebot

bot = telebot.TeleBot('1032705208:AAHL8Ut4k7iybsTEMszWVFB2JA8_Hw7GsBQ')

@bot.message_handler(content_types=['text'])

def get_text_messages(message):
	if message.text == 'Удивите меня':
		bot.delete_message(message.chat.id, message.message_id)
	elif message.text.lower() == 'del' and (message.from_user.username == 'ever_soup' or message.from_user.username == '@ever_soup'):
		bot.delete_message(message.chat.id, message.reply_to_message.id)

bot.polling(none_stop=True)
