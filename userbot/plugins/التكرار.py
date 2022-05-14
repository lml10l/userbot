import asyncio
import base64

from telethon.tl import functions, types
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name

from userbot import jmthon

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.tools import media_type
from ..helpers.utils import _catutils
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "extra"


async def spam_function(event, RR7PP, cat, sleeptimem, sleeptimet, DelaySpam=False):
  
    counter = int(cat[0])
    if len(cat) == 2:
        spam_message = str(cat[1])
        for _ in range(counter):
            if event.reply_to_msg_id:
                await RR7PP.reply(spam_message)
            else:
                await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and RR7PP.media:
        for _ in range(counter):
            RR7PP = await event.client.send_file(
                event.chat_id, RR7PP, caption=RR7PP.text
            )
            await _catutils.unsavegif(event, RR7PP)
            await asyncio.sleep(sleeptimem)
        if BOTLOG:
            if DelaySpam is not True:
                if event.is_private:
                    await event.client.send_message(
                        BOTLOG_CHATID,
                        "**⌯︙التڪـرار  **\n"
                        + f"**⌯︙تم تنفيذ التكرار بنجاح في ** [المستخـدم](tg://user?id={event.chat_id}) **الدردشـة مـع** {counter} **عدد المرات مع الرسالة أدناه**",
                    )
                else:
                    await event.client.send_message(
                        BOTLOG_CHATID,
                        "**⌯︙التڪـرار  **\n"
                        + f"**⌯︙تم تنفيذ التكرار بنجاح في ** {get_display_name(await event.get_chat())}(`{event.chat_id}`) **مـع** {counter} **عدد المرات مع الرسالة أدناه**",
                    )
            elif event.is_private:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    "**⌯︙التكرار الوقتي **\n"
                    + f"**⌯︙تم تنفيذ التكرار الوقتي  بنجاح في ** [المستخـدم](tg://user?id={event.chat_id}) **الدردشـة مـع** {counter} **عدد المرات مع الرسالة أدناه مع التأخير** {sleeptimet} ** الثوانـي **",
                )
            else:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    "**⌯︙التكرار الوقتي **\n"
                    + f"**⌯︙تم تنفيذ التكرار الوقتي  بنجاح في ** {get_display_name(await event.get_chat())}(`{event.chat_id}`) **مـع** {counter} **عدد المرات مع الرسالة أدناه مع التأخير** {sleeptimet} ** الثوانـي **",
                )

            RR7PP = await event.client.send_file(BOTLOG_CHATID, RR7PP)
            await _catutils.unsavegif(event, RR7PP)
        return
    elif event.reply_to_msg_id and RR7PP.text:
        spam_message = RR7PP.text
        for _ in range(counter):
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    else:
        return
    if DelaySpam is not True:
        if BOTLOG:
            if event.is_private:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    "**⌯︙التڪـرار  **\n"
                    + f"**⌯︙تم تنفيذ التكرار بنجاح في ** [المستخـدم](tg://user?id={event.chat_id}) **الدردشـة مـع** {counter} **رسائـل الـ   :** \n"
                    + f"⌯︙`{spam_message}`",
                )
            else:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    "**⌯︙التڪـرار  **\n"
                    + f"**⌯︙تم تنفيذ التكرار بنجاح في ** {get_display_name(await event.get_chat())}(`{event.chat_id}`) **الدردشـة مـع** {counter} **رسائـل الـ   :** \n"
                    + f"⌯︙`{spam_message}`",
                )
    elif BOTLOG:
        if event.is_private:
            await event.client.send_message(
                BOTLOG_CHATID,
                "**⌯︙التكرار الوقتي **\n"
                + f"**⌯︙تم تنفيذ التكرار الوقتي  بنجاح في ** [المستخـدم](tg://user?id={event.chat_id}) **الدردشـة مـع** {sleeptimet} seconds and with {counter} **رسائـل الـ   :** \n"
                + f"⌯︙`{spam_message}`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                "**⌯︙التكرار الوقتي **\n"
                + f"**⌯︙تم تنفيذ التكرار الوقتي  بنجاح في ** {get_display_name(await event.get_chat())}(`{event.chat_id}`) **الدردشـة مـع** {sleeptimet} **الثوانـي و مـع** {counter} **رسائـل الـ  ️ :** \n"
                + f"⌯︙`{spam_message}`",
            )


