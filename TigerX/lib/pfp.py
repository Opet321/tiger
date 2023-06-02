import os
from asyncio import sleep
import os
import sys
from re import sub
from time import time


from pyrogram import filters, enums
from pyrogram import Client as ren
from pyrogram import Client
from pyrogram.types import Message

from TigerX import *
from TigerX.lib import *

from pykillerx.helper.hacking import *
from pykillerx import *
from pykillerx.helper import *
from pykillerx.blacklist import *
from pykillerx.help import *


flood = {}
profile_photo = "cache/pfp.jpg"


async def extract_userid(message, text: str):
    def is_int(text: str):
        try:
            int(text)
        except ValueError:
            return False
        return True

    text = text.strip()

    if is_int(text):
        return int(text)

    entities = message.entities
    app = message._client
    if len(entities) < 2:
        return (await app.get_users(text)).id
    entity = entities[1]
    if entity.type == "mention":
        return (await app.get_users(text)).id
    return entity.user.id if entity.type == "text_mention" else None


async def extract_user_and_reason(message, sender_chat=False):
    args = message.text.strip().split()
    text = message.text
    user = None
    reason = None
    if message.reply_to_message:
        reply = message.reply_to_message
        if reply.from_user:
            id_ = reply.from_user.id

        elif (
                reply.sender_chat
                and reply.sender_chat != message.chat.id
                and sender_chat
            ):
            id_ = reply.sender_chat.id
        else:
            return None, None
        reason = None if len(args) < 2 else text.split(None, 1)[1]
        return id_, reason

    if len(args) == 2:
        user = text.split(None, 1)[1]
        return await extract_userid(message, user), None

    if len(args) > 2:
        user, reason = text.split(None, 2)[1:]
        return await extract_userid(message, user), reason

    return user, reason


async def extract_user(message):
    return (await extract_user_and_reason(message))[0]

async def unblock_user(client, message):
    user_id = await extract_user(message)
    tex = await message.reply_text("`Processing . . .`")
    if not user_id:
        return await message.edit(
            "Provide User ID/Username or reply to user message to unblock."
        )
    if user_id == client.me.id:
        return await tex.edit("Done ✅.")
    await client.unblock_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await message.edit(f"**Successfully Unblocked** {umention}")

async def block_user(client, message):
    user_id = await extract_user(message)
    tex = await message.reply_text("`Processing . . .`")
    if not user_id:
        return await tex.edit_text(
            "Provide User ID/Username or reply to user message to block."
        )
    if user_id == client.me.id:
        return await tex.edit_text("Done ✅.")
    await client.block_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await tex.edit_text(f"**Successfully blocked** {umention}")

async def setname(client, message):
    tex = await message.reply_text("`Processing . . .`")
    if len(message.command) == 1 or len(message.command) <= 1:
        return await tex.edit(
            "Provide a text to set as your name."
        )
    name = message.text.split(None, 1)[1]
    try:
        await client.update_profile(first_name=name)
        await tex.edit(f"**Successfully Changed Your Name To** `{name}`")
    except Exception as e:
        await tex.edit(f"**ERROR:** `{e}`")

async def set_bio(client, message):
    tex = await message.edit_text("`Processing . . .`")
    if len(message.command) == 1 or len(message.command) <= 1:
        return await tex.edit("Provide text to set as bio.")
    bio = message.text.split(None, 1)[1]
    try:
        await client.update_profile(bio=bio)
        await tex.edit(f"**Successfully Change your BIO to** `{bio}`")
    except Exception as e:
        await tex.edit(f"**ERROR:** `{e}`")

async def set_pfp(client, message):
    replied = message.reply_to_message
    if (
        replied
        and replied.media
        and (
            replied.photo
            or (replied.document and "image" in replied.document.mime_type)
        )
    ):
        await client.download_media(message=replied, file_name=profile_photo)
        await client.set_profile_photo(profile_photo)
        if os.path.exists(profile_photo):
            os.remove(profile_photo)
        await message.reply_text("**Your Profile Photo Changed Successfully.**")
    else:
        await message.reply_text(
            "Reply to any photo to set as profile photo"
        )
        await sleep(3)
        await message.delete()

