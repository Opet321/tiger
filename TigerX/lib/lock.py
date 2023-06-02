from pyrogram.errors.exceptions.bad_request_400 import (
    ChatAdminRequired,
    ChatNotModified,
)

from pyrogram.types import *
from pyrogram import *

from TigerX import *
from TigerX.lib import *

from pykillerx import *
from pykillerx.helper import *

incorrect_parameters = "Parameter Wrong, Type `.help locks`"
data = {
    "msg": "can_send_messages",
    "stickers": "can_send_other_messages",
    "gifs": "can_send_other_messages",
    "media": "can_send_media_messages",
    "games": "can_send_other_messages",
    "inline": "can_send_other_messages",
    "url": "can_add_web_page_previews",
    "polls": "can_send_polls",
    "info": "can_change_info",
    "invite": "can_invite_users",
    "pin": "can_pin_messages",
}


async def tg_lock(
    client: Client,
    message: Message,
    parameter,
    permissions: list,
    perm: str,
    lock: bool,
):
    if lock:
        if perm not in permissions:
            return await message.edit_text(f"🔒 `{parameter}` **is already locked!**")
        permissions.remove(perm)
    elif perm in permissions:
        return await message.edit_text(f"🔓 `{parameter}` **is already Unlocked!**")
    else:
        permissions.append(perm)
    permissions = {perm: True for perm in list(set(permissions))}
    try:
        await client.set_chat_permissions(
            message.chat.id, ChatPermissions(**permissions)
        )
    except ChatNotModified:
        return await message.edit_text(
            f"To unlock this, you have to `{prefix}unlock msg` first."
        )
    except ChatAdminRequired:
        return await message.edit_text("`I don't have permission to do that.`")
    await message.edit_text(
        (
            f"🔒 **Locked for non-admin!**\n  **Type:** `{parameter}`\n  **Chat:** {message.chat.title}"
            if lock
            else f"🔒 **Unlocked for non-admin!**\n  **Type:** `{parameter}`\n  **Chat:** {message.chat.title}"
        )
    )

async def locks_all_or_unlock_all(client, message):
    if len(message.command) != 2:
        return await message.edit_text(incorrect_parameters)
    chat_id = message.chat.id
    parameter = message.text.strip().split(None, 1)[1].lower()
    state = message.command[0].lower()
    if parameter not in data and parameter != "all":
        return await message.edit_text(incorrect_parameters)
    permissions = await current_chat_permissions(client, chat_id)
    if parameter in data:
        await tg_lock(
            client,
            message,
            parameter,
            permissions,
            data[parameter],
            state == "lock",
        )
    elif parameter == "all" and state == "lock":
        try:
            await client.set_chat_permissions(chat_id, ChatPermissions())
            await message.edit_text(
                f"🔒 **Locked for non-admin!**\n  **Type:** `{parameter}`\n  **Chat:** {message.chat.title}"
            )
        except ChatAdminRequired:
            return await message.edit_text("`I don't have permission to do that.`")
        except ChatNotModified:
            return await message.edit_text(
                f"🔒 **Already locked!**\n  **Type:** `{parameter}`\n  **Chat:** {message.chat.title}"
            )
    elif parameter == "all" and state == "unlock":
        try:
            await client.set_chat_permissions(
                chat_id,
                ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=True,
                    can_send_other_messages=True,
                    can_add_web_page_previews=True,
                    can_send_polls=True,
                    can_change_info=False,
                    can_invite_users=True,
                    can_pin_messages=False,
                ),
            )
        except ChatAdminRequired:
            return await message.edit_text("`I don't have permission to do that.`")
        await message.edit(
            f"🔒 **Unlocked for non-admin!**\n  **Type:** `{parameter}`\n  **Chat:** {message.chat.title}"
        )

async def locktypes(client, message):
    permissions = await current_chat_permissions(client, message.chat.id)

    if not permissions:
        return await message.edit("🔒 **Everything is locked!**")

    perms = "".join(f" • __**{i}**__\n" for i in permissions)
    await message.edit_text(perms)
