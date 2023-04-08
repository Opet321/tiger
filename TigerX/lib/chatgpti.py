# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#
# developer credits @xtsea

import requests
from io import BytesIO
import os
import json
import random
import asyncio
from pyrogram import *
from pyrogram.types import *

from TigerX import OPENAI_API

from TigerX import *
from TigerX.lib import *

from pykillerx.openai import PayLoadHeaders, ImageGenerator
from pykillerx.types import SendPhoto

async def new_model_chatgpt(client, message):
    ran = await message.reply_text("<code>Processing....</code>")
    RAPIDAPI = "ce36c261f1mshb4a0a55aaca548ep12c9f3jsn3d6761cb63fb"
    asked = message.text.split(None, 1)[1] if len(message.command) != 1 else None
    if not asked:
        await ran.edit_text("question ask this chagpt")
        return
    url = "https://openai80.p.rapidapi.com/completions"
    payload_headers = PayLoadHeaders("text-davinci-003", asked, RAPIDAPI)
    response = requests.request("POST", url, json=payload_headers.payload, headers=payload_headers.headers)
    if not RAPIDAPI:
        await ran.edit_text("Missing Api key: <code>rapidapi.com</code>")
        return
    if response.status_code == 200:
        data_model = response.json()
        try:
            text_davinci = data_model["choices"][0]["text"]
        except Exception as e:
            await ran.edit_text(f"Error request {e}")
            return
        if text_davinci:
            await ran.edit(text_davinci)
        else:
            await ran.edit_text("Yahh, sorry i can't get your answer")
    else:
        await ran.edit_text("failed to api chatgpt")
    

# using original openai.com 

async def chatgpt_ask(c, m):
    question = (m.text.split(None, 1)[1] if len(m.command) != 1 else None)
    if not question:
       await m.reply(f"use command <code>.{m.command[0]} [question]</code> to ask questions using the API.")
       return
    if not OPENAI_API:
       await m.reply("missing api key : `OPENAI_API`")
       return
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {OPENAI_API}"}
    json_data = {"model": "text-davinci-003", "prompt": question, "max_tokens": 200, "temperature": 0}
    msg = await m.reply(f"Wait a moment looking for your answer..")
    try:
        response = (await http.post("https://api.openai.com/v1/completions", headers=headers, json=json_data)).json()
        await msg.edit(response["choices"][0]["text"])
    except MessageNotModified:
        pass
    except Exception as e:
        await msg.edit_text(f"Yahh, sorry i can't get your answer: {e}")


# Credits @xtsea 
# DON'T REMOVE CREDITS THIS

# using rapidapi.com

async def chatpgt_image_generator(client, message):
    ran = await message.reply_text("<code>Processing....</code>")
    APIKEY = "ce36c261f1mshb4a0a55aaca548ep12c9f3jsn3d6761cb63fb"
    ask_image = message.text.split(None, 1)[1] if len(message.command) != 1 else None
    if not ask_image:
        await ran.edit_text("question ask this other picture")
        return
    if not APIKEY:
       await ran.edit_text("Missing Api key: <code>rapidapi.com</code>")
       return
    url = "https://openai80.p.rapidapi.com/images/generations"
    payload_image = ImageGenerator(ask_image, "1024x1024", APIKEY)
    headers = {"content-type": "application/json", "X-RapidAPI-Key": APIKEY, "X-RapidAPI-Host": "openai80.p.rapidapi.com"}
    response = requests.request("POST", url, json=payload_image.payload, headers=payload_image.headers)
    if response.status_code == 200:
        data_image = response.json()
        try:
            image_url = data_image["data"][0]["url"]
        except Exception as e:
            await ran.edit_text(f"Error request {e}")
            return
        if send_image:
            send_image = SendPhoto(chat_id=message.chat.id, photo=image_url, replywithme=message.id)
            await send_image(client)
        else:
            await ran.edit_text("Yahh, sorry i can't get your photo")
    else:
        await ran.edit_text("Failed to api chatgpt image")
    try:
        await ran.delete()
    except Exception:
        pass

async def new_chatgpt_turbo(client, message):
    ran = await message.reply_text("<code>Processing....</code>")
    APIKEY = "ce36c261f1mshb4a0a55aaca548ep12c9f3jsn3d6761cb63fb"
    ask_turbo = message.text.split(None, 1)[1] if len(message.command) != 1 else None
    if not ask_turbo:
        await ran.edit_text("for example the question asked this chatgpt")
        return
    if not APIKEY:
       await ran.edit_text("Missing Api key: <code>rapidapi.com</code>")
       return
    url = "https://openai80.p.rapidapi.com/chat/completions"
    payload = {"model": "gpt-3.5-turbo", "messages": [{"role": "user", "content": ask_turbo}]}
    headers = {"content-type": "application/json", f"X-RapidAPI-Key": APIKEY, "X-RapidAPI-Host": "openai80.p.rapidapi.com"}
    response = requests.request("POST", url, json=payload, headers=headers)
    if response.status_code == 200:
        data_turbo = response.json()
        try:
            message_text = data_turbo["choices"][0]["message"]["content"]
        except Exception as e:
            await ran.edit_text(f"Error request {e}")
            return
        if message_text:
            await ran.edit_text(message_text)
        else:
            await ran.edit_text("Yahh, sorry i can't get your answer")
    else:
        await ran.edit_text("Failed to api chatgpt turbo")
