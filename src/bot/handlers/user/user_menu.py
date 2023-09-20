from aiogram import types

from bot.config.loader import bot
from bot.data import dict_data as dd
from bot.keyboards import inline as ik
from bot.data import text_data as td
from bot.handlers.user import admin_answer as ho
from bot.handlers.user import create_user_disck as t

async def edit_menu(call: types.CallbackQuery):
    global c
    action = call.data.replace("act_", "")

    ref=t.TelegramUser.objects.filter(user_id=call.message.chat.id).first().ref_col
    ref_bal=int(ref) * 50






    invited_friend =t.TelegramUser.objects.filter(user_ref=call.message.chat.id).all()
    a = ""
    c = 0
    g = 0
    f = 0
    for user in invited_friend:
        ref=t.TelegramUser.objects.filter(user_id=call.message.chat.id).first().ref_col
        if int(user.ref_col)== 0:
            a = a + user.name + " ❌  \n"
            g+=1
        else:
            a = a + user.name + " ✅ \n"
            c+=1
        f=c+g
    if action == "6":
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            text= f"Привет! Приглашаю тебя на бесплатный онлайн-курс по программированию в Иннополис.\n\nУ школьников 8-11 классов и студентов колледжей появилась крутая возможность бесплатно научиться программировать на Python благодаря проекту «Код будущего». Ты создашь собственную 2D-игру или Telegram-бот 🔥\n\nЧтобы занять место в проекте, переходи по ссылке и регистрируйся 👉https://t.me/pythonbuddy_bot?start={call.message.chat.id} \n\n✌ До встречи на обучении!",
            message_id=call.message.message_id,
            reply_markup=await ik.back()
    )
    elif action == "2":
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            text= f"РЕФЕРАЛЬНАЯ ПРОГРАММА - Это классная возможность набрать бонусные баллы и обменять их на ценные подарки 🎁\n\nЧтобы участвовать, нужно рассказать другу или однокласснику о бесплатном обучении программированию в университете Иннополис и прислать ему письмо-приглашение со своей реферальной ссылкой. 📨\n\nКак получить подарки от Бадди Бота?\n\nРегистрируйся в проекте и получи приветственные 200 бадди-баллов.\n\nПодпишись на наши социальные сети ВК и Telegram и получай по 50 баллов за каждую подписку. \n\nПриводи друзей и получай неограниченное количество баллов! За каждого друга, который зарегистрировался по твоей ссылке ты получаешь по 100 баллов.\n\n💲 Давай посчитаем: зарегистрировавшись на курс и подписавшись на наши крутые соцсети ты получаешь 300 бадди баллов, которые ты уже можешь потратить!\n\nКак и на что обменять накопленные бонусы?\n\n✌ 1 БАДДИ балл = 1 рубль\n\n✌ Баллы обмениваются на сертификаты для покупок в OZON, СберМегаМаркет, Золотое яблоко, Спортмастер, Lamoda, Skyeng.\n\n✌ Номиналы сертификатов: от 300 руб. и до 3000 руб. Количество сертификатов неограниченно!\n\nПриводи сто друзей - получай 10 000 баллов 😉\n\nА потратить свои баллы ты сможешь с 20.10.2023 до 20.12.2023.\n\nВажно: Баллы зачисляются на твой бонусный счет после того, как твой друг успешно пройдет регистрацию по твоей ссылке.\n\nЧеловек, которому ты отправляешь приглашение, должен учиться в 8-11 классе или быть студентом СПО (коллежда, техникума), а такжееи быть гражданином РФ.\n\nСгенерируй готовое письмо-приглашение с реферальной ссылкой, просто нажав на кнопку ниже и перешли друзьям ⤵ ",
            message_id=call.message.message_id,
            reply_markup=await ik.reg_ref()
    )
    elif action == "411":
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            text= f"Зарегистрироваться на курс не сложно, но на всякий случай лучше прочитать инструкцию - так у тебя точно не возникнет проблем 💫\n\nВся информация в PDF файле ниже 👇",
            message_id=call.message.message_id,
            reply_markup=await ik.back()

    )
    elif action == "3":
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            text= f"ВОТ ЭТО ДИЛЕММА ‼\n\nПрежде чем зарегистрироваться, надо выбрать курс.\n\n💬 Что тебе интересно? Что сейчас востребовано?\n\n🤖 Telegram-боты или игры, искусственный интеллект или графические интерфейсы?\n\nЗнакомься с кратким описанием каждой программы и выбери, что тебе нравится!\n\nСмелее! ⤵\n\nТы в любом случае в выигрыше 🎉",
            message_id=call.message.message_id,
            reply_markup=await ik.course()

    )
    elif action == "9":
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            text= f"🎁 ОБМЕНЯЙ БАДДИ БАЛЛЫ НА ПОДАРКИ\n\nОстаток бонусного счета: {ref_bal} баллов.\n\nКоличество зарегестрированных друзей: {c} из {f} \n\n 💰Для обмена Бадди баллов на сертификат, тебе необходимо выбрать площадку и номинал сертификата.\n\nНапример: Ozon 500\n\nНоминалы сертификатов:\n\n🔹 Золотое яблоко\n\n300 руб., 500 руб., 1500 руб., 2000 руб., 3000 руб.\n\n🔹 OZON\n\n500 руб., 700 руб., 1000 руб., 1500 руб., 2000 руб., 3000 руб.\n\n🔹 Спортмастер\n\n500 руб., 1000 руб., 2000 руб., 3000 руб\n\n🔹 СберМегаМаркет \n\n500 руб., 1500 руб., 3000 руб.\n\n🔹 Lamoda\n\n1000 руб., 1500 руб., 2000 руб., 2200 руб., 3000 руб.\n\n🔹 Skyeng\n\n1000 руб., 2000 руб., 3000 руб\n\n‼ Обменять баллы на сертификаты можно с 20.10.2023 до 20.12.2023.\n\n⚠ Нажми на кнопку под сообщением ⤵",
            message_id=call.message.message_id,
            reply_markup=await ik.trade()

    )
        c = 0
        f = 0
        g = 0
    elif action == "10":
        await bot.edit_message_text(
                chat_id=call.message.chat.id,
            text= f"МОИ ДРУЗЬЯ\n\n❌  - твой друг еще не подтвердил свою заявку на госуслугах, напомни ему об этом!\n\n✅  - заявка твоего друга подтверждена и ты получишь за него 100 бадди-баллов\n\nПриводи сто друзей, получай 10.000 баллов - у нас нет ограничений 😉\n\nСписок друзей : \n\n"+a,
            message_id=call.message.message_id,
            reply_markup=await ik.back()

    )
    elif action == "11":
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            text=f"Твоя заявка на обмен принята! Ожидай свой сертификат😎",
            message_id=call.message.message_id,
            reply_markup=await ik.back()
    )
    elif action == "4":
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            text= f"🎓TELEGRAM-БОТЫ НА PYTHON\n\n🐍 Python — универсальный язык программирования, на котором работают известные IT-компании: Google, Youtube, Netflix, Facebook, Pinterest, Pixar и др.\n\nЕго часто используют для создания ботов в Telegram.\n\nПо итогу курса научишься:\n\n▪ регистрировать боты в Telegram;\n\n▪ пользоваться технологиями работы с API Telegram;\n\n▪ реализовывать базовые алгоритмы;\n\n▪ осуществлять обработку сообщений в чат-боте.\n\nС помощью Python создашь своего 👾 Telegram-бота с полным функционалом.",
            message_id=call.message.message_id,
            reply_markup=await ik.fio()
    )
    elif action == "5":
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            text= f"🎓РАЗРАБОТКА 2D-ИГР НА PYTHON\n\nСоздание игр — это увлекательное и полезное занятие, оно тренирует последовательное обдумывание действий.\n\nЧему научишься на курсе:\n\n▪ владеть базовыми конструкциями Python;\n\n▪ разбираться в особенностях библиотек Arcade и PyGame;\n\n▪ работать с анимацией в библиотеках Arcade и PyGame;\n\n▪ применять звуки, свет, создавать меню и дополнительные окна.\n\n🤖 По итогу обучения ты сделаешь 2D-игру с анимированным персонажем и реализацией пользовательского интерфейса.",
            message_id=call.message.message_id,
            reply_markup=await ik.fio()
    )
    elif action == "51":
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            text= f"🎓 ПРИРУЧИ ИСКУССТВЕННЫЙ ИНТЕЛЛЕКТ: ОТ ТЕОРИИ К ПРАКТИКЕ\n\nТехнология искусственного интеллекта используется во многих сферах - от маркетинга до медицины. Повышенный спрос на проекты в области ИИ указывает на высокую востребованность специалистов. \n\nЧему научишься на курсе:\n\n▪  основам программирования\n\n▪  применять типы данных и операторов Python\n\n▪  владеть технологиями Pandas, Numpy, Tensorflow, Scikit-learn\n\n▪ основам машинного обучения и нейросетей.",
            message_id=call.message.message_id,
            reply_markup=await ik.fio()
    )
    elif action == "52":
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            text= f"🎓СОЗДАНИЕ ПАРСЕРОВ НА PYTHON\n\nПарсинг позволяет автоматически обрабатывать и анализировать данные по определенным параметрам, получать необходимую информацию с сайтов без ручного ввода данных, собирать и структурировать данные для последующего использования. Это помогает ускорить трудоемкую и рутинную работу. \n\n🤖 По итогу обучения ты изучишь Python и различные библиотеки, чтобы разрабатывать программы для парсеров",
            message_id=call.message.message_id,
            reply_markup=await ik.fio()
    )
    elif action == "53":
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            text= f"🎓РАЗРАБОТКА ГРАФИЧЕСКИХ ИНТЕРФЕЙСОВ НА PYTHON\n\nГрафические интерфейсы отвечают за взаимодействие программ между пользователем и машинным кодом. Главная задача специалистов сделать интерфейс  интуитивно понятным и удобным. \n\n🤖 По итогу обучения ты изучишь Python и библиотеку PyQt, освоишь навыки junior-разработчика. ",
            message_id=call.message.message_id,
            reply_markup=await ik.fio()
    )
    elif action == "54":
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            text= f"🎓ЭТИЧНЫЙ ХАКИНГ НА PYTHON\n\nСпециалисты в области информационной безопасности занимаются обнаружением и предотвращением вредоносных программ, программ-шпионов и других видов атак. Популярной становится профессия пентестера - они специализируются на поиске уязвимостей. Python нашел широкое применение в сфере кибербезопасности.\n\n🤖 По итогу обучения ты углубленно изучишь Python  напишешь веб-приложение на Django/Flask и отчет о его безопасности",
            message_id=call.message.message_id,
            reply_markup=await ik.fio()
    )
    elif action == "7":
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            text= f"Отправь свое ФИО и нажми кнопку внизу, чтобы продолжить регистрацию⤵",
            message_id=call.message.message_id,
            reply_markup=await ik.take_fio()
    )
    elif action == "91":
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            text= f"📋 Условия обмена баллов\n\n✌1 балл=1 рубль\n\nНоминалы сертификатов:\n\n🔹 Золотое яблоко\n300 руб., 500 руб., 1500 руб., 2000 руб., 3000 руб.\n\n🔹 OZON\n500 руб., 700 руб., 1000 руб., 1500 руб., 2000 руб., 3000 руб.\n\n🔹 Спортмастер\n500 руб., 1000 руб., 2000 руб., 3000 руб\n\n🔹 СберМегаМаркет \n500 руб., 1500 руб., 3000 руб.\n\n🔹 Lamoda\n1000 руб., 1500 руб., 2000 руб., 2200 руб., 3000 руб.\n\n🔹 Skyeng\n1000 руб., 2000 руб., 3000 руб.\n\n‼ Обменять баллы на сертификаты можно с 20.09.2023 до 20.12.2023.\n\nНачисление баллов будет происходить после подсчета всех зарегистрировавшихся на курс с 20.10.2023 по 20.12.2023. Обязательно дождись результатов!",
            message_id=call.message.message_id,
            reply_markup=await ik.back()
    )
    elif action == "12":
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            text= f"Отправь свой номер заявления с гос.услуг и нажми кнопку внизу, чтобы продолжить регистрацию⤵ ⚠ \n\nВажно: заявление должно пройти регистрацию. Мы прикрепили скриншот для примера.\n\nДо встречи на обучении!!",
            message_id=call.message.message_id,
            reply_markup=await ik.take_num()
    )
    elif action == "13":
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            text= f"Отправь свою электронную почту и нажми кнопку внизу, чтобы получить подробную инструкцию для регистрации на обучение ⤵",
            message_id=call.message.message_id,
            reply_markup=await ik.instruction()
    )
    elif action == "14":
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            text= f"Пришли Бадди Боту скрин с сайта Госуслуг с подтверждением успешной регистрации, и получи свои приветственные 200 баллов!\n\n⚠ Важно: проверь, чтобы на скриншоте была верная дата. Для удобства мы прикрепили пример верного скриншота. \n\nДо встречи на обучении!!",
            message_id=call.message.message_id,
            reply_markup=await ik.back()
    )
    elif action == "15":
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            text= f"Подписывайся на наши социальные сети, чтобы быть в курсе актуальных новостей.\n\nВК https://vk.com/inno_code\n\nTelegram https://t.me/inno_code",
            message_id=call.message.message_id,
            reply_markup=await ik.back()
    )
    elif action == "8":
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            text= f"📋 ИНСТРУКЦИЯ ДЛЯ РЕГИСТРАЦИИ\n\nЗарегистрироваться на курс несложно, мы расписали супер удобную инструкцию с примерами в PDF файле ниже \n\nЕсли говорить кратко - есть 3 простых шага. \n\n1️ебе необходимо подать заявление на Госуслугах : https://www.gosuslugi.ru/futurecode?organization=44&view=online\n\nДля подачи заявления тебе понадобится справка из школы или твоего учебного заведения.\n\n⚠ При заполнении анкеты на Госуслугах нужно ввести СВОЮ электронную почту. Это требуется для создания личного кабинета на платформе, где будет проходить обучение. \n\n2️⃣В течение 5 дней после подачи заявления на Госуслугах тебе на почту придёт письмо со ссылкой на входное тестирование, логином и паролем Leader-ID.\n\n▪ Тест состоит из 2-х блоков, пройти нужно оба. На выполнение теста дается 7 дней.\n\n▪ В течение 2 дней после его прохождения ты получишь письмо с результатами.\n\n3️⃣ осле успешного тестирования нужно подписать договор с образовательной организацией в личном кабинете на обучающей платформе Университета Иннополис.\n\n✌ Всего 3 простых шага — и ты уже осваиваешь Python в одном из самых молодых и инновационных IT-вузов России.\n\n⚠ Для получения 200 стартовых БАДДИ баллов пришли мне скрин успешной регистрации на сайте Госуслуг.\n\n🤖 Если возникнут вопросы — сразу пиши Бадди.",
            message_id=call.message.message_id,
            reply_markup=await ik.final()
    )
        user_id = call.data.replace("code_", "")
        doc =(open(r'/home/cheese/RIN1/fa/Инструкция Онлайн полная (1).pdf', 'rb'))
        await bot.send_document(call.message.chat.id,doc)
    else:
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            text=dd.btn_text[action],
            message_id=call.message.message_id,
            reply_markup=await ik.back()
        )
        c=0
        b=0
async def back(call: types.CallbackQuery):
    await bot.edit_message_text(
        chat_id=call.message.chat.id,
        text=td.MAIN_TEXT,
        message_id=call.message.message_id,
        reply_markup=await ik.get_user_menu()
    )
