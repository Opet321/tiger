import os
from io import BytesIO
import math
import time
import traceback
import asyncio
import requests
import wget
from youtubesearchpython import SearchVideos
from datetime import datetime as dt
from pyrogram import filters, errors
from pyrogram.types import Message
from pykillerx.helper.dl_helpers import progress_for_pyrogram
from yt_dlp import YoutubeDL, utils
from pykillerx.helper.check_size import get_directory_size
from TigerX import *
from TigerX.lib import *

__PLUGIN__ = os.path.basename(__file__.replace(".py", ""))


ydl_search_opts = {
    "quiet": True,
    "skip_download": True,
    "forcetitle": True,
    "forceduration": True,
}

ytv_opts = {
    "verbose": True,
    "merge_output_format": "mkv",
    "geo_bypass": True,
    "outtmpl": "/root/TigerX/cache/ytv/%(id)s/%(title)s.%(ext)s",
    "restrictfilenames": True,
    "writeautomaticsub": True,
    "writedescription": True,
    "format": "(bestvideo[height>=720]+bestaudio/bestvideo+bestaudio)",
}

ytp_opts = {
    "verbose": True,
    "merge_output_format": "mkv",
    # outtmpl key updated later!
    "geo_bypass": True,
    "restrictfilenames": True,
    "writeautomaticsub": True,
    "writedescription": True,
    "format": "(bestvideo[height>=720]+bestaudio/bestvideo+bestaudio)",
}

yta_opts = {
    "verbose": True,
    "writethumbnail": True,
    "geo_bypass": True,
    "restrictfilenames": True,
    "outtmpl": "/root/TigerX/cache/yta/%(id)s/%(title)s.%(ext)s",
    "extractaudio": True,
    "audioformat": "mp3",
    "format": "(bestaudio[ext=m4a]/bestaudio)",
    # Embed Thumbnail
    'postprocessors': [
            {'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'},
            {'key': 'EmbedThumbnail',},]
}