@jmthon.ar_cmd(
    pattern="كرر (.*)",
    command=("كرر", plugin_category),
    info={
        "header": "⌯︙ملـئ النـص في الدردشـة مع عدد معيّن من المـرات ",
        "description": "⌯︙إرسـال الوسائط/الرسائل التي تم الردّ عليها <عدد> مرّة في الدردشـة ",
        "usage": ["{tr}<كرر <عدد> <الكلمه", "{tr}كرر الكلمه <عدد> الـرّد علـىٰ رسـالة "],
        "examples": "{tr}كرر 10 الكلمه",
    },
)
async def spammer(event):
    "⌯︙ملـئ النـص في الدردشـة "
    RR7PP = await event.get_reply_message()
    cat = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    try:
        counter = int(cat[0])
    except Exception:
        return await edit_delete(
            event, "⌯︙يـجي استـخدام كتـابة صحـيحة الرجاء الـتاكد من الامر اولا ⚠️"
        )
    if counter > 50:
        sleeptimet = 0.5
        sleeptimem = 1
    else:
        sleeptimet = 0.1
        sleeptimem = 0.3
    await event.delete()
    await spam_function(event, RR7PP, cat, sleeptimem, sleeptimet)


@jmthon.ar_cmd(
    pattern="تكرار الملصق$",
    command=("تكرار الملصق", plugin_category),
    info={
        "header": "⌯︙للتكرار الدردشـة بالملصقـات  💢.",
        "description": "⌯︙للدردشة العشوائية مع جميع الملصقات في حزمة ملصقات الرسائل التي تم الرد عليها 💢.",
        "usage": "{tr}تكرار الملصق",
    },
)
async def stickerpack_spam(event):
    "للتكرار الدردشـة بالملصقـات."
    reply = await event.get_reply_message()
    if not reply or media_type(reply) is None or media_type(reply) != "Sticker":
        return await edit_delete(
            event, "**⌯︙قم بالـردّ على أيّ ملصق لإرسـال جميع ملصقات الحزمة  **"
        )
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    try:
        stickerset_attr = reply.document.attributes[1]
        catevent = await edit_or_reply(
            event, "**⌯︙جاري إحضار تفاصيل حزمة الملصقات، يرجى الإنتظار قليلا  ⏱**"
        )
    except BaseException:
        await edit_delete(event, "⌯︙أعتقد أنّ هذا الملصق ليس جزءًا من أيّ حزمة لذا لا أستطيع إيجاد حزمته ⚠️", 5)
        return
    try:
        get_stickerset = await event.client(
            GetStickerSetRequest(
                types.InputStickerSetID(
                    id=stickerset_attr.stickerset.id,
                    access_hash=stickerset_attr.stickerset.access_hash,
                )
            )
        )
    except Exception:
        return await edit_delete(
            catevent,
            "⌯︙أعتقد أنّ هذا الملصق ليس جزءًا من أيّ حزمة لذا لا أستطيع إيجاد حزمته ⚠️",
        )
    try:
        hmm = Get(hmm)
        await event.client(hmm)
    except BaseException:
        pass
    reqd_sticker_set = await event.client(
        functions.messages.GetStickerSetRequest(
            stickerset=types.InputStickerSetShortName(
                short_name=f"{get_stickerset.set.short_name}"
            )
        )
    )
    for m in reqd_sticker_set.documents:
        await event.client.send_file(event.chat_id, m)
        await asyncio.sleep(0.7)
    if BOTLOG:
        if event.is_private:
            await event.client.send_message(
                BOTLOG_CHATID,
                "**⌯︙تكرار الملصق :**\n"
                + f"**⌯︙تم تنفيذ الإزعـاج بواسطة حزمة الملصقات في   :** [المستخـدم](tg://user?id={event.chat_id}) **الدردشـة مع الحزمـة **",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                "**⌯︙تكرار الملصق :**\n"
                + f"**⌯︙تم تنفيذ الإزعـاج بواسطة حزمة الملصقات في   :** {get_display_name(await event.get_chat())}(`{event.chat_id}`) **الدردشـة مع الحزمـة **",
            )
        await event.client.send_file(BOTLOG_CHATID, reqd_sticker_set.documents[0])


