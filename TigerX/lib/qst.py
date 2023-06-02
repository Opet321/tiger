# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#

import asyncio
import random
from asyncio import sleep

from pyrogram import filters
from pyrogram.types import Message

from TigerX import *
from TigerX.lib import *

async def quotly(bot, message):
    kk = await message.reply_text("Making a quote")
    from_where = "QuotLyBot"
    msg = bool(message.reply_to_message)
    if not msg:
        await kk.edit("Please reply to a sticker message")
        return
    progress = 0 + random.randint(0, 100)
    if progress > 100:
        await kk.edit('There was a long running error')
        return
    await message.reply_to_message.forward(from_where)
    gg = await kk.edit(f"```Making a Quote\nProcessing {progress}%```")
    await asyncio.sleep(10)
    async for quotly in bot.search_messages(from_where, limit=1):
        if not quotly:
            return await message.edit("**Error Sticker Quotly**")
        await message.reply_sticker(sticker=quotly.sticker.file_id, reply_to_message_id=message.reply_to_message.id if message.reply_to_message else None)
        await gg.delete()