async def time_length(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    if hour:
        return "%d:%02d:%02d" % (hour, minutes, seconds)
    elif minutes:
        return "%02d:%02d" % (minutes, seconds)
    else:
        return "%02d" % (seconds)


async def GetPlaylistInfo(link):
    with YoutubeDL(ydl_search_opts) as ydl:
        infoSearched = ydl.extract_info(link)
    title = infoSearched["title"]
    artist = infoSearched["uploader"]
    pid = infoSearched["id"]
    entries = infoSearched["entries"]
    return artist, title, pid, entries


async def GetVidInfo(link):
    with YoutubeDL(ydl_search_opts) as ydl:
        infoSearched = ydl.extract_info(link)
    duration = await time_length(infoSearched["duration"])
    timeS = infoSearched["duration"]
    title = infoSearched["title"]
    link_video = infoSearched["webpage_url"]
    artist = infoSearched["uploader"]
    vid = infoSearched["id"]
    return artist, duration, timeS, title, vid


async def ytv_dl(c, m):
    link = m.text.split(None, 1)[1]
    if not link:
       await m.reply_text("unsupported text use link youtube")
       return
    if "youtube.com" in link or "youtu.be" in link:
        await m.edit_text("<i>Getting Video Information...</i>")
        try:
            artist, duration, timeS, title, vid = await GetVidInfo(
                link
            )  # Get information about video!
        except utils.DownloadError:
            await m.edit_text("Could not extract video data, please try agin later!")
            return
        await m.edit_text(
            (
                f"<i>Downloading Video...</i>\n\n"
                f"<b>ID:</b> <code>{vid}</code>\n"
                f"<b>Uploader:</b> <code>{artist}</code>\n"
                f"<b>Duration:</b> <code>{duration}</code>\n"
                f"<b>Title:</b> <code>{title}</code>"
            )
        )
        dl_location = f"/root/TigerX/cache/ytv/{vid}/"
        try:
            with YoutubeDL(ytv_opts) as ydl:
                ydl.download([link])  # Use link in list!
                print("Downloaded!")
        except Exception:
            exc = traceback.format_exc()
            await m.reply_text(exc)

        files = os.listdir(dl_location)
        files.sort()
        for file in files:
            c_time = time.time()
            if file.endswith(".mkv"):
                await m.reply_document(
                    document=dl_location + file,
                    caption=f"<b>Uploader:</b> <code>{artist}</code>\n<b>Duration:</b> <code>{duration}</code>\n<b>Title:</b> <code>{title}</code>\n<b>Link:</b> {link}",
                    progress=progress_for_pyrogram,
                    progress_args=(f"Uploading <i>{file}</i>...", m, c_time),
                )
                continue
            await m.reply_document(
                document=dl_location + file,
                progress=progress_for_pyrogram,
                progress_args=(f"Uploading <i>{file}</i>...", m, c_time),
            )
        await m.delete()
    return


async def yta_dl(c, m):
    link = m.text.split(None, 1)[1]
    if not link:
       await m.reply_text("unsupported text use link youtube")
       return
    if "youtube.com" in link or "youtu.be" in link:
        await m.edit_text("<i>Getting Music Information...</i>")
        try:
            artist, duration, timeS, title, mid = await GetVidInfo(
                link
            )  # Get information about video!
        except utils.DownloadError:
            await m.edit_text("Could not extract video data, please try agin later!")
            return
        await m.edit_text(
            (
                f"<i>Downloading Music...</i>\n\n"
                f"<b>ID:</b> <code>{mid}</code>\n"
                f"<b>Uploader:</b> <code>{artist}</code>\n"
                f"<b>Duration:</b> <code>{duration}</code>\n"
                f"<b>Title:</b> <code>{title}</code>"
            )
        )
        dl_location = f"/root/TigerX/cache/yta/{mid}/"
        try:
            with YoutubeDL(yta_opts) as ydl:
                ydl.download([link])  # Use link in list!
                print("Downloaded Music...!")
        except Exception:
            exc = traceback.format_exc()
            await m.reply_text(exc)

        c_time = time.time()
        files = os.listdir(dl_location)
        files.sort()

        for file in files:
            await m.reply_audio(
                audio=dl_location + file,
                title=title,
                performer=artist,
                duration=int(timeS),
                caption=title,
                progress=progress_for_pyrogram,
                progress_args=(f"Uploading <i>{title}</i> ...", m, c_time),
            )
        await m.delete()
    return


async def ytp_dl(c, m):
    link = m.text.split(None, 1)[1]
    if not link:
       await m.reply_text("unsupported text use link youtube")
       return
    if "youtube.com" in link or "youtu.be" in link:
        await m.edit_text("<i>Getting Playlist Information...</i>")
        try:
            artist, title, pid, entries = await GetPlaylistInfo(
                link
            )  # Get information about video!
        except utils.DownloadError:
            await m.edit_text("Could not extract video data, please try agin later!")
            return

        dl_location = f"/root/TigerX/cache/ytp/{vid}/"
        num = 0  # To show download number

        Download_Text = (
            "<b>Downloading Playlist ({numbytotal}))</b>\n{progress}\n"
            "<b>Title:</b> {title}\n"
            "<b>Uploader:</b> {uploader}\n"
            "<b>Duration:</b> {duration}"
        )
        Ers = "Errors while Downloading:\n\n"
        total_vids = len(entries)

        for p in entries:
            ytp_opts["outtmpl"] = f"/root/TigerX/cache/ytp/{str(pid)}/%(title)s.%(ext)s"
            try:
                url = p["webpage_url"]
                with YoutubeDL(ytp_opts) as ydl:
                    ydl.download([url])  # Use link in list!
                print(f"Downloaded {p}!")
                num += 1
                title = p["title"]
                uploader = p["uploader"]
                duration = await time_length(p["duration"])
                percentage = (num / total_vids) * 100  # Percentage
                progress_str = (
                    "<b>[{0}{1}]</b>\n<b>Progress:</b> <i>{2}%</i>".format(
                        "".join(
                            ["●" for _ in range(math.floor(percentage / 5))]
                        ),
                        "".join(
                            [
                                "○"
                                for _ in range(20 - math.floor(percentage / 5))
                            ]
                        ),
                        round(percentage, 2),
                    )
                )
                try:
                    await m.edit_text(
                        Download_Text.format(
                            numbytotal=f"{num}/{total}",
                            progress=progress_str,
                            entries=total_vids,
                            title=title,
                            uploader=uploader,
                            duration=duration,
                        )
                    )
                except errors.MessageNotModified:
                    pass
            except Exception:
                exc = traceback.format_exc()
                Ers += exc + "\n"

        files = os.listdir(dl_location)
        files.sort()

        output = f"Playlist Downloaded to <code>{dl_location}</code> ({get_directory_size(os.path.abspath(dl_location))})\n\n"
        for file in files:
            output += f"• <code>{file}</code>\n ({get_directory_size(os.path.abspath(dl_location+file))})\n"

        output += f"\nTo upload, use <code> .batchup {dl_location}</code> to upload all contents of this folder!"

        await m.edit_text(output)
        if not Ers.endswith("Downloading:\n\n"):
            with BytesIO(str.encode(Ers)) as f:
                f.name = "ytp_errors.txt"
                await m.reply_document(document=f, caption="Download Errors!")
    return


async def yt_video(c, m):
    input_st = m.text
    input_str= input_st.split(" ", 1)[1]
    pablo = await m.edit_text("`Processing...`")
    if not input_str:
        await m.edit_text(
            "`Please Give Me A Valid Input. You Can Check Help Menu To Know More!`"
        )
        return
    await m.edit_text(f"`Searching {input_str} From Youtube. Please Wait.`")
    search = SearchVideos(str(input_str), offset=1, mode="dict", max_results=1)
    rt = search.result()
    result_s = rt["search_result"]
    url = result_s[0]["link"]
    vid_title = result_s[0]["title"]
    yt_id = result_s[0]["id"]
    uploade_r = result_s[0]["channel"]
    thumb_url = f"https://img.youtube.com/vi/{yt_id}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    downloaded_thumb = wget.download(thumb_url)
    opts = {
        "format": "best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
        "outtmpl": "%(id)s.mp4",
        "logtostderr": False,
        "quiet": True,
    }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url, download=True)
    except Exception as e:
        await m.edit_text(f"**Failed To Download** \n**Error :** `{str(e)}`")
        return
    c_time = time.time()
    file_path= f"{ytdl_data['id']}.mp4"
    capy = f"**Video Name ➠** `{vid_title}` \n**Requested For ➠** `{input_str}` \n**Channel ➠** `{uploade_r}` \n**Link ➠** `{url}`"
    await c.send_video(
        m.chat.id,
        video=open(file_path, "rb"),
        duration=int(ytdl_data["duration"]),
        file_name=str(ytdl_data["title"]),
        thumb=downloaded_thumb,
        caption=capy,
        supports_streaming=True,
    )
    await m.delete()
    for files in (downloaded_thumb, file_path):
        if files and os.path.exists(files):
            os.remove(files)
