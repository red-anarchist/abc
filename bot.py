# Импорт
import telebot
import random

# Токен
bot = telebot.TeleBot('1032705208:AAHL8Ut4k7iybsTEMszWVFB2JA8_Hw7GsBQ')

# Списки
KNB_list = ['камень', 'ножницы', 'бумага'] # Игра

trusiki_list = ['трусы-шорты', 'плавки', 'панталоны', 'слип', 'кюлот', 'бикини', 'чикибоксеры', 'стринги', 'семейники', 'боксеры', 'хипсы', 'джокстрэпы', 'брифы', 'трусы']

duel_list = ['кнб', 'жребий', 'борьба', 'наперегонки', 'члены', 'пистолеты', 'видеоигры', 'гачимучи']
duel_list2 = ['Я порву тебя!', 'Я убью тебя!', 'Тебе не жить!', 'Ты не знаешь с кем тебе предстоит сразиться!', 'Ты себя-то хоть видел?',
	'Я заставлю тебя страдать!', 'Ты у меня попляшешь!', 'Я заставлю тебя ответить за свои слова, подлец!', 'Лучше сдавайся сразу!',
	'Ты у меня отхватишь!', 'Ты ответишь за свои слова!', 'Жить надоело?'
	]
duel_list3 = ['нанометров', 'милиметров', 'сантиметров', 'метров', 'километров', 'миль']
duel_list5 = ['Glock 20','Glock 34','Bersa Thunder 380','FN Five-seveN','Melior','Пистолет Макарова','FEG PA-63','Mauser C96','Volkspistole',
	'SIG Sauer Pro','Walther PP','Пистолет Люгера','Llama M82','Star Model B','AF2011-A1 «Second Century»','Beretta Px4 Storm','WIST-94',
	'Пистолет Лебедева','Пистолет Ярыгина','Стриж','Grand Power K100','Colt Double Eagle','M1911','Smith & Wesson Model 59','Beretta M9',
	'Desert Eagle','Sphinx 3000'
	]
duel_list5b = ['плечо','колено','руку','живот','ногу']
duel_list6a = ['секунд','минут','часов','дней','недель','месяцев','лет','десятилетий','столетий','тысячелетий']
duel_list6b = ['строил дом','строил ферму','выращивал пшеницу','убивал свиней','убивал овец','убивал зомби','готовил еду',
	'добывал уголь','добывал железо','добывал золото','добывал алмазы','добывал изумруды','добывал красную пыль','спал',
	'строил члены','выращивал арбузы','выращивал тыквы','гулял','грабил деревни','крафтил броню','крафтил оружие',
	'добывал дерево','плавал на лодке','рыбачил','осваивал механизмы','строил замок','ел','голодал','писал в чат',
	'катался на свинье','катался на лошади','катался на вагонетке'
	]
duel_list6c = ['взрывом динамита','деревянным мечом','железным мечом','золотым мечом','стрелой','огненной стрелой','палкой',
	'деревянной киркой','железной киркой','золотой киркой','алмазной киркой','алмазным мечом','руками','деревянным топором',
	'каменным топором','железным топором','золотым топором','алмазным топором','каменным мечом','каменной киркой','лавой',
	'деревянной мотыгой','каменной мотыгой','золотой мотыгой','железной мотыгой','алмазной мотыгой','огнём'
	]

# Случайный элемент списка
def ran(p_list):
	index = random.randint(0, int(len(p_list))-1)
	return p_list[index]

# Хендлер
@bot.message_handler(content_types=['text'])

