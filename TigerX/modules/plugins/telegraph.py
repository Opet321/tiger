from TigerX import *
from TigerX.lib import *

from pykillerx.help import *

@randydev(command(["tg", "telegraph"], cmd) & owner)
async def telegraph_command(client: Client, message: Message):
    await telegraph_upload(client, message)

add_command_help(
    "telegraph",
    [
        [
            "telegraph or .tg",
            "Reply to messages or media to upload them to the telegraph.",
        ]
    ],
)
