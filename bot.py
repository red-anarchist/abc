import telebot
from random import randint

quotes = ['Лучше наслаждаться манией величия, чем страдать от комплекса неполноценности.',
	'Один. Всегда — один. В этом есть своя прелесть: не нужно ни за кого быть в ответе — только за себя самого и только перед собою же, любимым. Одиночество болезненно, но, поверьте: к нему привыкаешь. И привыкаешь тем быстрее, чем яснее тебе дают понять, что ты никому не нужен.',
	'Ничто не дает столько преимуществ перед другими, как способность оставаться спокойным и хладнокровным в любой ситуации.',
	'Работать — значит проиграть.',
	'Моя жизнь не какое-нибудь любовное кино. Я достаточно подкован, чтобы не попадаться в типовую романтик-комедийную ловушку. Девушки помешаны на красавчиках и порочных связях. Другими словами, они — мои враги. А ненависть — лучший способ избежать и не попасться в эту западню.',
	'Если кого-то уже бросили. Говорят изменишь себя и сможешь изменить мир, но это все вранье. Когда всех судят это превращается в стереотип. Одиночке приходится быть одному. Попробуешь выделится и тебя начнут осуждать. Таковы законы детского королевства.',
	'Для животных естественны группы. Хищникам присуще жестокая иерархия. Тот кому не удалось стать вожаком обречен страдать до самой смерти. Травоядные же постоянно вынуждены сталкиваться с дилеммой, погибнуть самому, или пожертвовать товарищем. В нашем мире образование групп не дает никакого преимущества отдельно взятому индивиду поэтому я и выбрал для себя модель поведения медведей. Медведь — самодостаточное животное живущее в одиночестве без всяких тревог к тому же зимой впадает в спячку, чего еще можно желать. Если бы была следующая жизнь, я бы непременно хотел стать, медведем.',
	'Терпение и труд некогда не предадут, а вот мечта предать может. Естественно все мы стараемся, чтобы исполнить свою мечту, но чаще всего она ведь не сбывается. Но плоды старания станут утешением.',
	'Гораздо лучше, когда тебе сразу говорят «да» или «нет». Тогда не случается никакого недопонимания. Услышал «нет» и сразу понял, что ты ей неинтересен. И спокойно уходишь в тень. Это ж чёрт знает сколько несчастных парней могло бы спасти, заверяю вас.',
	'Пытаясь не делать оправданий из потерянного, мы ещё больше пытаемся взять себя в руки и ещё больше пытаемся вести себя как обычно.',
	'Проблема не является проблемой, не став проблемой.',
	'Когда человеку страшно, он ни о ком, кроме себя не думает. Он постарается выжить, даже если придется пожертвовать другими. Стоит человеку показать эту сторону, и с ним уже никто не захочет дружить.',
	'Те, кто думают, что в очках выглядят умнее, особым умом не отличаются.',
	'Не страшно ошибиться, ведь можно задать вопрос снова. А потом ещё раз.',
	'Говорят: "Изменишь себя и сможешь изменить мир", но это всё бред. Заставляют идти на компромисс, кормят выдумками...',
	'Когда говорят, что ты хороший — это значит, что ты ничтожество.',
	'Когда о ком-то судят — это превращается в стереотип. Одиночке приходится быть одному. Попробуешь выделиться и тебя начнут осуждать.',
	'Когда идёшь куда-то, где небезопасно, или просто попадаешь куда-то впервые, обязательно надо проверить, всё ли там в порядке, пропустив даму вперёд.',
	'Какая разница кто я, когда ты шлюха?'
	'Те, кто наслаждается юностью в школьные годы — погубят себя в будущем.',
	'Вспоминая прошлое — хочется застрелиться от сожаления, а стоит задуматься о будущем — начинаешь переживать. Методом исключения, выходит, что здесь и сейчас лучше всего...',
	'Девушки сделаны из сахара, приправ и ещё чего-то прекрасного.',
	'Пусть в мире и существуют "хорошие девушки", но "удобных девушек" нигде не найти.',
	'Иногда люди, чтобы не потерять то, что им дорого, избавляются от чего-то иного, даже от своих отношений с другими.',
	'Жизнь — слишком горькая штука, так пусть хоть кофе будет сладким.']

ranElement = lambda l : l[randint(0,len(l)-1)]

bot = telebot.TeleBot('1195524530:AAEiqqtCNonICXijH07775JqHF1vtn3Jnj8')

@bot.message_handler(content_types=['text'])

def get_text_message(message):
	if message.text.lower() == 'хачиман, цитата' or message.text.lower() == 'хачиман цитата' or message.text.lower() == 'хачиман, цитату' or message.text.lower() == 'хачиман цитату' or message.text.lower() == 'ебани цитатку':
		bot.send_message(message.chat.id, ranElement(quotes))
	elif 'хикки' in message.text.replace('!', '').replace('.', '').replace(',', '').replace('?', '')lower().split():
		bot.send_message(message.chat.id, 'Не называй меня Хикки, сучка.')
	elif message.text.lower()[0:6] == 'хачиман' and len(message.text) < 9:
		bot.send_message(message.chat.id, 'Скажи ещё три раза.')
	elif 'хикитани' in message.text.replace('!', '').replace('.', '').replace(',', '').replace('?', '')lower().split():
		u = ['{message.from_user.first_name}, заткнись!', 'Всё равно неправильно.', 'Вообще-то Хикигая.']
		bot.send_message(message.chat.id, ranElement(u))

bot.polling(none_stop=True)
