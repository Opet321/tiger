# Code Based by @RendyProjects

from TigerX import *
from TigerX.lib import *

from pykillerx.help import *

@randydev(command(["notes"], cmd) & owner)
async def list_notes_command(client: Client, message: Message):
    await list_notes(client, message)

@randydev(command(["delete"], cmd) & owner)
async def remove_notes_command(client: Client, message: Message):
    await remove_notes(client, message)

@randydev(command(["save"], cmd) & owner)
async def save_notes_command(client: Client, message: Message):
    await save_note(client, message)

@randydev(command(["get"], cmd) & owner)
async def get_notes_command(client: Client, message: Message):
    await call_notes(client, message)

add_command_help(
    "notes",
    [
        ["save [name and reply to message]", "to save notes"],
        ["get [name]", "to call notes"],
        ["delete [name]", "to delete a note"],
        ["notes", "to display a list of notes"],
    ],
)
