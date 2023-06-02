import asyncio
import socket
import sys
import os
from re import sub
from time import time
import aiohttp
import requests
import asyncio
from os import getenv
import shlex
import textwrap
from typing import Tuple

from PIL import Image, ImageDraw, ImageFont

from pyrogram import enums
from datetime import datetime as dt
from os import environ, execle, path, remove

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message

from TigerX import *
from TigerX.lib import *

from pykillerx import *
from pykillerx.helper import *
from pykillerx.blacklist import *
from pykillerx.help import *

HAPP = None

XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(HEROKU_API_KEY),
    "https",
    str(HEROKU_APP_NAME),
    "HEAD",
    "main",
]

BASE = "https://batbin.me/"

def get_arg(message: Message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    return "" if not " ".join(split[1:]).strip() else " ".join(split[1:])


async def post(url: str, *args, **kwargs):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, *args, **kwargs) as resp:
            try:
                data = await resp.json()
            except Exception:
                data = await resp.text()
        return data


async def PasteBin(text):
    resp = await post(f"{BASE}api/v2/paste", data=text)
    if not resp["success"]:
        return
    return BASE + resp["message"]

if GIT_TOKEN:
    GIT_USERNAME = REPO_URL.split("com/")[1].split("/")[0]
    TEMP_REPO = REPO_URL.split("https://")[1]
    UPSTREAM_REPO = f"https://{GIT_USERNAME}:{GIT_TOKEN}@{TEMP_REPO}"
UPSTREAM_REPO_URL = UPSTREAM_REPO if GIT_TOKEN else REPO_URL
__file__ = os.path.abspath(__file__)

requirements_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "requirements.txt"
)


def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "TigerX"])

async def is_heroku():
    return "heroku" in socket.getfqdn()

async def bash(cmd):
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    err = stderr.decode().strip()
    out = stdout.decode().strip()
    return out, err


async def gen_chlog(repo, diff):
    d_form = "%d/%m/%y"
    return "".join(
        f"• [{c.committed_dt.strftime(d_form)}]: {c.summary} <{c.author}>\n"
        for c in repo.iter_commits(diff)
    )


