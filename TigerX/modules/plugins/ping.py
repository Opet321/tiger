from TigerX.lib import *

from pykillerx import *
from pykillerx.help import add_command_help

@randydev(command(["speedtest"], cmd) & owner)
async def speed_test_command(client: Client, message: Message):
    await speed_test(client, message)

@randydev(command("kping", cmd) & owner)
async def kping_command(client: Client, message: Message):
    await kping(client, message)

@randydev(command("ping", cmd) & owner)
async def ping_command(client: Client, message: Message):
    await ping(client, message)

@randydev(command(["fck"], cmd) & owner)
async def fuck_command(client: Client, message: Message):
    await ping_fuck(client, message)


add_command_help(
    "ping",
    [["ping or .kping", "Check bot alive or not."], ["fck", "Check fucking."]],
)
