# Copyright (C) 2022 JepThon TEAM

import asyncio
import math
import os

import heroku3
import requests
import urllib3

from userbot import jmthon

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply

plugin_category = "tools"

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# =================

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY


@jmthon.ar_cmd(
    pattern="(اضف|المعلومات|حذف) فار ([\s\S]*)",
    command=("فار", plugin_category),
    info={
        "header": "To manage heroku vars.",
        "flags": {
            "set": "To set new var in heroku or modify the old var",
            "get": "To show the already existing var value.",
            "del": "To delete the existing value",
        },
        "usage": [
            "{tr}set var <var name> <var value>",
            "{tr}get var <var name>",
            "{tr}del var <var name>",
        ],
        "examples": [
            "{tr}get var ALIVE_NAME",
        ],
    },
)
async def variable(var):  # sourcery no-metrics
    """
    Manage most of ConfigVars setting, set new var, get current var, or delete var...
    """
    if (Config.HEROKU_API_KEY is None) or (Config.HEROKU_APP_NAME is None):
        return await edit_delete(
            var,
            "⌯︙يجـب وضع الـفارات المطـلوبة لاستخدام الأمر \n ⌯︙يجب وضع `HEROKU_API_KEY` و `HEROKU_APP_NAME",
        )
    app = Heroku.app(Config.HEROKU_APP_NAME)
    exe = var.pattern_match.group(1)
    heroku_var = app.config()
    if exe == "المعلومات":
        cat = await edit_or_reply(var, "`⌯︙يـتم سـحب المعـلومـات`")
        await asyncio.sleep(1.0)
        try:
            variable = var.pattern_match.group(2).split()[0]
            if variable in heroku_var:
                return await cat.edit(
                    "**معلـومات الـفار**:" f"\n\n`{variable}` = `{heroku_var[variable]}`\n"
                )
            await cat.edit(
                "**معلـومات الـفار**:" f"\n\nخـطأ:\n-> `{variable}` ه"
            )
        except IndexError:
            configs = prettyjson(heroku_var.to_dict(), indent=2)
            with open("configs.json", "w") as fp:
                fp.write(configs)
            with open("configs.json", "r") as fp:
                result = fp.read()
                await edit_or_reply(
                    cat,
                    "`[HEROKU]` معلومات الفار:\n\n"
                    "================================"
                    f"\n```{result}```\n"
                    "================================",
                )
            os.remove("configs.json")
    elif exe == "اضف":
        variable = "".join(var.text.split(maxsplit=2)[2:])
        cat = await edit_or_reply(var, "`⌯︙يتم سحب المعلومات`")
        if not variable:
            return await cat.edit("⌯︙`.ضع فار <كود الفار> <القيمة>`")
        value = "".join(variable.split(maxsplit=1)[1:])
        variable = "".join(variable.split(maxsplit=1)[0])
        if not value:
            return await cat.edit("⌯︙`.ضع فار <كود الفار> <القيمة>`")
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await cat.edit(f"`⌯︙`{variable}`  تم بنجاح التغيير الى  \n  ⌯︙`{value}`")
        else:
            await cat.edit(
                f"⌯︙`{variable}`  تم بنجاح اضافه القيمة مع \n   ⌯︙`{value}`"
            )
        heroku_var[variable] = value
    elif exe == "حذف":
        cat = await edit_or_reply(var, "⌯︙يتم سحب المعلومات انتظر")
        try:
            variable = var.pattern_match.group(2).split()[0]
        except IndexError:
            return await cat.edit("⌯︙يرجـى تحديد الفار التي تريد حذفه")
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
            return await cat.edit(f"`{variable}`**  لايوجد**")

        await cat.edit(f"`{variable}`  **تم الحذف بنجاح**")
        del heroku_var[variable]


@jmthon.ar_cmd(
    pattern="استخدامي$",
    command=("استخدامي", plugin_category),
    info={
        "header": "To Check dyno usage of userbot and also to know how much left.",
        "usage": "{tr}usage",
    },
)
async def dyno_usage(dyno):
    """
    Get your account Dyno Usage
    """
    if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
        return await edit_delete(
            dyno,
            "⌯︙يجـب وضع الـفارات المطـلوبة لاستخدام الأمر \n ⌯︙يجب وضع `HEROKU_API_KEY` و `HEROKU_APP_NAME",
        )
    dyno = await edit_or_reply(dyno, "`⌯︙يـتم الـحساب`")
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    user_id = Heroku.account().id
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {Config.HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = f"/accounts/{user_id}/actions/get-quota"
    r = requests.get(heroku_api + path, headers=headers)
    if r.status_code != 200:
        return await dyno.edit(
            "⌯︙خـطأ : يبـدو ان هـنالك خـطأ ما حـدث\n\n" f">.`{r.reason}`\n"
        )
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]

    # - Used -
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)
    # - Current -
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)
    await asyncio.sleep(1.5)
    return await dyno.edit(
        "**اسـتخدام الـدينو**:\n\n"
        f" ⌯︙مـدة الاستخـدام لديـك  **{Config.HEROKU_APP_NAME}**:\n"
        f"     •  `{AppHours}`**سـاعات**  `{AppMinutes}`**دقـائق**  "
        f"**|**  [`{AppPercentage}`**%**]"
        "\n\n"
        " ⌯︙الساعات المتبقية لهذا الشهر :\n"
        f"     •  `{الساعات}`**h**  `{الدقائق}`**m**  "
        f"**|**  [`{percentage}`**%**]"
    )


@jmthon.ar_cmd(
    pattern="(herokulogs|الدخول)$",
    command=("الدخول", plugin_category),
    info={
        "header": "To get recent 100 lines logs from heroku.",
        "usage": ["{tr}herokulogs", "{tr}logs"],
    },
)
async def _(dyno):
    "To get recent 100 lines logs from heroku"
    if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
        return await edit_delete(
            dyno,
            "⌯︙يجـب وضع الـفارات المطـلوبة لاستخدام الأمر \n ⌯︙يجب وضع `HEROKU_API_KEY` و `HEROKU_APP_NAME",
        )
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        app = Heroku.app(HEROKU_APP_NAME)
    except BaseException:
        return await dyno.reply(
            " ⌯︙ عذرا لا يمكنك استخدام اوامر الفارات وهيروكو الا بعد اضافة كود هيروكو الى الفارات شرح الاضافة [اضغط هنا](https://t.me/Jepthon2)"
        )
    data = app.get_log()
    await edit_or_reply(
        dyno, data, deflink=True, linktext="⌯︙هـذه اخـر 100 سـطر في هيـروكو: **"
    )


def prettyjson(obj, indent=2, maxlinelength=80):
    """Renders JSON content with indentation and line splits/concatenations to fit maxlinelength.
    Only dicts, lists and basic types are supported"""
    items, _ = getsubitems(
        obj,
        itemkey="",
        islast=True,
        maxlinelength=maxlinelength - indent,
        indent=indent,
    )
    return indentitems(items, indent, level=0)
