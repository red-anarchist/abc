import telebot
from random import randint

quotes_hachiman = ['Лучше наслаждаться манией величия, чем страдать от комплекса неполноценности.',
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
	'Какая разница кто я, когда ты шлюха?',
	'Те, кто наслаждается юностью в школьные годы — погубят себя в будущем.',
	'Вспоминая прошлое — хочется застрелиться от сожаления, а стоит задуматься о будущем — начинаешь переживать. Методом исключения, выходит, что здесь и сейчас лучше всего...',
	'Девушки сделаны из сахара, приправ и ещё чего-то прекрасного.',
	'Пусть в мире и существуют "хорошие девушки", но "удобных девушек" нигде не найти.',
	'Иногда люди, чтобы не потерять то, что им дорого, избавляются от чего-то иного, даже от своих отношений с другими.',
	'Жизнь — слишком горькая штука, так пусть хоть кофе будет сладким.',
	'В девственности нет ничего плохого!',
	'Если человек упал, все будут его топтать. Любому понравится издеваться над тем, над кем уже издеваются.',
	'Решать свои проблемы ложью, хвастовством и позёрством — на такое способен только человек.',
	'Умный в гору не пойдёт. Мудрый человек не будет соваться к кому бы то ни было без всякой на то причины. Идти на контакт с остальными значит — искать неприятности на свою голову. Вот и получается, что одиночки мудры.',
	'Люди эгоистичные, ровно как и самосознательные, всегда сопротивляются переменам. Всем на свете по определению хочется сохранить свою личность.',
	'Вера превращается в мысли, мысли переходят в слова, слова — в действия, действия — в привычку, привычки становятся ценностями, ценности — судьбой.']

quotes_jotaro = ['Чего ты боишься больше всего на свете? Больше всего ты боишься боли. Боль страшна? ... Ты не думаешь, что гораздо страшнее стать человеком, который не в состоянии сделать что-то сам?',
	'Без боли кто бы знал, что такое наслаждение?',
	'Тот, кто смеётся с закрытыми глазами, да ещё скрестив руки, точно знает, что выиграет.',
	'Человек взрослеет, побеждая над своим жалким прошлым.',
	'Всё начинается с осознания собственных слабостей.',
	'Любопытство — важный компонент человеческого развития.',
	'Ты же знаешь блох, да? Этих маленьких насекомых? Хоть мы, люди, и великаны для них, они всё равно нападают на нас. Можешь ли ты сказать, что это отвага? Нет, блохи не обладают отвагой. Тогда что такое отвага? Отвага — это познание страха! Преодоление его и подчинение!',
	'Паника — признак слабости духа.',
	'В нашей жизни бывают ситуации, когда возможности выбрать правильный путь у нас нет.',
	'Чем любопытнее человек, тем он психологически сильнее.',
	'Чтобы не пытался сделать негодяй, во всем облажается.',
	'Думая лишь о результате, люди начинают искать короткий путь. А на короткой дороге можно потерять истину из виду. И желание что-либо делать пропадёт. Думаю, важно лишь стремление узнать истину.',
	'Все мы живём в поисках кого то. Хорошего друга или прекрасной девушки.',
	'Страх нужно побеждать.',
	'Продолжая совершать преступления, обязательно тебя настигнет наказание, пришедшее из ниоткуда.']

quotes_arataka = ['Нельзя принимать деньги, чувствуя, что их не заработал. Если начнешь, то станешь постоянно выбирать легкую дорогу.',
	'Наличие сил не означает, что жизнь будет лёгкой. Но всё это ничего, пока мы можем выбирать то, что для нас важнее всего. Я главный герой своей жизни.',
	'Если ты не станешь сильнее, тебя будут использовать, будут помыкать тобой, и ты навсегда останешься лишь ступенькой для других.',
	'Будь ты одарённым до уровня бога, пусть ты не будешь как другие, но ты всё также остаёшься простым смертным.',
	'Человеческие чувства предназначены для того, чтобы откликаться на чувства других людей.',
	'Когда человек не может вести себя, как ему хочется, его чувства как бы замирают.',
	'За привлекательностью стоит человечность.',
	'У людского сердца две стороны медали. Так же, как счастье светит в тени печали, только в самой пучине страха рождается мужество.',
	'У работающих взрослых нет времени на игры с мечами.',
	'Не звезда освещается, а свет на сцене выделяет звезду.',
	'Жизнь, что вы ведете не изменить, как и абсурдность общества. Будет множество вещей, раздражающих и беспокоящих вас. Обидно, напрасно, жизнь лишь разочаровывает...',
	'Если ты влип... Можно просто убежать!']

