# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#

import requests
import asyncio
import ast
import json

from pyrogram import *
from pyrogram.types import *

from TigerX import *
from TigerX.lib import *

from pykillerx.helper.content import *

async def copy_message(client, message):
    command_args = message.text.split()[1:]
    if len(command_args) != 1:
        await message.reply_text("Please provide a link to the message you want to copy")
        return
    link = command_args[0]
    blacklist_url = "https://raw.githubusercontent.com/xtsea/pyKillerX/main/blacklist_channel.json"
    response = requests.get(blacklist_url)
    if response.status_code == 200:
        blacklist_str = response.text.strip()
        blacklist = ast.literal_eval(blacklist_str)
    else:
        print("Failed to fetch blacklist")
    if any(link.startswith(prefix) for prefix in blacklist):
        await message.reply_text("Sorry, this command is not allowed in this channel/group.")
        return
    link_parts = link.split("/")
    try:
        chat_id = link_parts[-2] if len(link_parts) >= 2 and link_parts[-2] else None
    except ValueError:
        return
    message_id = int(link_parts[-1])
    try:
        await randydevhack(client, message, chat_id, message_id)
        await msg.delete()
    except Exception as e:
        return
