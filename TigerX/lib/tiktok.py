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

async def tiktok_downloader(client, message):
    ran = await message.reply_text("<code>Processing.....</code>")
    link = message.text.split(None, 1)[1] if len(message.command) !=1 else None
    if not link:
        await ran.edit_text("please for example the TikTok link here")
        return

    url = "https://tiktok-full-info-without-watermark.p.rapidapi.com/vid/index"
    querystring = {"url": link}

    headers = {"X-RapidAPI-Key": "ce36c261f1mshb4a0a55aaca548ep12c9f3jsn3d6761cb63fb", "X-RapidAPI-Host": "tiktok-full-info-without-watermark.p.rapidapi.com"}

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        data_response = response.json()
        try:
            music_urls = data_response["music"]
            video_urls = data_response["video"]
        except Exception as e:
            await ran.edit_text(f"Error request {e}")
            return
        
        video_responses = []
        for video_url in video_urls:
            video_responses.append(requests.get(video_url))
        music_responses = []
        for music_url in music_urls:
            music_responses.append(requests.get(music_url))
        
        if music_urls and video_urls:
            if all(response.ok for response in video_responses):
                send_video_file_path = "tigerx_userbot.mp4"
                with open(send_video_file_path, "wb") as f:
                    for response in video_responses:
                        f.write(response.content)
                await client.send_video(message.chat.id, video=send_video_file_path, reply_to_message_id=message.message_id)
                os.remove(send_video_file_path)
            elif all(response.ok for response in music_responses):
                send_audio_file_path = "tigerx_userbot.mp3"
                with open(send_audio_file_path, "wb") as f:
                    for response in music_responses:
                        f.write(response.content)
                await client.send_audio(message.chat.id, audio=send_audio_file_path, reply_to_message_id=message.message_id)
                os.remove(send_audio_file_path)
            else:
                await ran.edit_text("Error please try again")
        else:
            await ran.edit_text("Error please try again tiktok")
    else:
        await ran.edit_text("Error failed api TikTok")
