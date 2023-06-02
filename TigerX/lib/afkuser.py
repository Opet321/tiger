import asyncio
from datetime import datetime as dt

import humanize
from pyrogram import *
from pyrogram.types import *

from TigerX import *
from TigerX.lib import *

from pykillerx.helper.hacking import *
from pykillerx.helper import *
from pykillerx.blacklist import *


AFK = False
AFK_REASON = ""
AFK_TIME = ""
USERS = {}
GROUPS = {}

def subtract_time(start, end):
    subtracted = humanize.naturaltime(start - end)
    return str(subtracted)



async def collect_afk_messages(bot, message):
    if not AFK:
        return
    last_seen = subtract_time(dt.now(), AFK_TIME)
    is_group = message.chat.type in ["supergroup", "group"]
    CHAT_TYPE = GROUPS if is_group else USERS

    if GetChatID(message) not in CHAT_TYPE:
        text = (
            f"`Beep boop. This is an automated message.\n"
            f"I am not available right now.\n"
            f"Last seen: {last_seen}\n"
            f"Reason: ```{AFK_REASON.upper()}```\n"
            f"See you after I'm done doing whatever I'm doing.`"
        )
        await bot.send_message(
            chat_id=GetChatID(message),
            text=text,
            reply_to_message_id=ReplyCheck(message),
        )
        CHAT_TYPE[GetChatID(message)] = 1
        return
    elif GetChatID(message) in CHAT_TYPE:
        if CHAT_TYPE[GetChatID(message)] == 50:
            text = (
                f"`This is an automated message\n"
                f"Last seen: {last_seen}\n"
                f"This is the 10th time I've told you I'm AFK right now..\n"
                f"I'll get to you when I get to you.\n"
                f"No more auto messages for you`"
            )
            await bot.send_message(
                chat_id=GetChatID(message),
                text=text,
                reply_to_message_id=ReplyCheck(message),
            )
        elif CHAT_TYPE[GetChatID(message)] > 50:
            return
        elif CHAT_TYPE[GetChatID(message)] % 5 == 0:
            text = (
                f"`Hey I'm still not back yet.\n"
                f"Last seen: {last_seen}\n"
                f"Still busy: ```{AFK_REASON.upper()}```\n"
                f"Try pinging a bit later.`"
            )
            await bot.send_message(
                chat_id=GetChatID(message),
                text=text,
                reply_to_message_id=ReplyCheck(message),
            )

    CHAT_TYPE[GetChatID(message)] += 1

async def afk_set_all(bot, message):
    global AFK_REASON, AFK, AFK_TIME
    cmd = message.command
    afk_text = " ".join(cmd[1:]) if len(cmd) > 1 else ""
    if isinstance(afk_text, str):
        AFK_REASON = afk_text

    AFK = True
    AFK_TIME = dt.now()
    await message.delete()

async def afk_unset_all(bot, message):
    global AFK, AFK_TIME, AFK_REASON, USERS, GROUPS

    if AFK:
        last_seen = subtract_time(dt.now(), AFK_TIME).replace("ago", "").strip()
        await message.edit(
            f"`While you were away (for {last_seen}), you received {sum(USERS.values()) + sum(GROUPS.values())} "
            f"messages from {len(USERS) + len(GROUPS)} chats`"
        )
        AFK = False
        AFK_TIME = ""
        AFK_REASON = ""
        USERS = {}
        GROUPS = {}
        await asyncio.sleep(5)

    await message.delete()

async def auto_afk_unset_all(bot, message):
       global AFK, AFK_TIME, AFK_REASON, USERS, GROUPS

       if AFK:
           last_seen = subtract_time(dt.now(), AFK_TIME).replace("ago", "").strip()
           reply = await message.reply(
               f"`While you were away (for {last_seen}), you received {sum(USERS.values()) + sum(GROUPS.values())} "
               f"messages from {len(USERS) + len(GROUPS)} chats`"
           )
           AFK = False
           AFK_TIME = ""
           AFK_REASON = ""
           USERS = {}
           GROUPS = {}
           await asyncio.sleep(5)
           await reply.delete()