@jmthon.ar_cmd(
    pattern="سبام (.*)",
    command=("سبام", plugin_category),
    info={
        "header": "⌯︙ڪتابة النّص حرف بعد حرف 📝",
        "description": "⌯︙لإزعـاج الدردشـة بجميع الأحرف في النّص المعطى ڪرسـالة جديدة 💢",
        "usage": "{tr}تكرار بالحرف <text>",
        "examples": "{tr}تكرار بالحرف جيـبثون ",
    },
)
async def tmeme(event):
    "⌯︙ڪتابة النّص حرف بعد حرف 📝."
    cspam = str("".join(event.text.split(maxsplit=1)[1:]))
    message = cspam.replace(" ", "")
    await event.delete()
    for letter in message:
        await event.respond(letter)
    if BOTLOG:
        if event.is_private:
            await event.client.send_message(
                BOTLOG_CHATID,
                "**⌯︙تكرار بالحرف 📝 :**\n"
                + f"**⌯︙تم تنفيذ الإزعـاج بواسطة الأحرف في   ▷  :** [User](tg://user?id={event.chat_id}) **الدردشـة مـع** : `{message}`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                "**⌯︙تكرار بالحرف 📝 :**\n"
                + f"**⌯︙تم تنفيذ الإزعـاج بواسطة الأحرف في   ▷  :** {get_display_name(await event.get_chat())}(`{event.chat_id}`) **الدردشـة مـع** : `{message}`",
            )


@jmthon.ar_cmd(
    pattern="وسبام (.*)",
    command=("وسبام", plugin_category),
    info={
        "header": "⌯︙ڪتابة النّص ڪلمة بعد ڪلمة 📝",
        "description": "⌔︙لل تكرار الدردشـة بجميع الڪلمات في النّص المعطى ڪرسـالة جديدة 💢.",
        "usage": "{tr}تكرار بالكلمه <text>",
        "examples": "{tr}تكرار بالكلمه كلمه1 كلمه2 كلمه3",
    },
)
async def tmeme(event):
    "⌔︙ڪتابة النّص ڪلمة بعد ڪلمة 📝"
    wspam = str("".join(event.text.split(maxsplit=1)[1:]))
    message = wspam.split()
    await event.delete()
    for word in message:
        await event.respond(word)
    if BOTLOG:
        if event.is_private:
            await event.client.send_message(
                BOTLOG_CHATID,
                "**⌯︙تكرار بالكلمه : **\n"
                + f"**⌯︙تم تنفيذ التكرار بواسطة الڪلمات في   :** [المستخـدم](tg://user?id={event.chat_id}) **الدردشـة مـع :** `{message}`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                "**⌯︙تكرار بالكلمه : **\n"
                + f"**⌯︙تم تنفيذ التكرار بواسطة الڪلمات في   :** {get_display_name(await event.get_chat())}(`{event.chat_id}`) **الدردشـة مـع :** `{message}`",
            )


@jmthon.ar_cmd(pattern="مكرر (.*)")
async def spammer(event):
    reply = await event.get_reply_message()
    input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    try:
        sleeptimet = sleeptimem = float(input_str[0])
    except Exception:
        return await edit_delete(
            event, "⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️"
        )
    jepthon = input_str[1:]
    await event.delete()
    addgvar("spamwork", True)
    await spam_function(event, reply, jepthon, sleeptimem, sleeptimet, DelaySpam=True)
@jmthon.ar_cmd(pattern="ايقاف مكرر ?(.*)")
async def stopspamrz(event):
    if gvarstatus("spamwork") is not None and gvarstatus("spamwork") == "true":
        delgvar("spamwork")
        return await edit_delete(event, "**⌔∮ تم بنجاح ايقاف التكرار **")
    return await edit_delete(event, "**⌔∮ عذرا لم يتم تفعيل التكرار بالاصل")
