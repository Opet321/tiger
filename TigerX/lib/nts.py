from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram import Client as ren

from pykillerx.helper.tools import *
from pykillerx.helper.hacking import *

from TigerX import *
from TigerX.lib import *
from TigerX.lib.db.ntssql import *

async def list_notes(client, message):
    user_id = message.from_user.id
    notes = get_notes(str(user_id))
    if not notes:
        return await message.reply("no notes.")
    msg = f"Notes list\n"
    for note in notes:
        msg += f"• {note.keyword}\n"
    await message.reply(msg)

async def remove_notes(client, message):
    notename = get_arg(message)
    user_id = message.from_user.id
    if rm_note(str(user_id), notename) is False:
        return await message.reply(f"Couldn't find the record: {notename}")
    return await message.reply(f"Successfully deleted the notes: {notename}")

async def save_note(client, message):
    keyword = get_arg(message)
    user_id = message.from_user.id
    msg = message.reply_to_message
    if not msg:
        return await message.reply("please reply to message")
    xnxx = await msg.forward(client.me.id)
    msg_id = xnxx.id
    await client.send_message(client.me.id,
        f"#NOTE\nKEYWORD: {keyword}"
        "\n\n The following messages are stored as log reply data for chats, please do not delete them!!",
    )
    await sleep(1)
    add_note(str(user_id), keyword, msg_id)
    await message.reply(f"Successfully saved note {keyword}")

async def call_notes(client, message):
    notename = get_arg(message)
    user_id = message.from_user.id
    note = get_note(str(user_id), notename)
    if not note:
        return await message.reply("no such notes.")
    msg_o = await client.get_messages(client.me.id, int(note.f_mesg_id))
    await msg_o.copy(message.chat.id, reply_to_message_id=message.id)
