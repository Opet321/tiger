import requests
import spotify_token as st
from pyrogram import Client, enums, filters
from TigerX import *
from TigerX.lib import *

async def lyrics(client, message):
    if len(message.command) == 1:
        await message.reply("Usage: `.lyrics <song>`")
    else:
        query = message.text[1+6+1:]

    if not SP_DC and not SP_KEY:
        await message.reply("Missing api key: `SP_DC` and `SP_KEY`")
        return
