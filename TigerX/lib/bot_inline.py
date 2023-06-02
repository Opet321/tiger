import time
import traceback
from sys import version as pyver
import os
import shlex
import textwrap
from typing import Tuple
import asyncio 
from os import getenv
from gc import get_objects
import io
import aiohttp
import requests
from io import BytesIO
from datetime import datetime as dt
from pyrogram.types import *
from pyrogram import *
import datetime

from pyrogram import Client
from pyrogram import __version__ as pyrover
from pyrogram.enums import ParseMode
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message,
)

from TigerX import ids as users
from TigerX import *
from TigerX.lib import *

from pykillerx.helper.inline import *
from pykillerx.helper.data import *
from pykillerx.help import *
from pykillerx.helper import *

async def _callbacks(_, callback_query):
    query = callback_query.data.lower()
    bot_me = await app.get_me()
    if query == "helper":
        buttons = paginate_help(0, CMD_HELP, "helpme")
        await app.edit_inline_text(
            callback_query.inline_message_id,
            Data.text_help_menu,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    elif query == "close":
        await app.edit_inline_text(callback_query.inline_message_id, "**— CLOSED**")
        return
    elif query == "close_help":
        if callback_query.from_user.id not in users:
           return
        await app.edit_inline_text(
            callback_query.inline_message_id,
            "**Closed Help**",
            reply_markup=InlineKeyboardMarkup(Data.reopen),
        )
        return
    elif query == "closed":
        try:
            await callback_query.message.delete()
        except BaseException:
            pass
        try:
            await callback_query.message.reply_to_message.delete()
        except BaseException:
            pass
    elif query == "make_basic_button":
        try:
            bttn = paginate_help(0, CMD_HELP, "helpme")
            await app.edit_inline_text(
                callback_query.inline_message_id,
                Data.text_help_menu,
                reply_markup=InlineKeyboardMarkup(bttn),
            )
        except Exception as e:
            e = traceback.format_exc()
            print(e, "Callbacks")

async def on_plug_in_cb(_, callback_query):
    modul_name = callback_query.matches[0].group(1)
    commands: dict = CMD_HELP[modul_name]
    this_command = f"──「 **Help For {str(modul_name).upper()}** 」──\n\n"
    for x in commands:
        this_command += f"  •  **Command:** `.{str(x)}`\n  •  **Function:** `{str(commands[x])}`\n\n"
    this_command += "© TigerX"
    bttn = [
        [
            InlineKeyboardButton("Support", url="https://t.me/RendyProjects"),
            InlineKeyboardButton(text="Return", callback_data="reopen"),
        ]
    ]
    reply_pop_up_alert = (
        this_command
        if this_command is not None
        else f"{module_name} No documentation has been written for the module."
    )
    await app.edit_inline_text(
        callback_query.inline_message_id,
        reply_pop_up_alert,
        reply_markup=InlineKeyboardMarkup(bttn),
    )

async def reopen_in_cb(_, callback_query):
    buttons = paginate_help(0, CMD_HELP, "helpme")
    await app.edit_inline_text(
        callback_query.inline_message_id,
        Data.text_help_menu,
        reply_markup=InlineKeyboardMarkup(buttons),
    )

async def on_plug_prev_in_cb(_, callback_query):
    current_page_number = int(callback_query.matches[0].group(1))
    buttons = paginate_help(current_page_number - 1, CMD_HELP, "helpme")
    await app.edit_inline_text(
        callback_query.inline_message_id,
        Data.text_help_menu,
        reply_markup=InlineKeyboardMarkup(buttons),
    )

async def on_plug_next_in_cb(_, callback_query):
    current_page_number = int(callback_query.matches[0].group(1))
    buttons = paginate_help(current_page_number + 1, CMD_HELP, "helpme")
    await app.edit_inline_text(
        callback_query.inline_message_id,
        Data.text_help_menu,
        reply_markup=InlineKeyboardMarkup(buttons),
    )
