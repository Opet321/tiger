from TigerX import *
from TigerX.lib import *

from pykillerx.help import add_command_help

@randydev(command(["sg", "sangmata"], cmd) & owner)
async def sangmata_command(client: Client, message: Message):
    await sangmata_check(client, message)

add_command_help(
    "sangmata",
    [
        [
            "sg [reply/userid/username]",
            "Its help uh to find someone name history.",
        ]
    ],
)
