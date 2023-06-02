import asyncio 
from pykillerx.helper.basic import *
from pykillerx.helper.hacking import *
from pykillerx.helper import *
from TigerX import *
from TigerX.lib import *

async def sangmata_check(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        user_id = message.reply_to_message.from_user.id
    else:
        try:
            user_id = int(message.text.split()[1])
        except (ValueError, IndexError):
            await message.reply_text("`Please specify a valid user ID!`")
            return
    bot = "@SangMata_beta_bot"
    await client.send_message(bot, f"{user_id}")
    anak_bocah_coding = await message.reply_text("`Whacking I check you`")
    await asyncio.sleep(3)
    async for stalk in client.search_messages(bot, limit=1):
        if not stalk:
            await message.reply_text("**This person has never changed their name**")
        else:
            await client.send_message(message.chat.id, stalk.text, reply_to_message_id=message.id)
            await anak_bocah_coding.delete()
        return
    await message.reply_text("**Timed out while searching for messages**")

# end this
