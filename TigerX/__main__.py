import asyncio
import importlib
from pyrogram import Client, idle
from pyrogram.types import *
from pyrogram import *
from TigerX.modules import ALL_MODULES
from TigerX import clients, ids, app, aiosession
from pykillerx.helper import *


async def start_bot():
    await app.start()
    print("LOG: Mendirikan Bot token Booting..")
    for all_module in ALL_MODULES:
        importlib.import_module(f"TigerX.modules{all_module}")
        print(f"Successfully Imported {all_module} 🛠️")
    for cli in clients:
        try:
            await cli.start()
            ex = await cli.get_me()
            await join(cli)
            try:
                await cli.send_photo("me", photo=LOG_ALIVE, caption=ALIVE_ONLINE)
            except BaseException:
                pass
            print(f"Started {ex.first_name} ☠️")
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")
    await idle()
    await aiosession.close()

event_policy = asyncio.get_event_loop_policy()
event_loop = event_policy.get_event_loop()
asyncio.set_event_loop(event_loop)
event_loop.run_until_complete(start_bot())
