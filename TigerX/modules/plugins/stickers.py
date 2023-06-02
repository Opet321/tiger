from TigerX import *
from TigerX.lib import *

from pykillerx.help import *

@randydev(command(["tikel", "kang", "steal"], cmd) & owner)
async def kang_command(client: Client, message: Message):
    await kang(client, message)

@randydev(command(["packinfo", "stickerinfo"], cmd) & owner)
async def packinfo_command(client: Client, message: Message):
    await packinfo(client, message)

@randydev(command(["sticker", "stickers"], cmd) & owner)
async def cb_sticker_command(client: Client, message: Message):
    await cb_sticker(client, message)

@randydev(command("tiny", cmd) & owner)
async def tinying_command(client: Client, message: Message):
    await tinying(client, message)

@randydev(command(["mmf", "memify"], cmd) & owner)
async def memify_command(client: Client, message: Message):
    await memify(client, message)

add_command_help(
    "sticker",
    [
        [
            "kang `reply` image",
            "Reply .kang To Sticker Or Image To Add To Sticker Pack.",
        ],
        [
            "kang [emoji] `or` .double [emoji]",
            "To add and custom emoji stickers to your sticker pack.",
        ],
        ["packinfo `or` .stickerinfo", "To Get Sticker Pack Information."],
        [
            "mtoi [reply ke sticker] or .getsticker [reply ke sticker]",
            "Reply to sticker to get sticker photo.",
        ],
        ["stickers [nama sticker]", "To find sticker packs."],
    ],
)


add_command_help(
    "memify",
    [
        [
            "mmf Top Text ; Bottom Text",
            "Reply To Message Sticker or Photo will be Converted to the specified meme text sticker.",
        ]
    ],
)


add_command_help(
    "tiny",
    [["tiny [reply ke photo/sticker]", "To Change the Sticker to be Small."]],
)