quotes_alchemist = ['Встань и иди. Всё время вперёд. В конце концов у тебя есть отличные, здоровые ноги.',
	'35 литров воды, 20 килограммов углерода, 4 литра аммиака, 1,5 килограмма оксида кальция, 800 грамм фосфора, 250 грамм соли, селитры — 100 грамм, 80 грамм серы, 7,5 грамм фтора, 5 граммов железа и 3 грамма кремния. Плюс ещё 15 элементов. Из этого состоит тело среднего взрослого человека. Между прочим, все эти компоненты можно купить на рынке за гроши. Люди стоят дёшево.',
	'Для того, чтобы получить что-либо, необходимо дать что-либо взамен. Это принцип не только алхимии, но и всего мироздания.',
	'Безболезненный урок не имеет смысла. Тот, кто ничего не потерял, не сумеет ничего достичь.',
	'Если посмотреть объективно, то, если я умру, мир продолжит вращаться так, словно ничего не произошло.',
	'Не бывает идеальных планов. Этот мир несовершенен, поэтому он и прекрасен.',
	'Невозможно стереть из души то, что стало ее частью.',
	'Когда люди многое теряют, мне кажется, они что-то и приобретают взамен.',
	'Чтобы человечество могло двигаться вперёд, мы должны искать решения, выходящие за рамки правил.',
	'Всегда есть что-то более важное, чем мы и наши мечты.',
	'Мы должны двигаться только вперед, даже если мы можем только ползти!',
	'Человек может создать ровно столько счастья, сколько усилий к этому приложит.',
	'Мы не дьяволы и не боги... Мы люди... Всего лишь люди... Слабые, беспомощные люди.',
	'Если выхода нет, то его всегда можно сделать.',
	'Можно спать, страдая от боли, но нельзя спать, причинив боль!',
	'Когда человек хочет что-то получить, ему нужно чем-то пожертвовать. Таким образом, если хочешь получить что-либо, ты должен отдать взамен нечто равноценное. В алхимии это называется законом равноценного обмена. В то время мы верили, что это истина, правящая миром...',
	'Я уверен, что два человека могут общаться как личности, а не как представители своих народов.',
	'Я думал, дождь смоет мою печаль... Но с каждой каплей, упавшей на моё лицо, мне только тяжелее.',
	'Не бывает прав без обязанностей.',
	'Если ты живёшь, твоя жизнь рано или поздно окончится... Тело вернётся к земле. Над ним вырастут трава и цветы. Душа станет воспоминаниями и будет жить в сердцах других людей. Всё в этом мире течёт и движется по кругу. Это относится и к человеческой жизни.',
	'В конечном счёте, судьба тела — быть переработанным бактериями и стать пищей для растений. Эти растения станут пищей травоядных животных. А травоядные — пищей плотоядных. Вот так всё и идёт по кругу, даже если мы этого и не осознаём.',
	'Целые века стараний алхимиков не смогли сотворить жизнь! Но женщина способна это сделать всего за 280 дней!',
	'Лишь тот, кто сможет увидеть скрытую правду, получит ключ к победе.',
	'Узнав, что равноценный обмен — это неправда, я вздохнул с облегчением. Никакая равная плата не обязательна. Когда родители отдают любовь своим детям, не может быть стоимостей или награды.',
	'Хочешь совершенствовать разум — совершенствуй тело.',
	'Всё — это одно, а одно — это всё.',
	'Если кто-то старается, чтобы стать счастливым, то хочется, чтобы он был вознагражден за свои старания.',
	'Слишком много тех, из которых надо душу вытрясти! Если не начну записывать, точно забуду.',
	'Если можешь целиком отдаваться какому-либо делу — это и есть талант.',
	'Воспоминания — это такая штука: накладываются одно за другим, а самые старые блекнут.',
	'Наука идёт путём проб и ошибок. Не использовать опыт прошлого только из-за того, что это опасно, просто глупо.',
	'Этот мир течёт согласно закону, такому огромному, что мы и представить его себе не можем. Понять это течение, разложить на составляющие, создать заново... Это может алхимия!',
	'Мы движемся вперёд, потому что мы живём.',
	'Это так тяжело — объяснить ребёнку, что такое смерть.',
	'Месть взращивает побеги новой мести.',
	'Разве у тебя нет цели, к которой ты стремишься? Разве у тебя есть время останавливаться?',
	'Солнце тоже не Бог, это просто сгусток вещества высокой температуры. Если слишком приблизишься к солнцу — просто сгоришь.',
	'Если мы будем бояться, то ничего не достигнем.',
	'Суди о мужчинах не по словам, а по их делам. Когда случаются неприятности, они молча справляются с ними, не перекладывая ношу на других, не заставляя их волноваться.',
	'Мы верили в справедливость, когда были маленькими.',
	'Душа ранит сердца. Но она зажигает жизнь в сердцах других.',
	'Для того, чтобы жить, необходимо забирать жизнь у другого, справедливо это или нет.',
	'Всё в этом мире течёт, повинуясь огромному потоку. Смерть человека — неотъемлемая часть потока.',
	'Если каждый, кто проиграл войну, решит мстить, то смертям конца не будет.',
	'Смерть всегда следует за убийцами. Жить рука об руку со смертью. Работа, на которой рискуешь душой, просто прекрасна. Наградой же мне служит поле боя.',
	'За правдой скрывается правда!',
	'Автоброню можно заменить, а жизнь — она одна!',
	'Вся логика нашего мира выражается, в основном, в законе равноценного обмена. Права получают вместе с обязанностями...',
	'Мечта, которая может исполниться, — ненастоящая мечта.',
	'Для завершения любого дела нужна жертва.',
	'Нельзя реконструировать живое существо, единожды лишившееся жизни. Кем бы ты ни был.',
	'Чем больше людей за столом, тем вкуснее еда.',
	'Порой необходимо остановиться и спокойно обо всём подумать.',
	'Молодым полезно гоняться за мечтой.',
	'Пытайся, экспериментируй, и, может, ты откроешь новые законы, которым потом подчинится этот мир.',
	'Я думаю, в этом мире нет ничего, на что можно было бы равноценно обменять мамину душу...',
	'Вызови гнев! Посей смятение! Не поддавайся на провокации врага!',
	'В драке сойдёт любая хитрость!']

