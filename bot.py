import telebot
from random import randint, choice
from fuzzywuzzy import fuzz

quotes = {
	'Yahari Ore no Seishun Love Come wa Machigatteiru / Розовая пора моей школьной жизни — сплошной обман':{
		'Hikigaya Hachiman / Хикигая Хачиман':[
			'«Главное не победа, а участие» — известная фраза, сказанная Пьером де Фреди, бароном де Кубертеном во время своей речи. Но эту цитату частенько используют не по назначению. Например, в виде предлога, чтобы заставить принять участие в чём-либо. Сумасбродных затей на свете миллионы. Если главное это участие, то можно отыскать смысл и в неучастии. Если всё стоит попробовать, то логично предположить, что ничего не пробовать тоже стоит попробовать. По сути, не пробовать то, что пробуют другие тоже можно назвать ценным опытом.',
			'Терпеть не могу добрых девушек. Стоит с ней поздороваться, и не идёт из головы, начнёт переписываться, западёт в сердце. А уж вдруг позвонит, будешь раз за разом заглядывать в список входящих не в силах сдержать улыбки. Но я уже это проходил, вот что такое доброта... Если кто-то добр ко мне, как и к остальным, я сам замечаю, как начинаю забывать... Раз за разом надеешься, каждый раз обжигаешься и сам не замечаешь, как теряешь надежду.',
			#'Для животных естественно образовывать группы, хищникам присуща жестокая иерархия. Тот, кому не удалось стать вожаком, обречён страдать до самой смерти. Травоядные же постоянно вынуждены сталкиваться с дилеммой: погибнуть самому или пожертвовать товарищем. В нашем мире образование групп не даёт никакого преимущества отдельно взятому индивидууму, потому я и выбрал для себя модель поведения медведей. Медведь — самодостаточное животное, живущее в одиночестве без всяких тревог, к тому же зимой впадает в спячку. Чего ещё можно желать? В следующей жизни я непременно хочу стать медведем.',
			'Я люблю себя. Ни разу за всю жизнь не случалось, чтобы я себя ненавидел. Мои неплохие данные, местами симпатичное лицо, пессимистичные взгляды и повальный реализм меня, в общем-то, вполне устраивают. Но сейчас я, кажется, впервые себя возненавидел. Юкиносита Юкино в моих глазах была всегда прекрасна, абсолютно честна, открыта. Она твёрдо стоит на своих ногах, ни на кого не надеясь. И такой Юкиноситой Юкино я, на самом деле, всегда восхищался. Я сам по себе начал многого от неё ждать, сам по себе возвёл её в идеал, сам по себе решил, что понимаю её, и сам по себе в ней разочаровался. Сколько раз я предупреждал себя, но в итоге всё оказалось без толку. Врут все, включая Юкиноситу Юкино. И за то, что я не могу простить ей эту, присущую каждому человеку черту... Я... Ненавижу себя.',
			'Вспоминая прошлое, хочется застрелиться от сожаления, а стоит задуматься о будущем, начинаешь переживать. Методом исключения понимаешь, что здесь и сейчас, лучше всего.',
			'Человек не всегда виноват. Твое окружение, общество, мир — все они ошибаются уже давно. Говоря, что ты можешь изменить себя, ты лишь подстраиваешься под этот дрянной, холодный и равнодушный мир. Признавая, что проиграл системе, становишься её рабом. Украшая правду красивыми словами, пытаешься обмануть окружающих и себя...',
			'Лучше наслаждаться манией величия, чем страдать от комплекса неполноценности.',
			'Нет никаких проблем, пока проблема не стала проблемой.',
			'При общении лишь 30% информации приходится на слова, а остальные 70% можно прочитать по движению глаз, жестам и позам. Проще говоря, даже ни с кем не разговаривающий одиночка может получить эти самые 70%.',
			'Раз не ладится в отношениях, возьми и разрушь их. Если одиночками станут все, не будет ни драк, ни конфликтов.',
			'Доверять другим. Помогать и поддерживать. Многие бы сказали, что так и надо. Но это просто идеализм. В реальной жизни всё сваливается на кого-то одного.',
			'Те, кто думают, что в очках выглядят умнее, особым умом не отличаются.',
			'Если для полноценной жизни приходится унижаться, то лучше по жизни шагать одному.',
			'Одиночке приходится быть одному. Попробуешь выделиться — и тебя начнут осуждать.',
			'Мне кажется, незнание — это не так уж и плохо. Ведь с новыми знаниями появляются и новые проблемы.',
			'С каких это пор не меняться, значит бежать от чего-то? Почему мне нельзя жить в согласии с собой, а не с окружающими?',
			'Я не собираюсь ждать тех, кто никуда не идёт!',
			'Терпение и труд никогда не предадут, а вот мечта предать может. Естественно, что все мы стараемся, чтобы исполнить свою мечту, но чаще всего она ведь не сбывается... Но плоды старания станут утешением.',
			'Если бы я мог получить всё, что пожелаю... Получить то, чего хочу... Я бы точно ничего не желал и не просил. Ведь полученное просто так, в подарок — лишь подделка, что однажды исчезнет без следа. Потому я наверняка предпочту и дальше стремиться.',
			'Мечты не всегда сбываются. Если стараешься, это еще не значит, что мечты сбудутся. Чаще всегда так и бывает. Но то, сколько сил ты на это потратил, станет отличным утешением.',
			'Не в моих правилах хвататься за прошлое. Если жить одним прошлым, то погрязнешь во тьме.',
			'Мир никогда не изменится, но себя изменить можно. Вопрос: как же тогда измениться? Ответом будет: «стать богом нового мира».',
			'Короткие фразы — лучшие. Их функционал просто не знает границ! Хочешь, прекрати разговор одним словом, хочешь, этим же словом его поддержи. Панацея двадцать первого века, не иначе!',
			'У каждого есть что-то для него важное, чего он не хочет лишиться. Ради этого прячутся, притворяются. Поэтому, все люди — это лжецы, но величайший из них. Это я.',
			'Начать жить заново невозможно, но начать заново отношения вполне.',
			'Мужчины — существа простые. Одного разговора с девушкой хватает, чтобы выбиться из колеи. А получить в подарок печенье — вообще взрыв эмоций. И неважно, вкусное оно или нет.',
			'Я всё усваивал в одиночку. Пока вы беззаботно веселились и утешали друг друга, я со всем справлялся один.',
			'Да ладно, нет ничего страшного во лжи. Я вот вру постоянно. Нет ничего страшного в том, чтобы притворяться, будто бы ты чего-то не знаешь. Скорее неправильно заставлять других принять то, что они принимать не хотят.',
			'То, что происходит перед моими глазами — часть моей жизни и ничьей другой. И нехрен в нее лезть.',
			'Дураки, что стремятся наслаждаться юностью, погубят сами себя.',
			'Когда человеку страшно, он ни о ком, кроме себя не думает. Он постарается выжить, даже если придется пожертвовать другими. Стоит человеку показать эту сторону, и с ним уже никто не захочет дружить.',
			'Говорят: «Изменишь себя и сможешь изменить мир», но это всё бред. Заставляют идти на компромисс, кормят выдумками...',
			'Быть единственным несогласным неправильно. Чувствовать себя недовольным так раздражает. Как будто мне больше всех надо.',
			'Моя жизнь не какое-нибудь любовное кино. Я достаточно подкован, чтобы не попадаться в типовую романтико-комедийную ловушку. Девушки помешаны на красавчиках и порочных связях. Другими словами, они — мои враги. А ненависть — лучший способ избежать и не попасться в эту западню.',
			'Чем злее правда, тем добрее ложь, потому доброта — это ложь...',
			'«Ни шагу назад» — девиз, подходящий разве что для солдата. Нельзя во всём винить себя. Часто бывает, что виновато общество, мир или окружающие. Изменить себя — значит просто приспособиться к этому безразличному и жестокому, похожему на помойку миру. Словно принять поражение и стать его рабом. Это просто облачённая в красивые слова ложь, чтобы успокоить всех вокруг и себя заодно.',
			'Мама учила меня не делить всё на «люблю» и «не люблю»...',
			'Не страшно ошибиться, ведь можно задать вопрос снова, а потом еще раз.',
			'Короче, слушай сюда, чел, обычное признание — ничто по сравнению с пулей в спине, не жди второго выстрела, признайся, пока тебя не отвергли.',
			'Чем постоянно бояться сказать кому-нибудь правду, лучше вообще ни с кем не разговаривать.',
			'Дружба — это такие отношения, когда с тобой даже не разговаривают.',
			'Я не амбициозен, я самомотивирован.',
			'Как рыбак рыбака видит издалека, так и одиноких тянет друг к другу неведомая сила.',
			'Настоящие друзья могут болтать просто так на любую тему. В этом и заключается дружба.',
			'Доброта — это яд.',
			'Среднестатистический парень уже давно бы в неё по уши влюбился. У непопулярных парней есть дурная привычка искать скрытый смысл в нелепых совпадениях и чистых случайностях. Но я не верю в совпадения, судьбу и предназначение.',
			'Если враг не старается во всю, никто не захочет стать лучше. Ведь именно войны всегда двигали науку вперёд.',
			'Любая девушка с сочными персиками однажды станет бабушкой с морщинистой курагой... Так зачем тебе потом этот компот, если сейчас ты наберешься смелости попробовать фрукты.',
			'Хорошо, самое время склонить голову. Когда готов сдаться, приходится отбросить гордость. А у меня от нее одно только название.',
			'Не ровняй меня с остальными. У меня есть невероятный дар быть не таким, как все, даже будучи одним из любого большинства.',
			'В день вступительной церемонии в старшей школе я попал в аварию. Я с таким волнением ждал начала новой жизни, что выехал из дома на целый час раньше. В результате, был госпитализирован с переломом, а заодно был обречен на судьбу одиночки.',
			'Я, конечно, не такой твердолобый, чтобы не понять, что к чему после такого-то спектакля, скорее наоборот, весьма восприимчивый: восприимчивый, чувствительный и весьма тонко на все реагирующий. Восемьдесят процентов парней, случись такое в их жизни, тут же подумали: «Она же в меня втюрилась!». Потому, лучше сразу одернуть себя фразой: «Быть такого не может!».'
			'В такие моменты лучше не привлекать к себе внимание и отойти на задний план. Надо вспомнить, как я играл дерево в младшей школе.',
			'Её индивидуальность, моя индивидуальность. Наверняка, какая-то часть нашего поведения определена кем-то другим. И она сбивает нас с пути. Мы хотим стать сами собой. Только вот, кто же всё-таки определяет кто мы есть.'
		],

		'Hiratsuka Shizuka / Хирацука Шизука':[
			'Люди одним своим существованием неосознанно причиняют кому-то боль. Будут они жить или умрут, это причиняет кому-то боль. Будешь иметь с кем-то дело — причинишь боль, а попытаешься дела не иметь — сделаешь еще больнее. Но если человек безразличен, то даже не понимаешь, что сделал ему больно. Нужно лишь осознать это. Когда человек тебе дорог, ты понимаешь, когда сделал ему больно. И дорожить кем-то, значит быть готовым причинить ему боль.',
			'Впечатление о людях меняется изо дня в день. Когда ты проводишь с ними время, вместе растёшь, ты начинаешь понимать их всё лучше и лучше.',
			'Судя по всему, причина твоего одиночества — в прогнившей душонке, гиперчувствительности и страхе быть отвергнутым.',
			'Наверняка сейчас для вас настоящее — это всё, но это совсем не так. Когда-нибудь всё плохое и хорошее уравновесится, так уж устроен мир. Настоящее — это ещё не всё, но есть то, что можно сделать только сейчас. То, что можно найти только здесь. Время не ждёт, время пришло... Думай, старайся, страдай, борись, переживай, а иначе вся жизнь не по-настоящему.',
			'Когда тебя ругают – это не всегда плохо. Так люди проявляют заботу.'
		],

		'Yukinoshita Yukino / Юкиносита Юкино':[
			'Тот, кто не прилагает ни малейших усилий, не смеет завидовать таланту. Неумехи даже не представляют, сколько времени и сил тратят умехи, чтобы добиться цели.',
			'Никто не идеален. Все люди слабы, мерзки и завистливы. Они терпеть не могут, когда есть кто-то лучше них. Жизнь выдающихся людей всегда была трудной. Глупо ведь, согласен?',
			'Если уж так хотите судить человека по обложке, то не учитывайте при этом лишь одну часть тела. Посмотрите на общий баланс...',
			'И касательно твоей внешности. Запомни — красоту оценивают окружающие, а не ты. Проще говоря, крут ты или нет, решать мне.',
			'Может хватит уже оглядываться на других? Меня это из себя выводит. Разве не стыдно прятаться за окружающими, чтобы оправдать собственную неуклюжесть, неловкость и глупость?',
			'Все эти глупые сказки о рыцарях на белых конях не имеют никакой связи с реальностью. Просто глупая выдумка, созданная, чтобы успокоить детей. В жизни люди просто смиряются друг с другом, со своими убеждениями и желаниями. Выбирают из двух зол меньшее. Но что делать, если оба зла равны? Нет какого-то очевидного, наносящего меньше вреда, чем другой.',
			'Думаешь, ты сможешь работать в команде? Подобного тебе они никогда не примут. Скорей, они найдут в твоём лице общего врага. Быть может, это и поможет объединить клуб... Но они потратят столько сил на то, чтобы выжить тебя, что на самосовершенствование их уже не хватит. Так что их проблем это не решит. Знаю по себе. Раньше я жила за границей. Я вернулась на родину, когда училась в средней школе. Все девушки в школе старались всеми силами меня выжить. Но ни одна из них даже не попыталась стать лучше, чтобы превзойти меня.',
			'Слабые, уродливые, готовые из-за ревности исподтишка напакостить. Как ни странно: чем ты лучше других, тем тебе тяжелее. Разве это правильно?',
			'Нам никогда не понять, что думают другие. Пусть мы и знаем друг друга, но понять друг друга — совсем другое дело.',
			'Доброта иногда бывает жестока...',
			'Каждый судит в меру своей испорченности.',
			'Когда не знаешь, куда дальше двигаться — не найти своего места. Остаётся прятаться, плыть по течению, за чем-то гнаться и биться в невидимые стены.',
			'Почему не спишь? Крепкий вечный сон пошел бы тебе на пользу.'
		],

		'Yuigahama Yui / Юигахама Юи':[
			'Как можно быть таким умным и еще не понимать что-то простое? Я никогда не хотела видеть что-то подобное.',
			'Есть вещи, о которых не хочется рассказывать. Упустишь нужный момент — и потом не можешь.',
			'Талант? Похоже, у меня его нет...'
		]
	},


	'Neon Genesis Evangelion / Евангелион нового поколения':{
		'Shinji Ikari / Синдзи Икари':[
			'Если мы будем просто продолжать жить, то однажды мы будем рады тому, что живы.',
			'Когда затыкаешь уши, сердце тоже недоступно. Поэтому я не соприкасаюсь с ненавистным миром.',
			'Никогда не говори «прощай» перед боем. Это слишком грустно.'
		],

		'Ikari Gendo / Икари Гэндо':[
			'Люди живут только потому, что могут забывать прошлое. Но есть вещи, которые нужно помнить всегда.',
			'Всё-таки первый враг человека — он сам.',
			'Стрелки часов не повернуть вспять. Но в наших силах двигать их вперед!'
		],

		'Kaji Ryohji / Кадзи Рёдзи':[
			'Нам не нужны причины, чтобы влюбиться, но для расставания мы всегда стараемся найти повод.',
			'Ты просто веришь, что кое-что узнал. Люди и себя-то толком не понимают, а других ещё меньше. Понять всё на сто процентов невозможно. Вот почему мы тратим столько времени на понимание причин собственных поступков и поступков других. Поэтому жизнь так интересна.',
			'Я не боюсь узнать свои слабости, поскольку они — часть меня самого. А я принимаю себя таким, какой я есть!',
			'Доброта — не есть проявление слабости.',
			'Жить — значит меняться.',
			'Практично быть склонным к естественным желаниям.'
		],

		'None':[
			'Твой разум смешивает истину с твоим восприятием реальности, так рождается твое мнение. Человек видит только то, что он хочет видеть.',
			'Тот, кто сам знает боль, лучше относится к людям — это не слабость.',
			'Ты ничего не мог поделать, со страхом узнать, что другие думают о тебе, потому ты избегал всех.',
			'Иероглиф, который мы используем для слова «она», так же означает «женщина в далеке». Чтобы мы не делали, для нас женщины останутся на другом берегу великой реки непонимания, поток реки между мужчинами и женщинами шире и глубже, чем любой океан.',
			'Человеческие истины так просты, что большинство даже не хочет задуматься о них, чтобы понять хоть то, что ты, например, просто не привык кому-то нравиться.',
			'Понимая различия между собой и окружающими, ты укрепляешь понимание себя.',
			'Любой может научиться судить о вещах с помощью услышанных от других истин, например, солнечный день поднимет тебе настроение, дождливый сделает тебя унылым, когда тебе это говорят, ты принимаешь эти слова на веру, но ты можешь радоваться и в дождливый день, ты легко можешь изменить свою истину, поскольку истина у людей непостоянна.',
			'Я не больше и не меньше, чем я.',
			'Тот, кто действительно ненавидит себя, не может любить, он не может довериться другому человеку.',
			'Твое сознание выделяет из реальности только то, что плохо и ненавистно, только сознание отделяет правду от реальности, твое видение реальности изменяет твое понимание ее природы.',
			'Переполненное печалью, ненавистью, страданием... Вот какое оно, твоё сердце.',
			'Никто никогда полностью не поймет другого человека.',
			'Посмотрите на них: мать и дочь — они сами словно куклы. Возможно, между людьми и куклами не так много различий. Ведь человек создаёт куклы по своему подобию. И, если Бог действительно существует, мы все, наверное, просто игрушки для него.',
			'Тот, кто забыл ошибки прошлого, обречен их повторить.',
			'Люди не способны создать нечто из ничего. Им нужно отталкиваться от чего-то. Ведь человек — не бог.',
			'Ты — это ты. Невелика разница между тем, как ты воспринимаешь себя и как тебя воспринимают другие.',
			'Познание — это удовольствие. Понимание — это контроль.'
		],

		'Asuka Langley Soryu / Аска Ленгли Сорью':[
			'Всё, что ты делаешь — сидишь и ждёшь, когда кто-нибудь сделает тебя счастливым! Но это фальшивое счастье!',
			'Ручной мужчина хуже кролика.',
			'Беспокоиться о ком-то гораздо тяжелее, чем самому подвергаться опасности.',
			'Я отличаюсь от этих людишек! Я особенная! И поэтому, отныне и впредь... Тебе придется быть одной, Аска.',
			'Я ненавижу. Ненавижу всё. Ненавижу всех. Но больше всего я ненавижу себя. Я больше не вижу смысла в своей жизни.'
		],

		'Kaworu Nagisa / Каору Нагиса':[
			'Ты избегаешь личных связей... неужели близость так пугает тебя? Если ты ни с кем не близок — тебя никто не предаст и не сделает тебе больно. Однако так ты никогда не забудешь об одиночестве. Человек всегда одинок, он не может полностью избавиться от одиночества. Но он может забыть о нём. В этом человек находит силы жить. Человек всегда носит боль в своем сердце. Сердце его болит, поэтому вся жизнь для него боль. Ты хрупкий как стекло. И этим ты мне симпатичен. Проще говоря — я люблю тебя.',
			'Петь — хорошо. Пение оживляет душу. По-моему, песня — величайшее достижение культуры Лилим.',
			'Люди — очень странные создания! Почему-то их ужасно волнует мнение других. Из-за этого они злятся, переживают, впадают в отчаяние... Люди не перестают поражать меня.',
			'Своя собственная смерть — вот единственная полная свобода.'
		],

		'Ayanami Rei / Аянами Рей':[
			'Людей много, но зачастую ты одинок даже в толпе.',
			'Человечество боится тьмы, поэтому изгоняет её огнём.',
			'Горы... огромные горы... нечто изменяющееся на протяжении тысячелетий. Небо... синее небо... нечто невидимое, нечто реальное. Солнце... оно всего лишь одно. Вода... нечто приятное... командующий Икари? Цветы... все одинаковые и все бесполезные. Небо... красное-красное небо... Красный цвет. Я не люблю красный. Всплеск воды. Кровь. Запах крови. Девочка, у которой нет крови. Человек, созданный из красной глины... человек, рождённый мужчиной и женщиной. Город. Он построен людьми. Ева. Она создана людьми... Что есть человек? Нечто созданное Богом? Или нечто созданное людьми? У меня есть жизнь и душа... И я живу для своей души. Контактная капсула — это трон души... Кто я? Это я. Кто Я? КТО я? Что Я?... Я — это я. Это я! Это моя видимая оболочка. У меня такое чувство, как будто это не я... Какое странное чувство... Моё тело словно растворяется. Я не вижу себя... Мой образ расплывается. Но я чувствую присутствие кого-то. Кто тут кроме меня?..',
			'Истина внутри тебя.',
			'Ты ищешь себя в глазах других людей. Ты боишься одиночества. Боишься, что перестанешь существовать как личность, если все тебя покинут.',
			'Меня создало общение с людьми. Они создают меня, я создаю их.'
		],

		'Aida Kensuke / Аида Кенске':[
			'С тобой она ведёт себя естественно, так, как ни с кем другим. Это значит, что ты для неё часть семьи.',
			'Дурак тот, кто дерётся без шансов на победу.'
		],

		'Misato Katsuragi / Мисато Кацураги':[
			'Для чего нужна эта проклятая наука, если она не может спасти даже одну жизнь.',
			'Только люди пытаются подчинить себе то, что может их уничтожить. Только люди могут быть так безрассудны.',
			'Люди — незавершенные существа, они не могут нормально жить в одиночестве. Однако им приходится жить, несмотря на эту незавершенность. А раз уж мы созданы такими, я думаю, и в том, что мы ищем тех, кто избавит нас от одиночества, и даже в том, что мы раним друг друга, есть смысл.',
			'Тебя не интересуют другие, но ты ненавидишь одиночество.',
			'Выживает тот, у кого есть воля к жизни.',
			'Может быть, тебе и легче только делать вид, что ты стараешься для других... Но в бою это притворство приведет к смерти!',
			'Я по-прежнему ненавижу темноту, она приносит с собой самые ужасные воспоминания.',
			'Он так одинок... Может, он боится женщин?... Нет. Он просто боится привязаться к кому-то.'
		],

		'Ritsuko Akagi / Рицуко Акаги':[
			'Существует, так называемая, «Дилемма дикобразов». Если они захотят согреть друг друга, то чем тесней они сблизятся, тем сильнее будет боль от уколов игл. Тоже самое и с людьми. Должно быть, Синдзи замкнут так замкнут, потому что боится уколоться.',
			'Не запятнав себя, сложно выжить среди людей.',
			'Гомеостаз и транзистаз. Силы поддерживающие или изменяющие текущую ситуацию. Эти противоборствующие силы живут внутри каждого живого существа.'
		]
	},


	'Death Note / Тетрадь смерти':{
		'L Lawliet / Эл Лоулайт':[
			'Человек, который пытается кому-либо подражать, всё равно делает это по-своему! Никто не может скрыть свою натуру и привычки!',
			'Не бывает безвыходных ситуаций… Тебе просто нужно умереть раньше, чем они тебя убьют.',
			'Рисковать жизнью — это одно, а поступить необдуманно и напрасно лишиться жизни — бессмысленно и нелепо.',
			'Поставить жизнь на карту — это одно, отдать её по глупости — совершенно другое.',
			'Можешь говорить что угодно, но пирожное я заберу.',
			'Если есть сладкое и при этом шевелить мозгами, то не потолстеешь.',
			'Глупо следовать совету того, кого ты подозреваешь.',
			'В моих руках есть средство, а в сердце — желание!',
			'Если я сяду по-другому, мои дедуктивные способности уменьшатся на 40%.',
			'Пока мы связаны этими наручниками — у нас одна судьба!',
			'Это настолько очевидно, что мне трудно в это поверить.',
			'Личные побуждения мешают трезво мыслить.',
			'Справедливость всегда одерживает победу.'
		],
		'Raito Yagami / Лайт Ягами':[
			'Нельзя выиграть, если ты только защищаешься. Чтобы выиграть, нужно идти в атаку.',
			'Я создам идеальное общество, создам такой мир, в котором будут жить только ответственные и добрые люди!',
			'Но я знаю одно — я никогда не стану лгать, чтобы намеренно навредить человеку.',
			'Если немного подумать, то без скольких людей мир стал бы лучше.',
			'Недосыпание подрывает здоровье и снижает мыслительные способности.',
			'Убийство человека богом смерти и убийство человека человеком – это разные вещи.',
			'Эл, ты знаешь, что боги смерти едят одни только яблоки?',
			'Этот мир гнилой. Гнилые люди должны быть уничтожены, чтобы сделать лучше этот мир. Я собираюсь изменить его. Я — справедливость!',
			'Я — зло? Я — справедливость! Я тот, кто пришёл в сей мир, чтобы поддерживать справедливость и защищать слабых... я – бог! Но те, кто противятся богу... они – зло!',
			'А если кто-то умрёт на самом деле, я стану убийцей?',
			'Разве кто-то может прожить жизнь, ни разу не солгав? Люди не настолько идеальны. Все люди лгут.',
			'Ты понял, Рюзаки? В любом мире правила устанавливают Боги. Ты отказался подчиниться моим правилам. Ты попытался низвергнуть Бога нового мира. И за это тебе не будет прощения...',
			'Женщины такие безрассудные создания.',
			'В человеческом обществе лишь немногие люди заслуживают того, чтобы им полностью доверяли.',
			'Чёрт возьми, мне сейчас стольких убить хочется. По-моему, мир станет только лучше, если я избавлю его от этих скотов.',
			'Я считаю, что мир делится на тех, кто правит и тех, кто повинуется. И я считаю, что я из первых.',
			'Рюзаки, даже ради расследования дела Киры я не могу использовать чувства, влюблённой в меня девушки. Прости, но я отказываюсь! Я считаю, что играть человеческими чувствами — самое отвратительное, что может быть на свете!'
		],
		'Ryuk / Рюк':[
			'Они ищут друг друга, не зная ни имён, ни лиц. И тот, кого найдут первым, погибнет. Всё-таки в мире людей так интересно!',
			'Ты что, не будешь убивать людей? Какой ты скучный...',
			'Вот и пробил твой час, Лайт. Я же тебе говорил в самом начале нашего знакомства, что наступит день, когда я запишу твое имя в свою тетрадь. Это правила, действующие для бога смерти, который передал тетрадь в мир людей, и того человека, который первым взял её в руки. Если тебя отправят в тюрьму, то кто знает, когда ты умрешь? Если честно, мне неохота ждать. С тобой всё кончено, умри же здесь. Должен тебе признаться, я довольно неплохо провел время в твоей компании, а иногда мне даже было весело.',
			'Яблоки — для меня, это как наркотики или алкоголь для людей.',
			'Люди... Они такие странные!'
		],
		'Nia / Ниа':[
			'Если головоломка не сложилась, и тебе уже не собрать пазлы — начни сначала.',
			'Когда ведешь дело нужно двигаться вперёд, а если ошибёшься — просто извиниться.',
			'Какие глупые люди! Меня не удивляет, что некоторые люди поддерживают Киру, но это относится лишь к тем, кто желает, чтобы Кира и впредь продолжал карать злодеев. А люди, которые хотят вломиться сюда — не такие. Это толпа глупых эгоистов, которые просто хотят повеселиться.'
		]
	}
}

