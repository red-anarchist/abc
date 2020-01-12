import telebot
import random

bot = telebot.TeleBot('1032705208:AAHL8Ut4k7iybsTEMszWVFB2JA8_Hw7GsBQ')

KNB_list = ['камень', 'ножницы', 'бумага']

def ran(p_list):
	index = random.randint(0, int(len(p_list))-1)
	return p_list[index]

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	mes = message.text.lower().split()
	M = list(message.text)

	if M[0] == '!' or M[0] == '/':
		if mes[0] == '!игра':
			KNB = ran(KNB_list)
			if len(mes) > 1:

				if mes[1] == 'к' or mes[1] == 'камень':
					if KNB == 'камень':
						bot.send_message(message.chat.id, 'Ничья.')
					elif KNB == 'ножницы':
						bot.send_message(message.chat.id, f'{message.from_user.first_name} победил.')
					else:
						bot.send_message(message.chat.id, f'{message.from_user.first_name} проиграл.')

				elif mes[1] == 'н' or mes[1] == 'ножницы':
					if KNB == 'камень':
						bot.send_message(message.chat.id, f'{message.from_user.first_name} проиграл.')
					elif KNB == 'ножницы':
						bot.send_message(message.chat.id, 'Ничья.')
					else:
						bot.send_message(message.chat.id, f'{message.from_user.first_name} победил.')

				elif mes[1] == 'б' or mes[1] == 'бумага':
					if KNB == 'камень':
						bot.send_message(message.chat.id, f'{message.from_user.first_name} победил.')
					elif KNB == 'ножницы':
						bot.send_message(message.chat.id, f'{message.from_user.first_name} проиграл.')
					else:
						bot.send_message(message.chat.id, 'Ничья.')
				else:
					bot.send_message(message.chat.id, 'Надо добавить "К", "Н" или "Б".')

			else:
				bot.send_message(message.chat.id, 'Выбери камень (К), ножницы (Н) или бумагу (Б)\nПример: !игра к')

		elif mes[0] == '!кража':
			dstr = ''
			for a in mes:
				if a == mes[0]:
					pass
				else:
					if a == mes[-1]:
						dstr = dstr + a
					else:
						dstr = dstr + a + ' '
			shans = random.randint(0, 100)
			i = random.randint(0, 100)
			if i <= shans:
				bot.send_message(message.chat.id, f'{message.from_user.first_name} успешно реализует кражу {dstr}! Шанс на успех был {shans}%!')
			else:
				bot.send_message(message.chat.id, f'{message.from_user.first_name} не смог совершить кражу {dstr}, хотя шанс был {shans}%.')

		elif message.text == '/help':
			bot.send_message(message.chat.id, '"!игра (буква)" - камень ножницы бумага\n"!кража (предмет)" - попытка кражи')

		else:
			bot.send_message(message.chat.id, 'Неизвестная команда. Напиши /help.')

bot.polling(none_stop=True)