ranElement = lambda l : l[randint(0,len(l)-1)]

hachiman_bot = telebot.TeleBot('1195524530:AAEiqqtCNonICXijH07775JqHF1vtn3Jnj8')
jotaro_bot = telebot.TeleBot('1176602512:AAHPDFTPrFxpW4ZGnJ1fvp5UFJlWVT0qEXc')
arataka_bot = telebot.TeleBot('1228187002:AAHa3fKbasoJAXpd6fbwQF13DoGLiwUxWOQ')
alchemist_bot = telebot.TeleBot('806229641:AAG9p3malOMMtM2z5I1MDPgcpeky6ia2iNI')

@hachiman_bot.message_handler(content_types=['text'])
def hachimanMessage(message):
	if message.text.lower() == 'хачиман, цитата' or message.text.lower() == 'хачиман цитата' or message.text.lower() == 'хачиман, цитату' or message.text.lower() == 'хачиман цитату':
		hachiman_bot.send_message(message.chat.id, ranElement(quotes_hachiman))
	elif 'хикки' in message.text.replace('!', '').replace('.', '').replace(',', '').replace('?', '').lower().split():
		hachiman_bot.send_message(message.chat.id, 'Не называй меня Хикки, сучка.')
	elif message.text.lower() == 'хачиман':
		hachiman_bot.send_message(message.chat.id, 'Скажи ещё три раза.')
	elif 'хикитани' in message.text.replace('!', '').replace('.', '').replace(',', '').replace('?', '').lower().split():
		u = [f'{message.from_user.first_name}, заткнись!', 'Всё равно неправильно.', 'Вообще-то Хикигая.', 'И кстати, меня никогда не звали Хикитани.']
		hachiman_bot.send_message(message.chat.id, ranElement(u))

	if message.chat.id == message.from_user.id and message.from_user.username == 'ever_soup':
		hachiman_bot.send_message(-1001433940163, message.text)

	if message.text.lower() == 'джотаро, цитата' or message.text.lower() == 'джотаро цитата' or message.text.lower() == 'джотаро, цитату' or message.text.lower() == 'джотаро цитату':
		jotaro_bot.send_message(message.chat.id, ranElement(quotes_jotaro))
	elif message.text.lower().replace('!', '').replace('.', '').replace(',', '').replace('?', '') == 'жотаро':
		jotaro_bot.send_message(message.chat.id, 'ДЫО!!!')
	elif message.text.lower().replace('!', '').replace('.', '').replace(',', '').replace('?', '') == 'любишь кабачки' or message.text.lower().replace('!', '').replace('.', '').replace(',', '').replace('?', '') == 'любишь кабачки джотаро':
		u = ['Твои кабачки - говно ёбаное.','Кабачки... Я их, блять, ненавижу!']
		jotaro_bot.send_message(message.chat.id, ranElement(u))
	elif 'муда' in message.text.replace('!', '').replace('.', '').replace(',', '').replace('?', '').lower().split():
		jotaro_bot.send_message(message.chat.id, 'ОРА! '*10)
	elif message.text.lower().replace('!', '').replace('.', '').replace(',', '').replace('?', '') == 'стар платинум':
		jotaro_bot.send_message(message.chat.id, 'ОРА! '*20)
	elif message.text.lower().replace('!', '').replace('.', '').replace(',', '').replace('?', '') == 'джотаро':
		jotaro_bot.send_message(message.chat.id, 'Яре Яре Дазе.')

	if message.text.lower() == 'рэйгэн, цитата' or message.text.lower() == 'рэйгэн цитата' or message.text.lower() == 'рэйгэн, цитату' or message.text.lower() == 'рэйгэн цитату':
		arataka_bot.send_message(message.chat.id, ranElement(quotes_arataka))

	if message.text.lower() == 'эдвард, цитата' or message.text.lower() == 'эдвард цитата' or message.text.lower() == 'эдвард, цитату' or message.text.lower() == 'эдвард цитату':
		alchemist_bot.send_message(message.chat.id, ranElement(quotes_alchemist))

hachiman_bot.polling(none_stop=True)
jotaro_bot.polling(none_stop=True)
arataka_bot.polling(none_stop=True)
alchemist_bot.polling(none_stop=True)