anime = ['Yahari Ore no Seishun Love Come wa Machigatteiru / Розовая пора моей школьной жизни — сплошной обман',
	'Neon Genesis Evangelion / Евангелион нового поколения', 'Death Note / Тетрадь смерти']

anime_lib = {
	'Yahari Ore no Seishun Love Come wa Machigatteiru / Розовая пора моей школьной жизни — сплошной обман':[
		'Hikigaya Hachiman / Хикигая Хачиман', 'Hiratsuka Shizuka / Хирацука Шизука', 'Yukinoshita Yukino / Юкиносита Юкино',
		'Yuigahama Yui / Юигахама Юи'
	],
	'Neon Genesis Evangelion / Евангелион нового поколения':[
		'Shinji Ikari / Синдзи Икари', 'Ikari Gendo / Икари Гэндо', 'Kaji Ryohji / Кадзи Рёдзи', 'None',
		'Asuka Langley Soryu / Аска Ленгли Сорью', 'Kaworu Nagisa / Каору Нагиса', 'Ayanami Rei / Аянами Рей',
		'Aida Kensuke / Аида Кенске', 'Misato Katsuragi / Мисато Кацураги', 'Ritsuko Akagi / Рицуко Акаги'
	],
	'Death Note / Тетрадь смерти':[
		'L Lawliet / Эл Лоулайт', 'Raito Yagami / Лайт Ягами', 'Ryuk / Рюк', 'Nia / Ниа'
	]
}

