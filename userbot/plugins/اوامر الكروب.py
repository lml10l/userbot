from asyncio import sleep
from ..Config import Config
from telethon.errors import (
    ChatAdminRequiredError,
    FloodWaitError,
    MessageNotModifiedError,
    UserAdminInvalidError,
)
from telethon.tl import functions
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChannelParticipantsKicked,
    ChatBannedRights,
    UserStatusEmpty,
    UserStatusLastMonth,
    UserStatusLastWeek,
    UserStatusOffline,
    UserStatusOnline,
    UserStatusRecently,
)
from userbot import jmthon
from .. import jmthon
from ..core.logger import logging
from ..helpers.utils import reply_id
from ..sql_helper.locks_sql import *
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import readable_time
from . import BOTLOG, BOTLOG_CHATID

LOGS = logging.getLogger(__name__)
plugin_category = "admin"

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)


async def ban_user(chat_id, i, rights):
    try:
        await jmthon(functions.channels.EditBannedRequest(chat_id, i, rights))
        return True, None
    except Exception as exc:
        return False, str(exc)

@jmthon.on(admin_cmd(outgoing=True, pattern="تخوني$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois1:
        await vois.client.send_file(vois.chat_id, jpvois1, reply_to=Ti)
        await vois.delete()

@jmthon.on(admin_cmd(outgoing=True, pattern="مستمرة الكلاوات$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois2:
        await vois.client.send_file(vois.chat_id, jpvois2, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="احب العراق$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois3:
        await vois.client.send_file(vois.chat_id, jpvois3, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="احبك$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois4:
        await vois.client.send_file(vois.chat_id, jpvois4, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="اخت التنيج$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois5:
        await vois.client.send_file(vois.chat_id, jpvois5, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="اذا اكمشك$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois6:
        await vois.client.send_file(vois.chat_id, jpvois6, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="اسكت$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois7:
        await vois.client.send_file(vois.chat_id, jpvois7, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="افتهمنا$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois8:
        await vois.client.send_file(vois.chat_id, jpvois8, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="اكل خرا$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois9:
        await vois.client.send_file(vois.chat_id, jpvois9, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="العراق$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois10:
        await vois.client.send_file(vois.chat_id, jpvois10, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="الكعده وياكم$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois11:
        await vois.client.send_file(vois.chat_id, jpvois11, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="الكمر اني$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois12:
        await vois.client.send_file(vois.chat_id, jpvois12, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="اللهم لا شماته$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois13:
        await vois.client.send_file(vois.chat_id, jpvois13, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="اني مااكدر$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois14:
        await vois.client.send_file(vois.chat_id, jpvois14, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="بقولك ايه$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois15:
        await vois.client.send_file(vois.chat_id, jpvois15, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="تف على شرفك$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois16:
        await vois.client.send_file(vois.chat_id, jpvois16, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="شجلبت$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois17:
        await vois.client.send_file(vois.chat_id, jpvois17, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="شكد شفت ناس$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois18:
        await vois.client.send_file(vois.chat_id, jpvois18, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="صباح القنادر$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois19:
        await vois.client.send_file(vois.chat_id, jpvois19, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="ضحكة فيطية$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois20:
        await vois.client.send_file(vois.chat_id, jpvois20, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="طار القلب$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois21:
        await vois.client.send_file(vois.chat_id, jpvois21, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="غطيلي$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois22:
        await vois.client.send_file(vois.chat_id, jpvois22, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="في منتصف الجبهة$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois23:
        await vois.client.send_file(vois.chat_id, jpvois23, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="لاتقتل المتعه$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois24:
        await vois.client.send_file(vois.chat_id, jpvois24, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="لا لتغلط$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois25:
        await vois.client.send_file(vois.chat_id, jpvois25, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="لا يمه لا$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois26:
        await vois.client.send_file(vois.chat_id, jpvois26, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="لحد يحجي وياي$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois27:
        await vois.client.send_file(vois.chat_id, jpvois27, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="ماادري يعني$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois28:
        await vois.client.send_file(vois.chat_id, jpvois28, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="منو انت$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois29:
        await vois.client.send_file(vois.chat_id, jpvois29, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="مو صوجكم$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois30:
        await vois.client.send_file(vois.chat_id, jpvois30, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="خوش تسولف$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois31:
        await vois.client.send_file(vois.chat_id, jpvois31, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="يع$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois32:
        await vois.client.send_file(vois.chat_id, jpvois32, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="زيج$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois33:
        await vois.client.send_file(vois.chat_id, jpvois33, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="زيج2$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois34:
        await vois.client.send_file(vois.chat_id, jpvois34, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="يعني مااعرف$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois35:
        await vois.client.send_file(vois.chat_id, jpvois35, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="يامرحبا$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois36:
        await vois.client.send_file(vois.chat_id, jpvois36, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="منو انتة$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois37:
        await vois.client.send_file(vois.chat_id, jpvois37, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="ماتستحي$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois38:
        await vois.client.send_file(vois.chat_id, jpvois38, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="كعدت الديوث$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois39:
        await vois.client.send_file(vois.chat_id, jpvois39, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="عيب$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois40:
        await vois.client.send_file(vois.chat_id, jpvois40, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="عنعانم$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois41:
        await vois.client.send_file(vois.chat_id, jpvois41, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="طبك مرض$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois42:
        await vois.client.send_file(vois.chat_id, jpvois42, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="سييي$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois43:
        await vois.client.send_file(vois.chat_id, jpvois43, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="سبيدر مان$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois44:
        await vois.client.send_file(vois.chat_id, jpvois44, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="خاف حرام$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois45:
        await vois.client.send_file(vois.chat_id, jpvois45, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="تحيه لاختك$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois46:
        await vois.client.send_file(vois.chat_id, jpvois46, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="امشي كحبة$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois47:
        await vois.client.send_file(vois.chat_id, jpvois47, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="امداك$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois48:
        await vois.client.send_file(vois.chat_id, jpvois48, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="الحس$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois49:
        await vois.client.send_file(vois.chat_id, jpvois49, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="افتهمنا$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois50:
        await vois.client.send_file(vois.chat_id, jpvois32, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="اطلع برا$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois51:
        await vois.client.send_file(vois.chat_id, jpvois51, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="اخت التنيج$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois52:
        await vois.client.send_file(vois.chat_id, jpvois52, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="اوني تشان$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois53:
        await vois.client.send_file(vois.chat_id, jpvois53, reply_to=Ti)
        await vois.delete()
@jmthon.on(admin_cmd(outgoing=True, pattern="اوني تشان2$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if jpvois54:
        await vois.client.send_file(vois.chat_id, jpvois54, reply_to=Ti)
        await vois.delete()        
@jmthon.on(events.NewMessage(outgoing=True, pattern="ارسل?(.*)"))
async def remoteaccess(event):

    p = event.pattern_match.group(1)
    m = p.split(" ")

    chat_id = m[0]
    try:
        chat_id = int(chat_id)
    except BaseException:

        pass

    msg = ""
    mssg = await event.get_reply_message()
    if event.reply_to_msg_id:
        await event.client.send_message(chat_id, mssg)
        await event.edit("تم الارسال الرسالة الى الرابط الذي وضعتة")
    for i in m[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await event.client.send_message(chat_id, msg)
        await event.edit("تم ارسال الرساله الى الرابط الذي وضعتة")
    except BaseException:
        await event.edit("** عذرا هذا ليست مجموعة **")
@jmthon.ar_cmd(
    pattern="اطردني$",
    command=("اطردني", plugin_category),
    info={
        "header": "To kick myself from group.",
        "usage": [
            "{tr}kickme",
        ],
    },
    groups_only=True,
)
async def kickme(leave):
    "to leave the group."
    await leave.edit("⌯︙ حسنا سأغادر المجموعه وداعا ")
    await leave.client.kick_participant(leave.chat_id, "me")

@jmthon.ar_cmd(
    pattern="تفليش بالطرد$",
    command=("تفليش بالطرد", plugin_category),
    info={
        "header": "To kick everyone from group.",
        "description": "To Kick all from the group except admins.",
        "usage": [
            "{tr}kickall",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def _(event):
    "To kick everyone from group."
    result = await event.client(
        functions.channels.GetParticipantRequest(event.chat_id, event.client.uid)
    )
    if not result.participant.admin_rights.ban_users:
        return await edit_or_reply(
            event, "⌯︙- يبدو انه ليس لديك صلاحيات الحذف في هذه الدردشة "
        )
    catevent = await edit_or_reply(event, "`يتم الطرد انتظر قليلا `")
    admins = await event.client.get_participants(
        event.chat_id, filter=ChannelParticipantsAdmins
    )
    admins_id = [i.id for i in admins]
    total = 0
    success = 0
    async for user in event.client.iter_participants(event.chat_id):
        total += 1
        try:
            if user.id not in admins_id:
                await event.client.kick_participant(event.chat_id, user.id)
                success += 1
                await sleep(0.5)
        except Exception as e:
            LOGS.info(str(e))
            await sleep(0.5)
    await catevent.edit(
        f"⌯︙ تم بنجاح طرد من {total} الاعضاء ✅ "
    )

@jmthon.ar_cmd(
    pattern="تفليش$",
    command=("تفليش", plugin_category),
    info={
        "header": "To ban everyone from group.",
        "description": "To ban all from the group except admins.",
        "usage": [
            "{tr}kickall",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def _(event):
    "To ban everyone from group."
    result = await event.client(
        functions.channels.GetParticipantRequest(event.chat_id, event.client.uid)
    )
    if not result:
        return await edit_or_reply(
            event, "⌯︙- يبدو انه ليس لديك صلاحيات الحذف في هذه الدردشة ❕"
        )
    catevent = await edit_or_reply(event, "`نورتونا 😍😍`")
    admins = await event.client.get_participants(
        event.chat_id, filter=ChannelParticipantsAdmins
    )
    admins_id = [i.id for i in admins]
    total = 0
    success = 0
    async for user in event.client.iter_participants(event.chat_id):
        total += 1
        try:
            if user.id not in admins_id:
                await event.client(
                    EditBannedRequest(event.chat_id, user.id, BANNED_RIGHTS)
                )
                success += 1
                await sleep(0.5) # for avoid any flood waits !!-> do not remove it 
        except Exception as e:
            LOGS.info(str(e))
    await catevent.edit(
        f"⌯︙ تم بنجاح حظر من {total} الاعضاء ✅ "
    )



@jmthon.ar_cmd(
    pattern="حذف المحظورين$",
    command=("حذف المحظورين", plugin_category),
    info={
        "header": "To unban all banned users from group.",
        "usage": [
            "{tr}unbanall",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def _(event):
    "To unban all banned users from group."
    catevent = await edit_or_reply(
        event, "**⌯︙يتـم الـغاء حـظر الجـميع فـي هذه الـدردشـة**"
    )
    succ = 0
    total = 0
    flag = False
    chat = await event.get_chat()
    async for i in event.client.iter_participants(
        event.chat_id, filter=ChannelParticipantsKicked, aggressive=True
    ):
        total += 1
        rights = ChatBannedRights(until_date=0, view_messages=False)
        try:
            await event.client(
                functions.channels.EditBannedRequest(event.chat_id, i, rights)
            )
        except FloodWaitError as e:
            LOGS.warn(f"لقد حدث عمليه تكرار كثير ارجو اعادة الامر او انتظر")
            await catevent.edit(
                f"أنتـظر لـ {readable_time(e.seconds)} تحتاط لاعادة الامر لاكمال العملية"
            )
            await sleep(e.seconds + 5)
        except Exception as ex:
            await catevent.edit(str(ex))
        else:
            succ += 1
            if flag:
                await sleep(2)
            else:
                await sleep(1)
            try:
                if succ % 10 == 0:
                    await catevent.edit(
                        f"⌯︙ الغاء حظر جميع الحسابات\nتم الغاء حظر جميع الاعضاء بنجاح ✅"
                    )
            except MessageNotModifiedError:
                pass
    await catevent.edit(f"⌯︙الغاء حظر :__{succ}/{total} في الدردشه {chat.title}__")

# Ported by ©[NIKITA](t.me/kirito6969) and ©[EYEPATCH](t.me/NeoMatrix90)
@jmthon.ar_cmd(
    pattern="المحذوفين ?([\s\S]*)",
    command=("المحذوفين", plugin_category),
    info={
        "header": "To check deleted accounts and clean",
        "description": "Searches for deleted accounts in a group. Use `.zombies clean` to remove deleted accounts from the group.",
        "usage": ["{tr}zombies", "{tr}zombies clean"],
    },
    groups_only=True,
)
async def rm_deletedacc(show):
    "To check deleted accounts and clean"
    con = show.pattern_match.group(1).lower()
    del_u = 0
    del_status = "⌯︙ لم يتم العثور على حسابات متروكه او حسابات محذوفة الكروب نظيف"
    if con != "اطردهم":
        event = await edit_or_reply(
            show, "⌯︙ يتم البحث عن حسابات محذوفة او حسابات متروكة انتظر"
        )
        async for user in show.client.iter_participants(show.chat_id):
            if user.deleted:
                del_u += 1
                await sleep(0.5)
        if del_u > 0:
            del_status = f"⌯︙تـم العـثور : **{del_u}** على حسابات محذوفة ومتروكه في هذه الدردشه من الحسابات في هذه الدردشه,\
                           \nاطردهم بواسطه  `.المحذوفين اطردهم`"
        await event.edit(del_status)
        return
    chat = await show.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_delete(show, "أنا لسـت مشرف هـنا", 5)
        return
    event = await edit_or_reply(
        show, "⌯︙جاري حذف الحسابات المحذوفة"
    )
    del_u = 0
    del_a = 0
    async for user in show.client.iter_participants(show.chat_id):
        if user.deleted:
            try:
                await show.client.kick_participant(show.chat_id, user.id)
                await sleep(0.5)
                del_u += 1
            except ChatAdminRequiredError:
                await edit_delete(event, "⌯︙ ليس لدي صلاحيات الحظر هنا", 5)
                return
            except UserAdminInvalidError:
                del_a += 1
    if del_u > 0:
        del_status = f"التنظيف **{del_u}** من الحسابات المحذوفة"
    if del_a > 0:
        del_status = f"التنظيف **{del_u}** من الحسابات المحذوف \
        \n**{del_a}** لا يمكنني حذف حسابات المشرفين المحذوفة"
    await edit_delete(event, del_status, 5)
    if BOTLOG:
        await show.client.send_message(
            BOTLOG_CHATID,
            f"#تنـظيف الـمحذوفات\
            \n{del_status}\
            \nالـدردشة: {show.chat.title}(`{show.chat_id}`)",
        )


@jmthon.ar_cmd(
    pattern="احصائيات الاعضاء ?([\s\S]*)",
    command=("احصائيات الاعضاء", plugin_category),
    info={
        "header": "To get breif summary of members in the group",
        "description": "To get breif summary of members in the group . Need to add some features in future.",
        "usage": [
            "{tr}ikuck",
        ],
    },
    groups_only=True,
)
async def _(event):  # sourcery no-metrics
    "To get breif summary of members in the group.1 11"
    input_str = event.pattern_match.group(1)
    if input_str:
        chat = await event.get_chat()
        if not chat.admin_rights and not chat.creator:
            await edit_or_reply(event, " انت لست مشرف هنا ⌔︙")
            return False
    p = 0
    b = 0
    c = 0
    d = 0
    e = []
    m = 0
    n = 0
    y = 0
    w = 0
    o = 0
    q = 0
    r = 0
    et = await edit_or_reply(event, "يتم البحث في القوائم ⌔︙")
    async for i in event.client.iter_participants(event.chat_id):
        p += 1
        #
        # Note that it's "reversed". You must set to ``True`` the permissions
        # you want to REMOVE, and leave as ``None`` those you want to KEEP.
        rights = ChatBannedRights(until_date=None, view_messages=True)
        if isinstance(i.status, UserStatusEmpty):
            y += 1
            if "y" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if status:
                    c += 1
                else:
                    await et.edit("⌯︙ احتاج الى صلاحيات المشرفين للقيام بهذا الامر ")
                    e.append(str(e))
                    break
        if isinstance(i.status, UserStatusLastMonth):
            m += 1
            if "m" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if status:
                    c += 1
                else:
                    await et.edit("⌯︙ احتاج الى صلاحيات المشرفين للقيام بهذا الامر ")
                    e.append(str(e))
                    break
        if isinstance(i.status, UserStatusLastWeek):
            w += 1
            if "w" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if status:
                    c += 1
                else:
                    await et.edit("⌯︙ احتاج الى صلاحيات المشرفين للقيام بهذا الامر ")
                    e.append(str(e))
                    break
        if isinstance(i.status, UserStatusOffline):
            o += 1
            if "o" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await et.edit("⌯︙ احتاج الى صلاحيات المشرفين للقيام بهذا الامر ")
                    e.append(str(e))
                    break
                else:
                    c += 1
        if isinstance(i.status, UserStatusOnline):
            q += 1
            if "q" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await et.edit("⌯︙ احتاج الى صلاحيات المشرفين للقيام بهذا الامر ")
                    e.append(str(e))
                    break
                else:
                    c += 1
        if isinstance(i.status, UserStatusRecently):
            r += 1
            if "r" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if status:
                    c += 1
                else:
                    await et.edit("⌯︙احتاج الى صلاحيات المشرفين للقيام بهذا الامر ")
                    e.append(str(e))
                    break
        if i.bot:
            b += 1
            if "b" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await et.edit("⌯︙احتاج الى صلاحيات المشرفين للقيام بهذا الامر ")
                    e.append(str(e))
                    break
                else:
                    c += 1
        elif i.deleted:
            d += 1
            if "d" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if status:
                    c += 1
                else:
                    await et.edit("⌯︙احتاج الى صلاحيات المشرفين للقيام بهذا الامر ")
                    e.append(str(e))
        elif i.status is None:
            n += 1
    if input_str:
        required_string = """الـمطرودين {} / {} الأعـضاء
الحـسابـات المـحذوفة: {}
حـالة المستـخدم الفـارغه: {}
اخر ظهور منذ شـهر: {}
اخر ظـهور منـذ اسبوع: {}
غير متصل: {}
المستخدمين النشطون: {}
اخر ظهور قبل قليل: {}
البوتات: {}
مـلاحظة: {}"""
        await et.edit(required_string.format(c, p, d, y, m, w, o, q, r, b, n))
        await sleep(5)
    await et.edit(
        """: {} مـجموع المـستخدمين
الحـسابـات المـحذوفة: {}
حـالة المستـخدم الفـارغه: {}
اخر ظهور منذ شـهر: {}
اخر ظـهور منـذ اسبوع: {}
غير متصل: {}
المستخدمين النشطون: {}
اخر ظهور قبل قليل: {}
البوتات: {}
مـلاحظة: {}""".format(
            p, d, y, m, w, o, q, r, b, n
        )
    )
