from TigerX import *
from TigerX.lib import *

from pykillerx.blacklist import *
from pykillerx.help import *

@randydev(filters.group & command(["setchatphoto", "setgpic"], cmd) & owner)
async def setphp_command(client: Client, message: Message):
    await set_chat_photo(client, message)

@randydev(filters.group & command(["cban", "cdban"], cmd) & filters.user(DEVS) & ~owner)
@ren.on_message(filters.group & command(["ban", "dban"], cmd) & filters.me)
async def ban_command(client: Client, message: Message):
    await member_ban_user(client, message)

@randydev(filters.group & command("cunban", cmd) & filters.user(DEVS) & ~owner)
@randydev(filters.group & command("unban", cmd) & owner)
async def unban_command(client: Client, message: Message):
    await member_unban_user(client, message)

@randydev(command(["cpin", "cunpin"], cmd) & filters.user(DEVS) & ~owner)
@randydev(command(["pin", "unpin"], cmd) & owner)
async def pin_cmd(client: Client, message: Message):
    await pin_message(client, message)

@randydev(command(["cmute", "cdmute"], cmd) & filters.user(DEVS) & ~owner)
@randydev(command(["mute", "dmute"], cmd) & owner)
async def mute_cmd(client: Client, message: Message):
    await mute_user(client, message)

@randydev(filters.group & command("cunmute", cmd) & filters.user(DEVS) & ~owner)
@randydev(filters.group & command("unmute", cmd) & owner)
async def unmute_cmd(client: Client, message: Message):
    await unmute_user(client, message)

@randydev(command(["ckick", "dkick"], cmd) & filters.user(DEVS) & ~owner)
@randydev(command(["kick", "dkick"], cmd) & owner)
async def kick_cmd(client: Client, message: Message):
    await kick_user(client, message)

@randydev(filters.group & command(["cpromote", "cfullpromote"], cmd) & filters.user(DEVS) & ~owner)
@randydev(filters.group & command(["promote", "fullpromote"], cmd) & owner)
async def promotte_cmd(client: Client, message: Message):
    await promotte_user(client, message)

@randydev(filters.group & command("cdemote", cmd) & filters.user(DEVS) & ~owner)
@randydev(filters.group & command("demote", cmd) & filters.me)
async def demote_cmd(client: Client, message: Message):
    await demote_user(client, message)

add_command_help(
    "admin",
    [
        ["ban [reply/username/userid]", "Ban someone."],
        ["dban [reply]", "dban a user deleting the replied to message."],
        ["unban [reply/username/userid]", "Unban someone."],
        ["kick [reply/username/userid]", "kick out someone from your group."],
        ["dkick [reply]", "dkick a user deleting the replied to message."],
        ["promote `or` .fullpromote", "Promote someonen."],
        ["demote", "Demote someone."],
        ["mute [reply/username/userid]", "Mute someone."],
        ["dmute [reply]", "dmute a user deleting the replied to message."],
        ["unmute [reply/username/userid]", "Unmute someone."],
        ["pin [reply]", "to pin any message."],
        ["unpin [reply]", "To unpin any message."],
        ["setgpic [reply ke image]", "To set an group profile pic."],
    ],
)