async def updateme_requirements():
    reqs = str(requirements_path)
    try:
        process = await asyncio.create_subprocess_shell(
            " ".join([sys.executable, "-m", "pip", "install", "-r", reqs]),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        await process.communicate()
        return process.returncode
    except Exception as e:
        return repr(e)


async def upstream(client, message):
    status = await message.edit_text("`Checking for Updates, Wait a Moment...`")
    conf = get_arg(message)
    off_repo = UPSTREAM_REPO_URL
    try:
        txt = (
            "**Update Could Not Continue Due "
            + "Several ERROR Occurred**\n\n**LOGTRACE:**\n"
        )
        repo = Repo()
    except NoSuchPathError as error:
        await status.edit(f"{txt}\n**Directory** `{error}` **Can not be found.**")
        repo.__del__()
        return
    except GitCommandError as error:
        await status.edit(f"{txt}\n**Early failure!** `{error}`")
        repo.__del__()
        return
    except InvalidGitRepositoryError:
        repo = Repo.init()
        origin = repo.create_remote("upstream", off_repo)
        origin.fetch()
        repo.create_head(
            BRANCH,
            origin.refs[BRANCH],
        )
        repo.heads[BRANCH].set_tracking_branch(origin.refs[BRANCH])
        repo.heads[BRANCH].checkout(True)
    ac_br = repo.active_branch.name
    if ac_br != BRANCH:
        await status.edit(
            f"**[UPDATER]:** `Looks like you are using your own custom branch ({ac_br}). in that case, Updater is unable to identify which branch is to be merged. please checkout to main branch`"
        )
        repo.__del__()
        return
    try:
        repo.create_remote("upstream", off_repo)
    except BaseException:
        pass
    ups_rem = repo.remote("upstream")
    ups_rem.fetch(ac_br)
    changelog = await gen_chlog(repo, f"HEAD..upstream/{ac_br}")
    if "deploy" not in conf:
        if changelog:
            changelog_str = f"**Update Available For Branch [{ac_br}]:\n\nCHANGELOG:**\n\n`{changelog}`"
            if len(changelog_str) <= 4096:
                return await status.edit(
                    f"{changelog_str}\n**Type** `.update deploy` **To Update TigerX.**",
                    disable_web_page_preview=True,
                )
            await status.edit("**Changelog too big, sent as file.**")
            with open("output.txt", "w+") as file:
                file.write(changelog_str)
            await client.send_document(
                message.chat.id,
                "output.txt",
                caption="**Type** `.update deploy` **To Update TigerX.**",
                reply_to_message_id=status.id,
            )
            remove("output.txt")
        else:
            await status.edit(
                f"\n`Your BOT is`  **up-to-date**  `with branch`  **[{ac_br}]**\n",
                disable_web_page_preview=True,
            )
            repo.__del__()
            return
    if HEROKU_API_KEY is not None:
        import heroku3

        heroku = heroku3.from_key(HEROKU_API_KEY)
        heroku_applications = heroku.apps()
        if not HEROKU_APP_NAME:
            await status.edit(
                "`Please set up the HEROKU_APP_NAME variable to be able to update KillerXBase.`"
            )
            repo.__del__()
            return
        heroku_app = next(
            (
                app
                for app in heroku_applications
                if app.name == HEROKU_APP_NAME
            ),
            None,
        )
        if heroku_app is None:
            await status.edit(
                f"{txt}\n`Invalid Heroku credentials for updating KillerXBase dyno.`"
            )
            repo.__del__()
            return
        await status.edit(
            "`[HEROKU]: DarkWeb Deploy Update is in Progress...`"
        )
        ups_rem.fetch(ac_br)
        repo.git.reset("--hard", "FETCH_HEAD")
        heroku_git_url = heroku_app.git_url.replace(
            "https://", f"https://api:{HEROKU_API_KEY}@"
        )
        if "heroku" in repo.remotes:
            remote = repo.remote("heroku")
            remote.set_url(heroku_git_url)
        else:
            remote = repo.create_remote("heroku", heroku_git_url)
        try:
            remote.push(refspec="HEAD:refs/heads/main", force=True)
        except GitCommandError:
            pass
        await status.edit(
            "`DarkWeb Successfully Updated! DarkWeb can be used again.`"
        )
    else:
        try:
            ups_rem.pull(ac_br)
        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")
        await updateme_requirements()
        await status.edit(
            "`TigerX Successfully Updated! TigerX can be used again.`",
        )
        args = [sys.executable, "-m", "TigerX"]
        execle(sys.executable, *args, environ)
        return


async def updatees(client, message):
    if await is_heroku():
        if HAPP is None:
            return await message.edit_text(
                "Make sure your HEROKU_API_KEY and HEROKU_APP_NAME are configured correctly in heroku config vars",
            )
    response = await message.edit_text("Checking for available updates...")
    try:
        repo = Repo()
    except GitCommandError:
        return await response.edit("Git Command Error")
    except InvalidGitRepositoryError:
        return await response.edit("Invalid Git Repsitory")
    to_exc = f"git fetch origin {BRANCH} &> /dev/null"
    await bash(to_exc)
    await asyncio.sleep(7)
    verification = ""
    REPO_ = repo.remotes.origin.url.split(".git")[0]  # main git repository
    for checks in repo.iter_commits(f"HEAD..origin/{BRANCH}"):
        verification = str(checks.count())
    if verification == "":
        return await response.edit("Bot is up-to-date!")
    ordinal = lambda format: "%d%s" % (
        format,
        "tsnrhtdd"[(format // 10 % 10 != 1) * (format % 10 < 4) * format % 10 :: 4],
    )
    updates = "".join(
        f"<b>➣ #{info.count()}: [{info.summary}]({REPO_}/commit/{info}) by -> {info.author}</b>\n\t\t\t\t<b>➥ Commited on:</b> {ordinal(int(dt.fromtimestamp(info.committed_date).strftime('%d')))} {dt.fromtimestamp(info.committed_date).strftime('%b')}, {dt.fromtimestamp(info.committed_date).strftime('%Y')}\n\n"
        for info in repo.iter_commits(f"HEAD..origin/{BRANCH}")
    )
    _update_response_ = "<b>A new update is available for the Bot!</b>\n\n➣ Pushing Updates Now</code>\n\n**<u>Updates:</u>**\n\n"
    _final_updates_ = _update_response_ + updates
    if len(_final_updates_) > 4096:
        url = await PasteBin(updates)
        nrs = await response.edit(
            f"<b>A new update is available for the Bot!</b>\n\n➣ Pushing Updates Now</code>\n\n**<u>Updates:</u>**\n\n[Click Here to checkout Updates]({url})"
        )
    else:
        nrs = await response.edit(_final_updates_, disable_web_page_preview=True)
    await bash("git stash &> /dev/null && git pull")
    if await is_heroku():
        try:
            await response.edit(
                f"{nrs.text}\n\nBot was updated successfully on Heroku! Now, wait for 2 - 3 mins until the bot restarts!"
            )
            await bash(
                f"{XCB[5]} {XCB[7]} {XCB[9]}{XCB[4]}{XCB[0]*2}{XCB[6]}{XCB[4]}{XCB[8]}{XCB[1]}{XCB[5]}{XCB[2]}{XCB[6]}{XCB[2]}{XCB[3]}{XCB[0]}{XCB[10]}{XCB[2]}{XCB[5]} {XCB[11]}{XCB[4]}{XCB[12]}"
            )
            return
        except Exception as err:
            return await response.edit(f"{nrs.text}\n\nERROR: <code>{err}</code>")
    else:
        await bash("pip3 install -r requirements.txt")
        restart()
        sys.exit()
