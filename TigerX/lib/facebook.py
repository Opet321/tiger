# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#
# Developer Credits: @xtsea

from TigerX import *
from TigerX.lib import *
import requests
import os
import time
from tqdm import tqdm

async def facebook_downloader(client, message):
    ran = await message.reply_text("<code>Processing.....</code>")
    link = message.text.split(" ", 1)[1] if len(message.command) != 1 else None
    if not link:
        await ran.edit_text("Please provide a valid video link from Facebook.")
        return

    url = "https://facebook-video-and-reel-downloader.p.rapidapi.com/"
    querystring = {"url": link}

    headers = {"X-RapidAPI-Key": "ce36c261f1mshb4a0a55aaca548ep12c9f3jsn3d6761cb63fb", "X-RapidAPI-Host": "facebook-video-and-reel-downloader.p.rapidapi.com"}
    response = requests.request("GET", url, headers=headers, params=querystring)

    if response.status_code == 200:
        data_facebook = response.json()
        try:
            facebook_hd = data_facebook["sd"]
        except Exception as e:
            await ran.edit_text(f"Error request {e}")
            return

        progress_bar = ""
        facebook_url = requests.get(facebook_hd, stream=True)
        if facebook_hd:
            if facebook_url:
                total_size = int(facebook_url.headers.get("content-length", 0))
                send_video_path = "tigerx_userbot.mp4"
                with open(send_video_path, "wb") as f:
                    bytes_received = 0
                    progress = 0
                    for data in facebook_url.iter_content(chunk_size=4096):
                        f.write(data)
                        bytes_received += len(data)
                        progress = int(bytes_received / total_size * 100)
                        new_progress_bar = f"Downloading {progress}% of {total_size}"
                        if new_progress_bar != progress_bar:
                            await ran.edit_text(new_progress_bar)
                            progress_bar = new_progress_bar
                await client.send_video(message.chat.id, video=send_video_path, reply_to_message_id=message.id)
                os.remove(send_video_path)   
            else:
                await ran.edit_text("Error please try again")
        else:
            await ran.edit_text("Error please try again facebook")
    else:
        await ran.edit_text("Failed to api facebook")
    try:
        await ran.delete()
    except Exception:
        pass
