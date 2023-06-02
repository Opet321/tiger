# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#
# Credits by : https://t.me/xtsea

from pyrogram import Client, filters
from pyrogram.types import Message
from pykillerx.helper.content import *
from TigerX import SAVE_CONTENT

async def verification_user(client, message, link):
    user_msg = f"""
full_name : `{message.from_user.first_name}`
username : @{message.from_user.username}
userID: `{message.from_user.id}`
mentioned : {message.from_user.mention}
copied link : {link}
""" 
    await client.send_message(SAVE_CONTENT, user_msg, disable_web_page_preview=True)

async def ass_copy_link(client, message):
    if message.text:
        link = message.text
        if "https://t.me/" in link:
            link_target = link.split("/")
            try:
                chat_id = link_target[-2]
            except ValueError as e:
                await message.reply_text(f"{e}")
                return
            message_id = int(link_target[-1])
            try:
                await randydevhack(client, message, chat_id, message_id)
                await verification_user(client, message, link)
                anak_bocah_coding = memekontol()
                await client.copy_message(SAVE_CONTENT, from_chat_id=chat_id, message_id=message_id, caption=None, reply_markup=anak_bocah_coding)
            except Exception:
                return
