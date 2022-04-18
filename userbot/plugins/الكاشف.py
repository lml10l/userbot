import asyncio

from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import CMD_HELP, jmthon
from . import parse_pre, sanga_seperator


@jmthon.on(admin_cmd(pattern="(الاسماء|المعرفات)($| (.*))"))
@jmthon.on(sudo_cmd(pattern="(الاسماء|المعرفات)($| (.*))", allow_sudo=True))
async def _(event):
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply_message = await event.get_reply_message()
    if not input_str and not reply_message:
        await edit_delete(
            event,
            "**⌔∮بالرد على الرسالة النصية للمستخدم للحصول على سجل الاسماء القديمه للمستخدم أو عرض سجل معرفات حساب المستخدم**",
        )
    if input_str:
        try:
            uid = int(input_str)
        except ValueError:
            try:
                u = await event.client.get_entity(input_str)
            except ValueError:
                await edit_delete(
                    event, "**⌔∮اكتب الامر + معرف المستخدم أو اسم المستخدم للعثور على سجل الاسماء القديمه**"
                )
            uid = u.id
    else:
        uid = reply_message.sender_id
    chat = "@SangMataInfo_bot"
    event = await edit_or_reply(event, "**⌔∮جـارِ الكشـف ...**")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message(f"/search_id {uid}")
        except YouBlockedUserError:
            await edit_delete(event, "`unblock @Sangmatainfo_bot and then try`")
        responses = []
        while True:
            try:
                response = await conv.get_response(timeout=2)
            except asyncio.TimeoutError:
                break
            responses.append(response.text)
        await event.client.send_read_acknowledge(conv.chat_id)
    if not responses:
        await edit_delete(event, "`bot can't fetch results`")
    if "No records found" in responses:
        await edit_delete(event, "**⌔∮المستخدم ليس لديه أي سجل ...**")
    names, usernames = await sanga_seperator(responses)
    cmd = event.pattern_match.group(1)
    if cmd == "الاسماء":
        lone = None
        for i in names:
            if lone:
                await event.reply(i, parse_mode=parse_pre)
            else:
                lone = True
                await event.edit(i, parse_mode=parse_pre)
    elif cmd == "المعرفات":
        lone = None
        for i in usernames:
            if lone:
                await event.reply(i, parse_mode=parse_pre)
            else:
                lone = True
                await event.edit(i, parse_mode=parse_pre)


CMD_HELP.update(
    {
        "الكاشف": "**الامر : **`.الاسماء <ايدي/معرف/بالرد>`\
    \n**الوظيفة : **يظهر لك تاريخ الاسم السابق للمستخدم\
    \n\n**الامـر : **`.المعرفات <معرف/ايدي/بالرد>`\
    \n**الوظيفة : **يظهر لك تاريخ اسم المستخدم السابق للمستخدم\
    "
    }
)