game_questions = [
	# OreGairu
	('Главный герой OreGairu — Хачиман Хикигая.', True),
	('Хачиман (OreGairu) вступил в клуб литературы.', False),
	('У Юи (OreGairu) розовые волосы.', True),
	('У Хачимана (OreGairu) есть старший брат.', False),
	('По словам Хачимана (OreGairu) у него есть 108 способностей.', True),
	('Первоисточником OreGairu является манга.', False),
	('Ранобе OreGairu состоит из 14 томов.', True),
	('Хирацука (OreGairu) — директор школы, в которой учатся главные герои.', False),
	('Хачиман (OreGairu) сначала подумал, что Сайка — девушка.', True),
	('В OreGairu 5 опенингов.', False),
	# Evangelion
	('Аниме Neon Genesis Evangelion вышло в 1995 году.', True),
	('В аниме Evangelion 13 ангелов, считая Адама и Лилит.', False),
	('Нагиса Каору (Evangelion) — ангел.', True),
	('Эндинг Evangelion называется "Komm, süsser Tod".', False),
	('Второй удар (Evangelion) произошёл в 2000 году.', True),
	('Целью Seele (Evangelion) является уничтожение человечества.', False),
	('Большинство ангелов (Evangelion) являются потомками Адама.', True),
	('После второго удара (Evangelion) Адам умер.', False),
	('В The End of Evangelion Икари Синдзи отвергает совершенствование.', True),
	('Seele (Evangelion) находится под руководством Nerv.', False),
	# Death Note
	('Ягами Лайт умер.', True),
	('Миса становится девушкой Эла.', False),
	('Миса совершала сделку на глаза Бога смерти несколько раз.', True),
	('При приобретении глаз Бога смерти отнимается одна третья доля оставшейся жизни.', False),
	('Владелец тетради смерти может отказаться от неё.', True),
	('Если владелец тетради смерти откажется от неё, то он умрёт.', False),
	('При продаже тетради смерти продавец и покупатель погибают.', True),
	('Первоисточником Death Note является ранобе.', False),
	('При отказе от тетради смерти у владельца теряются воспоминания связанные с ней.', True),
	('Бог смерти не может умереть.', False)
]