# Главная функция
def get_text_messages(message):
	mes = message.text.split() # Текст сообщения разбитый на списки

	# Кража
	if mes[0].lower() == '!кража':
		dstr = message.text.lstrip('!кража ')
		shans = random.randint(0, 100)
		i = random.randint(0, 100)
		if i <= shans:
			bot.send_message(message.chat.id, f'{message.from_user.first_name} успешно реализует кражу {dstr}! Шанс на успех был {shans}%!')
		else:
			bot.send_message(message.chat.id, f'{message.from_user.first_name} не смог совершить кражу {dstr}, хотя шанс был {shans}%.')

	# Кража трусов
	elif mes[0].lower() == '!трусики':
		dstr = message.text.lstrip('!трусики ')
		shans = random.randint(0, 100)
		i = random.randint(0, 100)
		if i <= shans:
			bot.send_message(message.chat.id, f'{message.from_user.first_name} смог украсть {ran(trusiki_list)} у {dstr}! Шанс на успех был целых {shans}%!')
		else:
			bot.send_message(message.chat.id, f'{message.from_user.first_name} не смог украсть нижнее бельё {dstr}, каков извращенец! Шанс на успех был {shans}%.')
		
	# Дуэль
	elif mes[0].lower() == '!дуэль':
		try:
			fight_UN1 = message.from_user.first_name
			fight_UN2 = message.reply_to_message.from_user.first_name
			fight = ran(duel_list)
			fight_text = ''
			if fight == 'кнб':
				fight_result = random.randint(0,8)
				if fight_result == 0:
					fight_text = f'*{fight_UN1}* хочет провести *дуэль* в игре _камень ножницы бумага_.\n*{fight_UN2}* соглашается.\n \nОни начинают:\n_— Раз, два, три!_\n \n*{fight_UN1}* показывает *камень*.\n*{fight_UN2}* тоже показывает *камень*!\n \n*Ничья!*'
				elif fight_result == 1:
					fight_text = f'*{fight_UN1}* хочет провести *дуэль* в игре _камень ножницы бумага_.\n*{fight_UN2}* соглашается.\n \nОни начинают:\n_— Раз, два, три!_\n \n*{fight_UN1}* показывает *камень*.\n*{fight_UN2}* показывает *ножницы*!\n \n*{fight_UN1} побеждает!*'
				elif fight_result == 2:
					fight_text = f'*{fight_UN1}* хочет провести *дуэль* в игре _камень ножницы бумага_.\n*{fight_UN2}* соглашается.\n \nОни начинают:\n_— Раз, два, три!_\n \n*{fight_UN1}* показывает *камень*.\n*{fight_UN2}* показывает *бумагу*!\n \n*{fight_UN2} побеждает!'

				elif fight_result == 3:
					fight_text = f'*{fight_UN1}* хочет провести *дуэль* в игре _камень ножницы бумага_.\n*{fight_UN2}* соглашается.\n \nОни начинают:\n_— Раз, два, три!_\n \n*{fight_UN1}* показывает *ножницы*.\n*{fight_UN2}* показывает *камень*!\n \n*{fight_UN2} побеждает!*'
				elif fight_result == 4:
					fight_text = f'*{fight_UN1}* хочет провести *дуэль* в игре _камень ножницы бумага_.\n*{fight_UN2}* соглашается.\n \nОни начинают:\n_— Раз, два, три!_\n \n*{fight_UN1}* показывает *ножницы*.\n*{fight_UN2}* тоже показывает *ножницы*!\n \n*Ничья!*'
				elif fight_result == 5:
					fight_text = f'*{fight_UN1}* хочет провести *дуэль* в игре _камень ножницы бумага_.\n*{fight_UN2}* соглашается.\n \nОни начинают:\n_— Раз, два, три!_\n \n*{fight_UN1}* показывает *ножницы*.\n*{fight_UN2}* показывает *бумагу*!\n \n*{fight_UN1} побеждает!*'

				elif fight_result == 6:
					fight_text = f'*{fight_UN1}* хочет провести *дуэль* в игре _камень ножницы бумага_.\n*{fight_UN2}* соглашается.\n \nОни начинают:\n_— Раз, два, три!_\n \n*{fight_UN1}* показывает *бумагу*.\n*{fight_UN2}* показывает *камень*!\n \n*{fight_UN1} побеждает!*'
				elif fight_result == 7:
					fight_text = f'*{fight_UN1}* хочет провести *дуэль* в игре _камень ножницы бумага_.\n*{fight_UN2}* соглашается.\n \nОни начинают:\n_— Раз, два, три!_\n \n*{fight_UN1}* показывает *бумагу*.\n*{fight_UN2}* показывает *ножницы*!\n \n*{fight_UN2} побеждает!*'
				elif fight_result == 8:
					fight_text = f'*{fight_UN1}* хочет провести *дуэль* в игре _камень ножницы бумага_.\n*{fight_UN2}* соглашается.\n \nОни начинают:\n_— Раз, два, три!_\n \n*{fight_UN1}* показывает *бумагу*.\n*{fight_UN2}* тоже показывает *бумагу*!\n \n*Ничья!*'
				else:
					pass

			elif fight == 'жребий':
				fight_result = random.randint(0,2)
				if fight_result == 0:
					fight_text = f'*{fight_UN1}* хочет провести *дуэль* _жребием_.\n*{fight_UN2}* даёт согласие.\n \n_—Если выпадает *орёл*, то побеждает *{fight_UN1}*, в противном случае побеждает *{fight_UN2}*._ \n*{fight_UN1}* подбрасывает монетку.\nМонетка падает ему в руку.\nВыпал *орёл*, победу одерживает *{fight_UN1}*.'
				elif fight_result == 1:
					fight_text = f'*{fight_UN1}* хочет провести *дуэль* _жребием_.\n*{fight_UN2}* даёт согласие.\n \n_—Если выпадает *орёл*, то побеждает *{fight_UN1}*, в противном случае побеждает *{fight_UN2}*._ \n*{fight_UN1}* подбрасывает монетку.\nМонетка падает ему в руку.\nВыпала *решка*, победу одерживает *{fight_UN2}*.'
				else:
					fight_text = f'*{fight_UN1}* хочет провести *дуэль* _жребием_.\n*{fight_UN2}* даёт согласие.\n \n_—Если выпадает *орёл*, то побеждает *{fight_UN1}*, в противном случае побеждает *{fight_UN2}*._ \n*{fight_UN1}* подбрасывает монетку.\nМонетка падает в снег, её никто не может найти.\n*{fight_UN1}* и *{fight_UN2}* объявляют _ничью_.'

			elif fight == 'борьба':
				fight_result = random.randint(0,1)
				if fight_result == 0:
					fight_text = f'*{fight_UN1}* хочет провести *дуэль* путём _борьбы_.\n*{fight_UN2}* без каких-либо раздумий соглашается.\n \n*{fight_UN1}*_: {ran(duel_list2)}_\n*{fight_UN2}*_: {ran(duel_list2)}_\n \n Спустя некоторое время, *{fight_UN2}* всё же сдаётся. *{fight_UN1} побеждает!*'
				elif fight_result == 1:
					fight_text = f'*{fight_UN1}* хочет провести *дуэль* путём _борьбы_.\n*{fight_UN2}* без каких-либо раздумий соглашается.\n \n*{fight_UN1}*_: {ran(duel_list2)}_\n*{fight_UN2}*_: {ran(duel_list2)}_\n \n Спустя некоторое время, *{fight_UN1}* всё же сдаётся. *{fight_UN2} побеждает!*'
				else:
					pass

			elif fight == 'наперегонки':
				fight_result = random.randint(0,1)
				if fight_result == 0:
					fight_text = f'*{fight_UN1}* хочет провести *дуэль*, чтобы победить надо первому пробежать {str(random.randint(1,50000))} {ran(duel_list3)}. *{fight_UN2}* с удовольствием принимает участие в *дуэли*.\n \n— На старт! Внимание! Марш!\n \n{fight_UN1} прибегает первым.'
				elif fight_result == 1:
					fight_text = f'*{fight_UN1}* хочет провести *дуэль*, чтобы победить надо первому пробежать {str(random.randint(1,50000))} {ran(duel_list3)}. *{fight_UN2}* с удовольствием принимает участие в *дуэли*.\n \n— На старт! Внимание! Марш!\n \n{fight_UN2} прибегает первым.'
				else:
					pass

			elif fight == 'члены':
				chlen_UN1 = random.randint(2,35)
				chlen_UN2 = random.randint(2,35)
				if chlen_UN1 > chlen_UN2:
					fight_text = f'*{fight_UN1}* заходит в туалет, там ссал {fight_UN2}.\n \n*{fight_UN1}*_: Привет, {fight_UN2}, какая встреча!_\n*{fight_UN2}*_: Привет!_\n*{fight_UN1}*_: У меня появилась одна мысля. Можем устроить_ *дуэль!*\n*{fight_UN2}*_: Хорошая идея, но в чём будет заключатся эта дуэль?_\n*{fight_UN1}*_: Можем помериться членами._\n*{fight_UN2}*_: Хорошая идея!_\n*{fight_UN1}* и *{fight_UN2}* снимают штаны и достают свои причендалы. *{fight_UN1}* достаёт из пенала линейку.\n*{fight_UN1}*_: У меня {chlen_UN1}_\n*{fight_UN2}*_: Чёрт, у меня {chlen_UN2}!_'
				elif chlen_UN2 > chlen_UN1:
					fight_text = f'*{fight_UN1}* заходит в туалет, там ссал {fight_UN2}.\n \n*{fight_UN1}*_: Привет, {fight_UN2}, какая встреча!_\n*{fight_UN2}*_: Привет!_\n*{fight_UN1}*_: У меня появилась одна мысля. Можем устроить_ *дуэль!*\n*{fight_UN2}*_: Хорошая идея, но в чём будет заключатся эта дуэль?_\n*{fight_UN1}*_: Можем помериться членами._\n*{fight_UN2}*_: Хорошая идея!_\n*{fight_UN1}* и *{fight_UN2}* снимают штаны и достают свои причендалы. *{fight_UN1}* достаёт из пенала линейку.\n*{fight_UN1}*_: У меня {chlen_UN1}_\n*{fight_UN2}*_: Ха, а у меня {chlen_UN2}!_'
				else:
					fight_text = f'*{fight_UN1}* заходит в туалет, там ссал {fight_UN2}.\n \n*{fight_UN1}*_: Привет, {fight_UN2}, какая встреча!_\n*{fight_UN2}*_: Привет!_\n*{fight_UN1}*_: У меня появилась одна мысля. Можем устроить_ *дуэль!*\n*{fight_UN2}*_: Хорошая идея, но в чём будет заключатся эта дуэль?_\n*{fight_UN1}*_: Можем помериться членами._\n*{fight_UN2}*_: Хорошая идея!_\n*{fight_UN1}* и *{fight_UN2}* снимают штаны и достают свои причендалы. *{fight_UN1}* достаёт из пенала линейку.\n*{fight_UN1}*_: У меня {chlen_UN1}_\n*{fight_UN2}*_: У меня тоже..._'
			
			elif fight == 'пистолеты':
				fight_result = random.randint(0,2)
				if fight_result == 0:
					fight_text = f'*{fight_UN1}* желает провести *дуэль* на _пистолетах_. *{fight_UN2}* соглашается, хотя он знает, что это может стоить ему жизни.\n \n`В матче не пострадает ни один человек!`\n \n*{fight_UN1}* уже позвал секунданта, секундант был с оружием. *{fight_UN1}* решил взять _{ran(duel_list5)}_, хороший выбор! *{fight_UN2}* хочет взять _{ran(duel_list5)}_.\n \nПоединок окончился ничьёй.'
				elif fight_result == 1:
					fight_text = f'*{fight_UN1}* желает провести *дуэль* на _пистолетах_. *{fight_UN2}* соглашается, хотя он знает, что это может стоить ему жизни.\n \n`В матче не пострадает ни один человек!`\n \n*{fight_UN1}* уже позвал секунданта, секундант был с оружием. *{fight_UN1}* решил взять _{ran(duel_list5)}_, хороший выбор! *{fight_UN2}* хочет взять _{ran(duel_list5)}_.\n \n*{fight_UN1}* попадает противнику в _{duel_list5b}_ и побеждает.'
				elif fight_result == 2:
					fight_text = f'*{fight_UN1}* желает провести *дуэль* на _пистолетах_. *{fight_UN2}* соглашается, хотя он знает, что это может стоить ему жизни.\n \n`В матче не пострадает ни один человек!`\n \n*{fight_UN1}* уже позвал секунданта, секундант был с оружием. *{fight_UN1}* решил взять _{ran(duel_list5)}_, хороший выбор! *{fight_UN2}* хочет взять _{ran(duel_list5)}_.\n \n*{fight_UN2}* попадает противнику в _{duel_list5b}_ и побеждает.'
				else:
					pass

			elif fight == 'видеоигры':
				fight_result = random.randint(0,1)
				if fight_result == 0:
					fight_text = f'*{fight_UN1}* хочет поиграть в _Minecraft_, но в сети был только *{fight_UN2}*. *{fight_UN2}* соглашается с ним поиграть.\nЧерез _{str(random.randint(2,9))} {ran(duel_list6a)}_ им стало скучно и тогда *{ran([fight_UN1,fight_UN2])}* предложил *PvP*.\n \nПока *{fight_UN2}* _{ran(duel_list6b)}_, *{fight_UN1}* убивает его _{ran(duel_list6c)}._'
				elif fight_result == 1:
					fight_text = f'*{fight_UN1}* хочет поиграть в _Minecraft_, но в сети был только *{fight_UN2}*. *{fight_UN2}* соглашается с ним поиграть.\nЧерез _{str(random.randint(2,9))} {ran(duel_list6a)}_ им стало скучно и тогда *{ran([fight_UN1,fight_UN2])}* предложил *PvP*.\n \nПока *{fight_UN1}* _{ran(duel_list6b)}_, *{fight_UN2}* убивает его _{ran(duel_list6c)}._'
				else:
					pass

			elif fight == 'гачимучи':
				fight_result = random.randint(0,1)
				if fight_result == 0:
					fight_text = f'*{fight_UN1}* спокойно сидит в раздевалке, заходит *{fight_UN2}*. *{fight_UN1}* замечает его латексную одежду. Они молча стоят. *{fight_UN2}* начинает переодеваться.\n*{fight_UN1}*_: Эй, дружок-пирожок, боюсь, ты ошибся дверью, клуб кожанного ремесла два блока вниз._\n*{fight_UN2}*_: Пошёл на хрен._\n*{fight_UN1}* встаёт со скамейки.\n*{fight_UN1}*_: Нет уж... Ты пойдёшь на хрен, кожаночка. Если ты думаешь, что такой крутой, то можем разобраться прямо сейчас, на ринге._\n*{fight_UN2}*_: Хорошо, я надеру тебе зад!_\n*{fight_UN1}*_: Ха! Ну хорошо, кожанный переплёт, тогда снимай свою кожаную обёртку, я сниму свою одёжку и мы разберёмся с тобой прямо сейчас на ринге_\n*{fight_UN2}*_: Да без проблем, дружочек._\n*{fight_UN1}*_: Ну вот и хорошо, снимай с себя этот наряд._\n*{fight_UN2}*_: Умная жопка._\nОни оба начинают раздеваться.\n*{fight_UN1}*_: Я покажу тебе, кто босс этой качалки._\nОни были готовы к схватке.\n*{fight_UN1}*_: Ну всё, погнали!_\n*{fight_UN2}*_: Ага..._\n`всё заканчивается тем, что {fight_UN1} надрал зад своему противнику.`'
				elif fight_result == 1:
					fight_text = f'*{fight_UN1}* спокойно сидит в раздевалке, заходит *{fight_UN2}*. *{fight_UN1}* замечает его латексную одежду. Они молча стоят. *{fight_UN2}* начинает переодеваться.\n*{fight_UN1}*_: Эй, дружок-пирожок, боюсь, ты ошибся дверью, клуб кожанного ремесла два блока вниз._\n*{fight_UN2}*_: Пошёл на хрен._\n*{fight_UN1}* встаёт со скамейки.\n*{fight_UN1}*_: Нет уж... Ты пойдёшь на хрен, кожаночка. Если ты думаешь, что такой крутой, то можем разобраться прямо сейчас, на ринге._\n*{fight_UN2}*_: Хорошо, я надеру тебе зад!_\n*{fight_UN1}*_: Ха! Ну хорошо, кожанный переплёт, тогда снимай свою кожаную обёртку, я сниму свою одёжку и мы разберёмся с тобой прямо сейчас на ринге_\n*{fight_UN2}*_: Да без проблем, дружочек._\n*{fight_UN1}*_: Ну вот и хорошо, снимай с себя этот наряд._\n*{fight_UN2}*_: Умная жопка._\nОни оба начинают раздеваться.\n*{fight_UN1}*_: Я покажу тебе, кто босс этой качалки._\nОни были готовы к схватке.\n*{fight_UN1}*_: Ну всё, погнали!_\n*{fight_UN2}*_: Ага..._\n`всё заканчивается тем, что {fight_UN2} надрал зад своему противнику.`'
				else:
					pass
			else:
				pass
			bot.send_message(message.chat.id, fight_text, parse_mode='markdown')
		except:
			bot.send_message(message.chat.id, 'Нужно ответить на чьё-либо сообщение.')

	# ----- @ ----- Команды ----- @ ----- #

	# Обновления
	elif mes[0].lower() == '/update' or mes[0] == '/обновления':
		bot.send_message(message.chat.id, '*Последние обновления*\n \n*18.01.2020*\n—Добавлена возможность устраивать дуэли\n—Была удалена игра\n—Исправление ошибок\n \n*13.01.2020*\n—Исправлен текст игры\n—Добавлены обновления\n—Обновлено меню помощи\n—Упрощён код\n—Теперь можно красть трусики', parse_mode='markdown')

	# Помощь
	elif mes[0].lower() == '/help' or mes[0] == '/помощь':
		bot.send_message(message.chat.id, '*!дуэль* _(необходимо ответить другому пользователю)_ — устраивает дуэль между вами и тем, кому вы ответили этой командой\n*!кража* _(предмет в родительном падеже)_ — попытка кражи\n*!трусики* _(имя пользователя в родительном падеже)_ — кража нижнего белья\n*/update* `или` */обновления* — показать последние обновления', parse_mode='markdown')

	# Неизвестная команада
	elif message.text[0] == '!' or message.text[0] == '/':
		bot.send_message(message.chat.id, 'Неизвестная команда, в /help (/помощь) вы можете посмотреть доступные команды.')

bot.polling(none_stop=True)
