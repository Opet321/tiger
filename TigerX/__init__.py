import os
import datetime
from os import getenv
from pyrogram import Client
import asyncio
import logging
import sys
import time
from pathlib import Path
from logging.handlers import RotatingFileHandler
from typing import Any, Dict
from aiohttp import ClientSession
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime as dt
from aiohttp import ClientSession
# from pytgcalls import GroupCallFactory

StartTime = time.time()
START_TIME = dt.now()
CMD_HELP = {}
clients = []
ids = []

aiosession = ClientSession()

TEMP_SETTINGS: Dict[Any, Any] = {"PM_COUNT": {}, "PM_LAST_MSG": {}}
LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)

logging.getLogger("asyncio").setLevel(logging.CRITICAL)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("pyrogram.client").setLevel(logging.WARNING)
logging.getLogger("pyrogram.session.auth").setLevel(logging.CRITICAL)
logging.getLogger("pyrogram.session.session").setLevel(logging.CRITICAL)

LOGS = logging.getLogger(__name__)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)


import configparser

config = configparser.ConfigParser()
config.read("config.ini")

# pyrogram

API_ID = int(config.get("pyrogram", "api_id"))
API_HASH = config.get("pyrogram", "api_hash")
BOT_TOKEN = config.get("pyrogram", "bot_token")

# owner sudo 

OWNER_ID = int(config.get("admins", "owner_id"))

# new custom features

ALIVE_PIC = config.get("custom", "alive_pic")
ALIVE_TEXT = config.get("custom", "alive_text")
PACK_NAME = config.get("custom", "pack_name")
PREFIXES = config.get("custom", "prefixes")

# get api key & database sql

DB_URL = config.get("database", "db_url")

RMBG_API = config.get("apikey", "rmbg_api")
OPENAI_API = config.get("apikey", "openai_api")
DEEPAI_API = config.get("apikey", "deepai_api")
API_KEY_GOOGLE = config.get("apikey", "api_key_google")
SEARCH_ENGINE_ID = config.get("apikey", "search_engine_id")

# lyrics

SP_DC = config.get("spotify", "sp_dc")
SP_KEY = config.get("spotify", "sp_key")

# string pyrogram v1

STRING_SESSION1 = config.get("string_pyrogram", "string_session1")

SAVE_CONTENT = -1001624259885
MAX_MESSAGE_LENGTH = 4096

# this unsupported 

HEROKU_API_KEY = None 
HEROKU_APP_NAME = None 
GIT_TOKEN = None
BOT_VER = "0.3.35@build"
BRANCH = "dev"
REPO_URL = "https://github.com/TeamKillerX/TigerX-Userbot"
RAPI_API_KEY = "ce36c261f1mshb4a0a55aaca548ep12c9f3jsn3d6761cb63fb" # you can fork this // you can just change the api key here

if not BOT_TOKEN:
   print("PERINGATAN: BOT TOKEN TIDAK DITEMUKAN")

app = Client(
    name="app",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="TigerX/modules/bot"),
    in_memory=True,
)

if STRING_SESSION1:
   print("Client1: Found.. Starting..")
   client1 = Client(name="one", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION1, plugins=dict(root="TigerX/modules"))
   clients.append(client1)

# client = [client for client in[STRING_SESSION1, STRING_SESSION2, STRING_SESSION3]if client]
# for client in clients:
#    if not hasattr(client, "group_call"):
#        setattr(client, "group_call", GroupCallFactory(client).get_group_call())
