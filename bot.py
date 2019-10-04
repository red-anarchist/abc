# -*- coding: utf-8 -*-
import telebot
import random

bot = telebot.TeleBot('981943532:AAHI9aAZkRG4Q0UuNIy2wKtve_y9QFMf9FU')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message('Привет!')

steal_wait = {}
steal2_wait = {}

@bot.message_handler(content_types=['text'])
def text(m):
	if m.text[:6].lower()=='!кража':
		if m.from_user.id not in steal2_wait:
			chance = random.randint(1, 100)
			if random.randint(1, 100)<=chance:
				success = 1
			else:
				success = 0
			t1 = m.text.split()
			i = 1
			target = ''
			while i<len(t1):
				if i + 1 == len(t1):
					target += t1[i]
				else:
					target += t1[i]+' '
				i += 1
			target = target.replace('*', '').replace('_', '').replace('`', '')
			target2 = None
			if target == '':
				return
			text = '*' + name + '* успешно реализует кражу *' + target + '! Шанс на успех был целых ' + str(chance) + ' процентов!'
			if success == 1:
				bot.send_message(m.chat.id, text, parse_mode = 'markdown')
			else:
				bot.send_message(m.chat.id, 'У *' + name + '* не хватает умения реализовать кражу *' + target + '*! А ведь шанс был целых ' + str(chance) + ' процентов!')
			steal2_wait.update({m.from_user.id:{'timer':60}})
		else:
			secs = steal2_wait[user['id']]['timer']
			bot.send_message(m.chat.id, '*' + name + '*, вы сможете красть через ' + str(secs) + ' секунд.', parse_mode = 'markdown')

bot.polling(none_stop=True)
