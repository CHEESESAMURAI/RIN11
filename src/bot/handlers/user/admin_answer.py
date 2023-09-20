from aiogram import types


from bot.config.loader import bot
from usersupport.models import TelegramUser, UserDiscussion
from bot.services.db import user as user_db
from bot.services.db import user_discussion as ud_db
from bot.data import text_data as td
from bot.handlers.user import create_user_disck as reeef
from bot.keyboards import inline as ik

async def answer_from_admin(message: types.Message):

    user_id = int(message.reply_to_message.text.split("\n")[0])
    user: TelegramUser = await user_db.select_user(
        user_id=user_id
    )
    d: UserDiscussion = await ud_db.select_discussion(user=user)
    answer = message.text
    klava = await ik.reg_ref()
    history = f"{d.history}\nA:{answer}"
    await ud_db.add_history(user=user, history=history)
    await bot.send_message(
        chat_id=user_id,
        text=answer,
    )
async def promo(call: types.CallbackQuery):
    global klava

    user_id = call.data.replace("code2_", "",)
    await bot.send_message(user_id,"✅  Зачислил тебе дополнительные 200 бадди-баллов, проверь свой бонусный счет! Жду тебя на обучении, и не забудь позвать друзей  😉", reply_markup = await ik.reg_ref())
    await call.answer()

    user: TelegramUser = await user_db.select_user(
        user_id=user_id
    )

    ref_id=TelegramUser.objects.filter(user_id=user_id).first().user_ref
    print(ref_id)

    user_ref_coll = TelegramUser.objects.filter(user_id=user_id).first().ref_col

    new_ref_col = int(user_ref_coll) + 4

    TelegramUser.objects.filter(user_id=user_id).update(ref_col=new_ref_col)

    d: UserDiscussion = await ud_db.select_discussion(user=user)
    admins = await user_db.select_all_admins()
    a_list = {a.chanel_id: a.chat_id for a in admins}
    mes_id = d.mes_id
    for admin in a_list:
        await bot.send_message(
            chat_id=a_list[admin],
            text=td.SUCCESS_MESSAGE_CARD,
            reply_to_message_id=mes_id,

        )

async def plus(call: types.CallbackQuery):
    global klava

    user_id = call.data.replace("plus_", "",)
    await bot.send_message(user_id,"+50 баллов", reply_markup = await ik.reg_ref())
    await call.answer()

    user: TelegramUser = await user_db.select_user(
        user_id=user_id
    )

    ref_id=TelegramUser.objects.filter(user_id=user_id).first().user_ref
    print(ref_id)


    user_ref_coll = TelegramUser.objects.filter(user_id=user_id).first().ref_col

    new_ref_col = int(user_ref_coll) + 1

    TelegramUser.objects.filter(user_id=user_id).update(ref_col=new_ref_col)

    d: UserDiscussion = await ud_db.select_discussion(user=user)
    admins = await user_db.select_all_admins()
    a_list = {a.chanel_id: a.chat_id for a in admins}
    mes_id = d.mes_id
    for admin in a_list:
        await bot.send_message(
            chat_id=a_list[admin],
            text=td.SUCCESS_MESSAGE_CARD,
            reply_to_message_id=mes_id,

        )


async def send_code(call: types.CallbackQuery):
    global klava

    user_id = call.data.replace("code_", "",)
    await bot.send_message(user_id,"ПОЗДРАВЛЯЮ 🎉🎉🎉\n\nТы успешно сдал тест и прошел регистрацию!\n\nПервый шаг на пути к профессии мечты сделан, теперь ты ученик Иннополиса!\n\n❤ Теперь на твоём бонусном счёте появились стартовые 200 баллов! Подпишись на нас в соцсетях и получи +100 баллов, и ты уже сможешь обменять их на сертификат! А за каждого приглашенного друга ты получишь +100 баллов. 🎁", reply_markup = await ik.reg_ref())
    await call.answer()

    user: TelegramUser = await user_db.select_user(
        user_id=user_id
    )

    ref_id=TelegramUser.objects.filter(user_id=user_id).first().user_ref
    print(ref_id)
    user_ref_coll = TelegramUser.objects.filter(user_id=ref_id).first().ref_col

    new_ref_col = int(user_ref_coll) + 2

    TelegramUser.objects.filter(user_id=ref_id).update(ref_col=new_ref_col)

    user_ref_coll = TelegramUser.objects.filter(user_id=user_id).first().ref_col

    new_ref_col = int(user_ref_coll) + 4

    TelegramUser.objects.filter(user_id=user_id).update(ref_col=new_ref_col)
    #print(reeef.reef)
    #print(reeef.reef.title)
    #print(str(reeef.reef))

    #reeef.reef()
    
    d: UserDiscussion = await ud_db.select_discussion(user=user)
    admins = await user_db.select_all_admins()
    a_list = {a.chanel_id: a.chat_id for a in admins}
    mes_id = eval(d.mes_id)
    for admin in a_list:
        await bot.send_message(
            chat_id=a_list[admin],
            text=td.SUCCESS_MESSAGE_CARD,
            reply_to_message_id=mes_id[a_list[admin]],

        )


async def access_denied(call: types.CallbackQuery):
    user_id = call.data.replace("denied_", "")
    await send_mes(user_id, td.TEXT_ANSWER_1)
    await call.answer()

    user: TelegramUser = await user_db.select_user(
        user_id=user_id
    )
    d: UserDiscussion = await ud_db.select_discussion(user=user)
    admins = await user_db.select_all_admins()
    a_list = {a.chanel_id: a.chat_id for a in admins}
    mes_id = eval(d.mes_id)
    for admin in a_list:
        await bot.send_message(
            chat_id=a_list[admin],
            text=td.SUCCESS_MESSAGE_CANCEL,
            reply_to_message_id=mes_id[a_list[admin]]
        )
async def access_denied2(call: types.CallbackQuery):
    user_id = call.data.replace("denied_", "")
    await send_mes(user_id, td.TEXT_ANSWER_4)
    await call.answer()

    user: TelegramUser = await user_db.select_user(
        user_id=user_id
    )
    d: UserDiscussion = await ud_db.select_discussion(user=user)
    admins = await user_db.select_all_admins()
    a_list = {a.chanel_id: a.chat_id for a in admins}
    mes_id = eval(d.mes_id)
    for admin in a_list:
        await bot.send_message(
            chat_id=a_list[admin],
            text=td.SUCCESS_MESSAGE_CANCEL2,
            reply_to_message_id=mes_id[a_list[admin]]
        )

async def send_mes(user_id, text):
    user: TelegramUser = await user_db.select_user(
        user_id=user_id
    )
    d: UserDiscussion = await ud_db.select_discussion(user=user)
    history = f"{d.history}\nA:{text}"
    await ud_db.add_history(user=user, history=history)
    await bot.send_message(
        chat_id=user_id,
        text=text
    )
