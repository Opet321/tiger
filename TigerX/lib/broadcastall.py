# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#

import asyncio
from pyrogram import *
from pyrogram.types import *
from requests import get

from TigerX import *
from TigerX.lib import *

from pykillerx import *
from pykillerx.helper import *
from pykillerx.blacklist import *

BLACKLIST = GROUP

def get_arg(message: Message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    return "" if not " ".join(split[1:]).strip() else " ".join(split[1:])

async def gcast_all(client, message):
    if message.reply_to_message or get_arg(message):
        tex = await message.reply_text("`Started global broadcast...`")
    else:
        return await message.edit_text("**Give A Message or Reply**")
    done = 0
    error = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            if message.reply_to_message:
                msg = message.reply_to_message
            elif get_arg:
                msg = get_arg(message)
            chat = dialog.chat.id
            if chat not in BLACKLIST:
                try:
                    if message.reply_to_message:
                        await msg.copy(chat)
                    elif get_arg:
                        await client.send_message(chat, msg)
                    done += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    error += 1
                    await asyncio.sleep(0.3)
    await tex.edit_text(
        f"**Successfully Sent Message To** `{done}` **Groups, chat, Failed to Send Message To** `{error}` **Groups**"
    )

async def gforward_all(client, message):
    if message.reply_to_message:
        lol = await message.reply_text("`Started global broadcast forward...`")
    else:
        return await message.edit_text("**Please reply**")
    kntl = 0
    rusak = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            if message.reply_to_message:
                msg = message.reply_to_message
            chat = dialog.chat.id
            if chat not in BLACKLIST:
                try:
                    if message.reply_to_message:
                        await msg.forward(chat, disable_notification=True)
                    kntl += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    rusak += 1
                    await asyncio.sleep(0.3)
    await lol.edit_text(
        f"**Successfully Sent Message To** `{kntl}` **Groups Forwarded, Failed to Send Message To** `{rusak}` **Groups**"
    )

async def guforward_all(client, message):
    if message.reply_to_message:
        lol = await message.reply_text("`Started global broadcast pm private forward...`")
    else:
        return await message.edit_text("**Please reply**")
    kntl = 0
    rusak = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE and not dialog.chat.is_verified:
            if message.reply_to_message:
                msg = message.reply_to_message
            chat = dialog.chat.id
            if chat not in DEVS:
                try:
                    if message.reply_to_message:
                        await msg.forward(chat, disable_notification=True)
                    kntl += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    rusak += 1
                    await asyncio.sleep(0.3)
    await lol.edit_text(
        f"**Successfully Sent Message To** `{kntl}` **pm forward, Failed to Send Message To** `{rusak}` **Chat**"
    )

async def gucast_all(client, message):
    if message.reply_to_message or get_arg(message):
        tex = await message.reply_text("`Started global broadcast...`")
    else:
        return await message.edit_text("**Give A Message or Reply**")
    done = 0
    error = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE and not dialog.chat.is_verified:
            if message.reply_to_message:
                msg = message.reply_to_message
            elif get_arg:
                msg = get_arg(message)
            chat = dialog.chat.id
            if chat not in DEVS:
                try:
                    if message.reply_to_message:
                        await msg.copy(chat)
                    elif get_arg:
                        await client.send_message(chat, msg)
                    done += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    error += 1
                    await asyncio.sleep(0.3)
    await tex.edit_text(
        f"**Successfully Sent Message To** `{done}` **pm forward, Failed to Send Message To** `{error}` **chat**"
    )
