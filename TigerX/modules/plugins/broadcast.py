from TigerX import *
from TigerX.lib import *

from pykillerx.help import *

@randydev(command(["gcast"], cmd) & owner)
async def gcast_command(client: Client, message: Message):
    await gcast_all(client, message)

@randydev(command(["gforward"], cmd) & owner)
async def gforward_command(client: Client, message: Message):
    await gforward_all(client, message)

@randydev(command(["guforward"], cmd) & owner)
async def guforward_command(client: Client, message: Message):
    await guforward_all(client, message)

@randydev(command(["gucast"], cmd) & owner)
async def gucast_command(client: Client, message: Message):
    await gucast_all(client, message)

add_command_help(
    "broadcast",
    [
        [
            "gcast [text/reply]",
            "Sending Global Broadcast messages to all groups you are logged into. (Can Send Media/Sticker)",
        ],
        [
            "gforward [reply]",
            "Sending Global Broadcast message to all group forwarded messages",
        ],
        [
            "guforward [reply]",
            "Sending Global Broadcast messages to all incoming Private Massages Forward",
        ],
        [
            "gucast [text/reply]",
            "Sending Global Broadcast messages to all incoming Private Massages / PCs. (Can Send Media/Sticker)",
        ],
    ],
)
