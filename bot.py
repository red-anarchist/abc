import telebot
from random import randint

bot = telebot.TeleBot('1032705208:AAHL8Ut4k7iybsTEMszWVFB2JA8_Hw7GsBQ')

@bot.message_handler(content_types=['text'])

def get_text_messages(message):
	if len(message.text) > 30:
		text = f'{message.text[0:30]}...'
	else:
		text = message.text
	print(f'{message.from_user.username}: "{text}"')
	if message.text == 'Удивите меня':
		bot.delete_message(message.chat.id, message.message_id)
	elif message.text == '▶️ Игры':
		bot.delete_message(message.chat.id, message.message_id)
	elif message.text == 'Связаться с поддержкой':
		bot.delete_message(message.chat.id, message.message_id)
	elif message.text[0:3].lower() == 'бот,' and message.text[-1] == '?':
		if randint(0,1) == 1:
			bot.send_message(message.chat.id, 'Да')
		else:
			bot.send_message(message.chat.id, 'Нет')

bot.polling(none_stop=True)
