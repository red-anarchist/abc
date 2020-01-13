# Импорт
import telebot
import random

# Токен
bot = telebot.TeleBot('1032705208:AAHL8Ut4k7iybsTEMszWVFB2JA8_Hw7GsBQ')

# Списки
KNB_list = ['камень', 'ножницы', 'бумага'] # Игра

trusiki_list = ['трусы-шорты', 'плавки', 'панталоны', 'слип', 'кюлот', 'бикини', 'чикибоксеры', 'стринги', 'семейники', 'боксеры', 'хипсы', 'джокстрэпы', 'брифы', 'трусы']

# Случайный элемент списка
def ran(p_list):
	index = random.randint(0, int(len(p_list))-1)
	return p_list[index]

# Хендлер
@bot.message_handler(content_types=['text'])

# Главная функция
def get_text_messages(message):
	mes = message.text.split() # Текст сообщения разбитый на списки

	# Игра
	if mes[0] == '!игра':
		KNB = ran(KNB_list)
		if len(mes) > 1:

			if mes[1] == 'к' or mes[1] == 'камень':
				if KNB == 'камень':
					bot.send_message(message.chat.id, '*показываю камень*\nНичья.')
				elif KNB == 'ножницы':
					bot.send_message(message.chat.id, f'*показываю ножницы*\n{message.from_user.first_name} победил.')
				else:
					bot.send_message(message.chat.id, f'*показываю бумагу*\n{message.from_user.first_name} проиграл.')

			elif mes[1] == 'н' or mes[1] == 'ножницы':
				if KNB == 'камень':
					bot.send_message(message.chat.id, f'*показываю камень*\n{message.from_user.first_name} проиграл.')
				elif KNB == 'ножницы':
					bot.send_message(message.chat.id, '*показываю ножницы*\nНичья.')
				else:
					bot.send_message(message.chat.id, f'*показываю бумагу*\n{message.from_user.first_name} победил.')

			elif mes[1] == 'б' or mes[1] == 'бумага':
				if KNB == 'камень':
					bot.send_message(message.chat.id, f'*показываю камень*\n{message.from_user.first_name} победил.')
				elif KNB == 'ножницы':
					bot.send_message(message.chat.id, f'*показываю ножницы*\n{message.from_user.first_name} проиграл.')
				else:
					bot.send_message(message.chat.id, '*показываю бумагу*\nНичья.')
			else:
				bot.send_message(message.chat.id, 'Надо добавить "К", "Н" или "Б".')

		else:
			bot.send_message(message.chat.id, 'Выбери камень (К), ножницы (Н) или бумагу (Б)\nПример: !игра к; !игра камень')

	# Кража
	elif mes[0] == '!кража':
		dstr = message.text.lstrip('!кража ')
		shans = random.randint(0, 100)
		i = random.randint(0, 100)
		if i <= shans:
			bot.send_message(message.chat.id, f'{message.from_user.first_name} успешно реализует кражу {dstr}! Шанс на успех был {shans}%!')
		else:
			bot.send_message(message.chat.id, f'{message.from_user.first_name} не смог совершить кражу {dstr}, хотя шанс был {shans}%.')

	# Кража трусов
	elif mes[0] == '!трусики':
		dstr = message.text.lstrip('!трусики ')
		shans = random.randint(0, 100)
		i = random.randint(0, 100)
		if i <= shans:
			bot.send_message(message.chat.id, f'{message.from_user.first_name} смог украсть {ran(trusiki_list)} у {dstr}! Шанс на успех был целых {shans}%!')
		else:
			bot.send_message(message.chat.id, f'{message.from_user.first_name} не смог украсть нижнее бельё {dstr}, каков извращенец! Шанс на успех был {shans}%.')

	# Обновления
	elif mes[0] == '/update' or mes[0] == '/обновления':
		bot.send_message(message.chat.id, '*Последние обновления*\n \n*13.01.2020*\n—Исправлен текст игры\n—Добавлены обновления\n—Обновлено меню помощи\n—Упрощён код\n—Теперь можно красть трусики', parse_mode='markdown')

	# Помощь
	elif mes[0] == '/help' or mes[0] == '/помощь':
		bot.send_message(message.chat.id, '*!игра (буква или объект)* — камень ножницы бумага\n*!кража (предмет в родительном падеже)* — попытка кражи\n*!трусики (имя пользователя в родительном падеже)* — кража нижнего белья\n*/update* `или` */обновления* — показать последние обновления', parse_mode='markdown')

	# Неизвестная команада
	elif message.text[0] == '!' or message.text[0] == '/':
		bot.send_message(message.chat.id, 'Неизвестная команда, в /help (/помощь) вы можете посмотреть доступные команды.')

bot.polling(none_stop=True)
