import random
import re
import time
from datetime import datetime
from platform import python_version

from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from userbot import StartTime, jmthon, JMVERSION

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention

plugin_category = "utils"

#كتـابة وتعـديل:  @lMl10l
ALIVE_ET = Config.ALIVE_ET or "فحص"
@jmthon.on(admin_cmd(pattern=f"{ALIVE_ET}(?:\s|$)([\s\S]*)"))
    
async def amireallyalive(event):
    "للتـأكد من ان البـوت يعـمـل"
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await edit_or_reply(event, "** ⌯︙يتـم التـأكـد انتـظر قليلا رجاءا**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "✇ ◅"
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "**[ 𝗝𝗘𝗣𝗧𝗛𝗢𝗡 𝗜𝗦 𝗪𝗢𝗥𝗞𝗜𝗡𝗚 ✓ ](t.me/Jepthon)**"
    RR7_IMG = gvarstatus("ALIVE_PIC") or Config.A_PIC
    jmthon_caption = gvarstatus("ALIVE_TEMPLATE") or temp
    caption = jmthon_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        EMOJI=EMOJI,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        jmver=JMVERSION,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
    )
    if RR7_IMG:
        RR7 = [x for x in RR7_IMG.split()]
        PIC = random.choice(RR7)
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=caption, reply_to=reply_to_id
            )
            await event.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                event,
                f"**الميـديا خـطأ **\nغـير الرابـط بأستـخدام الأمـر  \n `.اضف_فار ALIVE_PIC رابط صورتك`\n\n**لا يمـكن الحـصول عـلى صـورة من الـرابـط :-** `{PIC}`",
            )
    else:
        await edit_or_reply(
            event,
            caption,
        )


temp = """{ALIVE_TEXT}
**{EMOJI} قاعدۿ البيانات ↜ ** تعمل بنـجاح ✓
**{EMOJI} أصـدار التـيليثون ↜ :** `{telever}`
**{EMOJI} أصـدار جـيبثون ↜  :** `{jmver}`
**{EMOJI} أصدار البـايثون ↜ :** `{pyver}`
**{EMOJI} الوقـت ↜ :** `{uptime}`
**{EMOJI} البنك ↜ :** `{ping}`
**{EMOJI} المسـتخدم ↜:** {mention}"""
