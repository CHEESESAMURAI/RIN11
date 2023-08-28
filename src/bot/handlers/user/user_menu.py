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

    for user in invited_friend:
        ref=t.TelegramUser.objects.filter(user_id=call.message.chat.id).first().ref_col
        if int(user.ref_col)== 0:
            a = a + user.name + " ❌  \n"
        else:
            a = a + user.name + " ✅ \n"
    if action == "6":
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            text= f"Привет! Приглашаю тебя на бесплатный онлайн-интенсив по 🤖 программированию в Иннополис.\n\nЭтим летом у школьников 8-11 классов благодаря проекту «Код будущего» появилась крутая возможность бесплатно научиться программировать на Python. Ты создашь собственную 2D-игру или Telegram-бот 🔥\n\nЧтобы занять место в проекте, переходи по ссылке и регистрируйся 👉: https://t.me/pythonbuddy_bot?start={call.message.chat.id} \n\n⚠ Пришли Бадди боту скрин с сайта Госуслуг с подтверждением успешной регистрации, и получить свои приветсвенные 50 баллов!\n\n✌ До встречи на летнем онлайн-интенсиве!",
            message_id=call.message.message_id,
            reply_markup=await ik.back()
    )
    elif action == "2":
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            text= f"🪙 РЕФЕРАЛЬНАЯ ПРОГРАММА. ЧТО ЭТО И ЗАЧЕМ?\n\nЭто классная возможность набрать бонусные баллы и обменять их на ценные подарки 🎁\n\nЧтобы участвовать, нужно рассказать другу или однокласснику о бесплатном обучении программированию в Иннополис и прислать ему письмо-приглашение со своей реферальной ссылкой 📨\n\nДруг зарегистрируется по ней и станет участником нашего проекта!\n\nА ты получишь за приглашение одного друга 50 баллов.\n\nБаллы зачисляются на твой бонусный счет после того, как друг пришлет скриншот с успешной регистрацией на Госуслугах.\n\n‼ Внимание! Человек, которому ты отправляешь приглашение, должен учиться в 8-11 классе и быть гражданином РФ.\n\n⚠ А за свою регистрацию ты тоже получаешь стартовые 50 баллов.\n\nКак и на что обменять накопленные бонусы?\n\n✌ 1 БАДДИ балл = 1 рубль\n\n✌ Баллы обмениваются на сертификаты для покупок в OZON, Золотое яблоко.\n\n✌ Номиналы сертификатов: от 300 руб. и до 300 000 руб.\n\nА обменять свои баллы ты сможешь с 15.06.2023 до 30.06.2023.\n\nСгенерируй готовое письмо-приглашение с реферальной ссылкой, просто нажав на кнопку ⤵\n\nСкопируй его и отправь друзьям!",
            message_id=call.message.message_id,
            reply_markup=await ik.reg_ref()
    )
    elif action == "3":
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            text= f"ВОТ ЭТО ДИЛЕММА ‼\n\nПрежде чем зарегистрироваться, надо выбрать курс.\n\n💬 Что тебе интересно? Что сейчас востребовано?\n\n🤖 Telegram-боты или игры?\n\nЗнакомься с кратким описанием двух программ летнего интенсива и выбери, что тебе нравится!\n\nСмелее! ⤵\n\nТы в любом случае в выигрыше 🎉",
            message_id=call.message.message_id,
            reply_markup=await ik.course()

    )
    elif action == "9":
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            text= f"🎁 ОБМЕНЯЙ БАДДИ БАЛЛЫ НА ПОДАРКИ\n\nОстаток бонусного счета:{ref_bal} баллов.\n\nКоличество приглашенных друзей: {ref}\n\n 💰Для обмена Бадди баллов на сертификат, тебе необходимо выбрать площадку и номинал сертификата.\n\nНапример: Ozon 500\n\nДоступные номиналы сертификатов для обмена: \n\n1️олотое яблоко 300 - 500 - 1500 - 2000 - 3000\n\n2️зон - 500 - 700 - 1000 - 1500 - 2000- 3000\n\nОбменять баллы на сертификаты можно с 15.06.2023  до 30.06.2023\n\n⚠ Нажми на кнопку под сообщением ⤵",
            message_id=call.message.message_id,
            reply_markup=await ik.trade()

    )
    elif action == "10":
        await bot.edit_message_text(
                chat_id=call.message.chat.id,
            text= f"МОИ ДРУЗЬЯ\n\n ❌  - твой друг еще не подтвердил свою заявку на госуслугах\n\n ✅  - заявка твоего друга подтверждена\n\nСписок друзей : \n\n"+a,
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
            text= f"1 курс\n\nTELEGRAM-БОТЫ НА PYTHON\n\n🐍 Python — универсальный язык программирования, на котором работают известные IT-компании: Google, Youtube, Netflix, Facebook, Pinterest, Pixar и др.\n\nЕго часто используют для создания ботов в Telegram.\n\nПо итогу курса научишься:\n\n▪ регистрировать боты в Telegram;\n\n▪ пользоваться технологиями работы с API Telegram;\n\n▪ реализовывать базовые алгоритмы;\n\n ▪использовать современные библиотеки и работать с ними;\n\n▪ осуществлять обработку сообщений в чат-боте.\n\nС помощью Python создашь своего 👾 Telegram-бота с полным функционалом.",
            message_id=call.message.message_id,
            reply_markup=await ik.fio()
    )
         elif action == "5":
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            text= f"2 курс\n\nРАЗРАБОТКА 2D-ИГР НА PYTHON\n\nCоздание игр — это увлекательное и полезное занятие, оно тренирует последовательное обдумывание действий.\n\nЧему научишься на курсе:\n\n▪ владеть базовыми конструкциями Python;\n\n▪ разбираться в особенностях библиотек Arcade и PyGame;\n\n▪ работать с анимацией в библиотеках Arcade и PyGame;\n\n▪ применять звуки, свет, создавать меню и дополнительные окна.\n\n🤖 По итогу обучения ты сделаешь 2D-игру с анимированным персонажем и реализацией пользовательского интерфейса.",
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
    elif action == "12":
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            text= f"Отправь свой номер телефона и нажми кнопку внизу, чтобы продолжить регистрацию⤵ ",
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
            text= f"⚠ Пришли Бадди боту скрин с сайта Госуслуг с подтверждением успешной регистрации, и получить свои приветсвенные 50 баллов!\n\n✌ До встречи на летнем онлайн-интенсиве!",
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
            text= f"📋 ИНСТРУКЦИЯ ДЛЯ РЕГИСТРАЦИИ ЗАЯВКИ НА БЕСПЛАТНОЕ ОБУЧЕНИЕ\n\n1️ебе необходимо подать заявление на Госуслугах : https://www.gosuslugi.ru/futurecode?organization=44&view=online\n\nДля подачи заявления тебе понадобится справка из школы, которая подтверждает, что ты учишься в 8–11 классе. \n\n▪ Можешь это сделать сам, если тебе исполнилось 14 лет, и у тебя есть личный кабинет на Госуслугах с подтвержденной учетной записью.\n\n▪ В ином случае — попроси помочь своего родителя или опекуна. \n\n⚠ Внимание! При заполнении анкеты на Госуслугах нужно ввести СВОЮ электронную почту. Это требуется для создания личного кабинета на платформе, где будет проходить обучение. \n\n2️⃣  течение 5 дней после подачи заявления на Госуслугах тебе на почту придёт письмо со ссылкой на входное тестирование, логином и паролем Leader-ID.\n\n▪ Тест состоит из 2-х блоков, пройти нужно оба. На выполнение теста дается 7 дней.\n\n▪ В течение 2 дней после его прохождения ты получишь письмо с результатами. \n\n3️⃣ ледующий шаг после успешного тестирования — подписание договора с образовательной организацией в личном кабинете на обучающей платформе Университета Иннополис.\n\n✌ Всего 4 простых шага — и ты уже осваиваешь Python в одном из самых молодых и инновационных IT-вузов России.\n\nПритом абсолютно бесплатно!\nКогда ещё будет такой шанс!\n\nУспей зарегистрироваться и выбрать курс!\n\n⚠ Для получения 50 стартовых БАДДИ баллов пришли мне скрин успешной регистрации на сайте Госуслуг.\n\nУчаствуй в программе «Приведи друга», собирай бонусы, чтобы потом обменять их на подарки!\n\n🤖 Если возникнут вопросы — сразу пиши Бадди.",
            message_id=call.message.message_id,
            reply_markup=await ik.final()
    )
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