bot = telebot.TeleBot('1195524530:AAEiqqtCNonICXijH07775JqHF1vtn3Jnj8')

@bot.message_handler(commands=['help'])
def getHelp(message):
	bot.send_message(message.chat.id, 'Список комманд:\n\nЦитата — показывает цитату случайного персонажа из случайного аниме.\nЦитата (название аниме) — показывает цитату случайного персонажа из аниме.\nОбновления — показывает список обновлений.\nPlay, game или игра — начинает игру "правда или ложь".')

@bot.message_handler(content_types=['text'])
def getMessage(message):
	if message.text.lower() == 'цитата':
		a = choice(anime)
		c = choice(anime_lib[a])
		bot.send_message(message.chat.id, f'<i>«{choice(quotes[a][c])}»</i>\n\n<b>Аниме:</b> {a}\n<b>Персонаж:</b> {c}', parse_mode='html')
	elif len(message.text.split()) > 1 and message.text.lower().split()[0] == 'цитата':
		if fuzz.ratio(message.text.lower()[7:], 'oregairu') > 90 or fuzz.ratio(message.text.lower()[7:], 'розовая пора моей школьной жизни сплошной обман') > 50 or fuzz.ratio(message.text.lower()[7:], 'yahari ore no seishun love come wa machigatteiru') > 50:
			a = 'Yahari Ore no Seishun Love Come wa Machigatteiru / Розовая пора моей школьной жизни — сплошной обман'
			c = choice(anime_lib['Yahari Ore no Seishun Love Come wa Machigatteiru / Розовая пора моей школьной жизни — сплошной обман'])
			bot.send_message(message.chat.id, f'<i>«{choice(quotes[a][c])}»</i>\n\n<b>Персонаж:</b> {c}', parse_mode='html')
		elif fuzz.ratio(message.text.lower()[7:], 'evangelion') > 80 or fuzz.ratio(message.text.lower()[7:], 'евангелион') > 80 or fuzz.ratio(message.text.lower()[7:], 'neon genesis evangelion') > 70 or fuzz.ratio(message.text.lower()[7:], 'евангелион нового поколения') > 80:
			a = 'Neon Genesis Evangelion / Евангелион нового поколения'
			c = choice(anime_lib['Neon Genesis Evangelion / Евангелион нового поколения'])
			bot.send_message(message.chat.id, f'<i>«{choice(quotes[a][c])}»</i>\n\n<b>Персонаж:</b> {c}', parse_mode='html')
		else:
			bot.send_message(message.chat.id, 'Аниме не найдено.')

	if message.text.lower() == 'обновления':
		bot.send_message(message.chat.id, f'<b> ~ Хачиман 2.2 ~ </b>\n\n22.01.2021 — Добавлены 10 вопросов по Death Note для "Правда или ложь", также добалены цитаты.\nДобавлена команда, где есть все команды бота. /help\n\n31.12.2020 — Добавлена игра "Правда или ложь", вызвать её можно с помощью команд "play", "game" или "игра".\n — В игру добавлено 10 вопросов по OreGairu и 10 вопросов по Евангелиону.\n — Добавлено поздравление с новым годом.\n\n24.12.2020 — Добавлена возможность выводить цитату из определённого аниме.\n\n23.12.2020 — Добавлены цитаты из Evangelion.\n\n22.12.2020 — Создание версии 2.0.\n  — Добавлены команды "цитаты" и "обновления".\n  — Добавлены цитаты из OreGairu.', parse_mode='html')
	elif 'хикки' in message.text.replace('!', '').replace('.', '').replace(',', '').replace('?', '').lower().split():
		bot.send_message(message.chat.id, 'Не называй меня Хикки, сучка.')
	elif 'хикитани' in message.text.replace('!', '').replace('.', '').replace(',', '').replace('?', '').lower().split():
		u = [f'{message.from_user.first_name}, заткнись!', 'Всё равно неправильно.', 'Вообще-то Хикигая.', 'И кстати, меня никогда не звали Хикитани.']
		bot.send_message(message.chat.id, choice(u))

	if message.text.lower() == 'play' or message.text.lower() == 'game' or message.text.lower() == 'игра':
		bot.send_message(message.chat.id, choice(game_questions)[0])
	try:
		if message.reply_to_message.from_user.username == 'hachi_gachi_bot' and message.reply_to_message.text in dict(game_questions):
			if message.text.lower() in ['да', 'правда', '+', 'yes', 'true']:
				ex = True
			elif message.text.lower() in ['нет', 'ложь', '-', 'no', 'false']:
				ex = False
			if ex != None:
				try:
					if dict(game_questions)[message.reply_to_message.text] == ex:
						bot.send_message(message.chat.id, '<i>Правильный ответ!</i>', parse_mode='html')
					elif dict(game_questions)[message.reply_to_message.text] != ex:
						bot.send_message(message.chat.id, '<i>К сожалению, вы ошиблись.</i>', parse_mode='html')
				except KeyError:
					pass
	except AttributeError:
		pass

	if message.chat.id == message.from_user.id and message.from_user.username == 'ever_soup':
		bot.send_message(-1001433940163, message.text)

bot.polling(none_stop=True)

