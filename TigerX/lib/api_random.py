# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#
# Developer Credits: @xtsea

import requests
from random import choice
from base64 import b64decode as kc
import base64
import aiohttp
import httpx

async def api_ceo_dog(client, message):
    ran = await message.reply_text("<code>Uploading.......</code>")
    API_DOG = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(API_DOG)
    if response.status_code == 200:
        data_ceo = response.json()
        try:
            photo_dog_url = data_ceo["message"]
        except Exception as e:
            await ran.edit_text(f"Error requests: {e}")
            return
        if photo_dog_url:
            await client.send_photo(message.chat.id, photo=photo_dog_url, reply_to_message_id=message.id)
        else:
            await ran.edit_text("Not founds")
    else:
        await ran.edit_text("Sorry, there was an error processing your request. Please try again later")
    try:
        await ran.delete()
    except Exception:
        pass

async def api_big_cat(client, message):
    ran = await message.reply_text("<code>Uploading.......</code>")
    API_BIG_CAT = "https://randombig.cat/roar.json"
    response = requests.get(API_BIG_CAT)
    if response.status_code == 200:
        data_cat = response.json()
        try:
            photo_cat_url = data_cat["url"]
        except Exception as e:
            await ran.edit_text(f"Error requests: {e}")
            return
        if photo_cat_url:
            await client.send_photo(message.chat.id, photo=photo_cat_url, reply_to_message_id=message.id)
        else:
            await ran.edit_text("Not founds")
    else:
        await ran.edit_text("Sorry, there was an error processing your request. Please try again later")
    try:
        await ran.delete()
    except Exception:
        pass

async def api_ceo_dog2(client, message):
    ran = await message.reply_text("<code>Uploading.......</code>")
    API_CEO_DOG2 = "https://random.dog/woof.json"
    response = requests.get(API_CEO_DOG2)
    if response.status_code == 200:
        data_dog2 = response.json()
        try:
            photo_dog2_url = data_dog2["url"]
        except Exception as e:
            await ran.edit_text(f"Error requests: {e}")
            return
        if photo_dog2_url:
            await client.send_photo(message.chat.id, photo=photo_dog2_url, reply_to_message_id=message.id)
        else:
            await ran.edit_text("Not founds")
    else:
        await ran.edit_text("Sorry, there was an error processing your request. Please try again later")
    try:
        await ran.delete()
    except Exception:
        pass

async def api_fox_ca(client, message):
    ran = await message.reply_text("<code>Uploading.......</code>")
    API_FOX_CA = "https://randomfox.ca/floof/"
    response = requests.get(API_FOX_CA)
    if response.status_code == 200:
        data_fox = response.json()
        try:
            photo_fox_url = data_fox["image"]
        except Exception as e:
            await ran.edit_text(f"Error requests: {e}")
            return
        if photo_fox_url:
            await client.send_photo(message.chat.id, photo=photo_fox_url, reply_to_message_id=message.id)
        else:
            await ran.edit_text("Not founds")
    else:   
        await ran.edit_text("Sorry, there was an error processing your request. Please try again later")
    try:
        await ran.delete()
    except Exception:
        pass


async def api_animechan_new(client, message):
    ran = await message.reply_text("<code>Processing anime quotes.......</code>")
    vercel_link = "https"
    vercel_name = "animechan.vercel.app"
    vercel_api = "api"
    vercel_random = "random"
    vercel_param = f"{vercel_link}://{vercel_name}/{vercel_api}/{vercel_random}"
    response = requests.get(vercel_param)
    if response.status_code == 200:
        data_animechan = response.json()
        try:
            anime_name = data_animechan["anime"]
            anime_character = data_animechan["character"]
            anime_quote = data_animechan["quote"]
        except Exception as e:
             await ran.edit_text(f"Error request {e}")
             return
        if anime_name and anime_character and anime_quote:
            animechan_full = f"<b>Anime name:</b> {anime_name}\n<b>Character:</b> {anime_character}\n<b>Quote:</b> {anime_quote}"
            await ran.edit_text(animechan_full)
        else: 
            await ran.edit_text("Not founds animechan")
    else:
        await ran.edit_text("Sorry, there was an error processing your request. Please try again later")


async def api_quotes_new(client, message):
    ran = await message.reply_text("<code>Processing quotes.......</code>")
    api_quotes_url = "https://api.breakingbadquotes.xyz/v1/quotes"
    response = requests.get(api_quotes_url)
    if response.status_code == 200:
        data_quotes = response.json()
        try:
            request_quotes = data_quotes[0]["quote"]
            request_author = data_quotes[0]["author"]
        except Exception as e:
             await ran.edit_text(f"Error request {e}")
             return
        if request_quotes and request_author:
            correct_this_quote = ""
            correct_this_quote += f"<b>Quote:</b> {request_quotes}\n"
            correct_this_quote += f"<b>Author:</b> {request_author}\n"
            await ran.edit_text(correct_this_quote)
        else: 
            await ran.edit_text("failed to quote")
    else:
        await ran.edit_text("Sorry, there was an error processing your request. Please try again later")

async def api_waifu_main(client, message):
    ran = await message.reply_text("<code>Processing.......</code>")
    LIST_SFW_JPG = ["neko", "waifu", "megumin"]
    waifu_link = "https"
    waifu_api = "api.waifu.pics"
    waifu_types = "sfw"
    waifu_category = choice(LIST_SFW_JPG)
    waifu_param = f"{waifu_link}://{waifu_api}/{waifu_types}/{waifu_category}"
    response = requests.get(waifu_param)
    if response.status_code == 200:
        data_waifu = response.json()
        try:
            waifu_image_url = data_waifu["url"]
        except Exception as e:
            await ran.edit_text(f"Error request {e}")
            return
        if waifu_image_url:
            await client.send_photo(message.chat.id, photo=waifu_image_url, reply_to_message_id=message.id)
        else:
            await ran.edit_text("Not founds animechan")
    else:
        await ran.edit_text("Sorry, there was an error processing your request. Please try again later")
    try:
        await ran.delete()
    except Exception:
        pass

async def randomuser(client, message):
    ran = await message.reply_text("<code>Processing.......</code>")
    url_random_user = "https://randomuser.me/api"
    response = requests.get(url_random_user)
    if response.status_code == 200:
        data_random = response.json()
        try:
            gender = data_random["results"][0]["gender"]
            name = data_random["results"][0]["name"]
            location = data_random["results"][0]["location"]
            email = data_random["results"][0]["email"]
            login = data_random["results"][0]["login"]
            dob = data_random["results"][0]["dob"]
            registered = data_random["results"][0]["registered"]
            phone = data_random["results"][0]["phone"]
            cell = data_random["results"][0]["cell"]
            picture = data_random["results"][0]["picture"]["large"]
        except Exception as e:
            await ran.edit_text(f"Error request {e}")
            return
        if gender and name and location and email and login and dob and registered and phone and cell and picture:
            random_results = ""
            random_results += f"<b>Name:</b> {name['title']} {name['first']} {name['last']}\n"
            random_results += f"<b>Gender:</b> {gender}\n"
            random_results += f"<b>Location:</b> {location['street']['number']} {location['street']['name']}, {location['city']}, {location['state']}, {location['country']} {location['postcode']}\n"
            random_results += f"<b>Email:</b> {email}\n"
            random_results += f"<b>Username:</b> {login['username']}\n"
            random_results += f"<b>Password:</b> {login['password']}\n"
            random_results += f"<b>Date of birth:</b> {dob['date'].split('T')[0]}\n"
            random_results += f"<b>Registered:</b> {registered['date'].split('T')[0]}\n"
            random_results += f"<b>Phone:</b> {phone}\n"
            random_results += f"<b>Cell:</b> {cell}\n"
            await client.send_photo(message.chat.id, photo=picture, caption=random_results, reply_to_message_id=message.id)
        else:
            await ran.edit_text("Sorry, there was an error processing your request. Please try again later")
    else:
        await ran.edit_text("Sorry, there was an error processing your request. Please try again later")
    try:
        await ran.delete()
    except Exception:
        pass
  
# DO NOT SHARE THIS MODULE 
# THIS DANGER IS TRACKED

async def hacker_lacak_target(client, message):
    apikey = kc("M0QwN0UyRUFBRjU1OTQwQUY0NDczNEMzRjJBQzdDMUE=").decode("utf-8")
    ran = await message.reply_text("<code>Processing.......</code>")
    ipddres = message.text.split(None, 1)[1] if len(message.command) != 1 else None
    if not ipddres:
        await ran.edit_text("Example: <code>+ip your ip address here : 1592.401.xxx</code>")
        return

    if not apikey:
        await ran.edit_text("Missing apikey ip location")
        return

    location_link = "https"
    location_api = "api.ip2location.io"
    location_key = f"key={apikey}"
    location_search = f"ip={ipddres}"
    location_param = f"{location_link}://{location_api}/?{location_key}&{location_search}"
    response = requests.get(location_param)
    if response.status_code == 200:
        data_location = response.json()
        try:
            location_ip = data_location["ip"]
            location_code = data_location["country_code"]
            location_name = data_location["country_name"]
            location_region = data_location["region_name"]
            location_city = data_location["city_name"]
            location_zip = data_location["zip_code"]
            location_zone = data_location["time_zone"]
            location_card = data_location["as"]
        except Exception as e:
            await ran.edit_text(f"Error request {e}")
            return
        if location_ip and location_code and location_name and location_region and location_city and location_zip and location_zone and location_card:
            location_target = ""
            location_target += f"<b>IP Address:</b> {location_ip}\n"
            location_target += f"<b>Country code:</b> {location_code}\n"
            location_target += f"<b>Country name:</b> {location_name}\n"
            location_target += f"<b>Region name:</b> {location_region}\n"
            location_target += f"<b>City name:</b> {location_city}\n"
            location_target += f"<b>Zip code:</b> {location_zip}\n"
            location_target += f"<b>Time Zone:</b> {location_zone}\n"
            location_target += f"<b>Data card:</b> {location_card}\n"
            await ran.edit_text(location_target)
        else:
            await ran.edit_text("Not data ip address")
    else:
        await ran.edit_text("Sorry, there was an error processing your request. Please try again later")


async def whois_domain_target(client, message):
    apikey = base64.b64decode("M0QwN0UyRUFBRjU1OTQwQUY0NDczNEMzRjJBQzdDMUE=").decode("utf-8")
    ran = await message.reply_text("<code>Processing.......</code>")
    domain_text = message.text.split(None, 1)[1] if len(message.command) != 1 else None
    if not domain_text:
        await ran.edit_text("Example: <code>+your can get ip domain</code>")
        return

    if not apikey:
        await ran.edit_text("Missing apikey ip domain")
        return

    url_api_domain = f"https://api.ip2whois.com/v2?key={apikey}&domain={domain_text}"
    whois_domain = ""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url_api_domain) as response:
                if response.status == 200:
                    data_domain = await response.json()
                    domain_domain = data_domain.get("domain")
                    domain_domainid = data_domain.get("domain_id")
                    domain_status = data_domain.get("status")
                    domain_create_date = data_domain.get("create_date")
                    domain_update_date = data_domain.get("update_date")
                    domain_expire_date = data_domain.get("expire_date")
                    domain_ages = data_domain.get("domain_age")
                    domain_server = data_domain.get("whois_server")
                    domain_name = data_domain.get("name")
                    domain_organization = data_domain.get("organization")
                    domain_addres = data_domain.get("street_address")
                    domain_city = data_domain.get("city")
                    domain_region = data_domain.get("region")
                    domain_country = data_domain.get("country")
                    domain_email = data_domain.get("email")
                    domain_zip = data_domain.get("zip_code")
                    domain_phone = data_domain.get("phone")
                    domain_nameservers = data_domain.get("nameservers")

                    if domain_domain and domain_domainid and domain_status and domain_create_date and domain_update_date and domain_expire_date and domain_ages and domain_server and domain_name and domain_organization and domain_addres and domain_city and domain_region and domain_country and domain_email and domain_zip and domain_phone and domain_nameservers:
                        whois_domain += f"<b>Domain:</b> {domain_domain}\n"
                        whois_domain += f"<b>Domain ID:</b> {domain_domainid}\n"
                        whois_domain += f"<b>Status:</b> {domain_status}\n"
                        whois_domain += f"<b>Create date:</b> {domain_create_date}\n"
                        whois_domain += f"<b>Update date:</b> {domain_update_date}\n"
                        whois_domain += f"<b>Expire date:</b> {domain_expire_date}\n"
                        whois_domain += f"<b>Age:</b> {domain_ages}\n"
                        whois_domain += f"<b>Whois_server:</b> {domain_server}\n"
                        whois_domain += f"<b>Name:</b> {domain_name}\n"
                        whois_domain += f"<b>Organization:</b> {domain_organization}\n"
                        whois_domain += f"<b>Street address:</b> {domain_addres}\n"
                        whois_domain += f"<b>City:</b> {domain_city}\n"
                        whois_domain += f"<b>Region:</b> {domain_region}\n"
                        await ran.edit_text(whois_domain)
                    else:
                        await ran.edit_text("No data for this domain.")
                else:
                    await ran.edit_text("Error: could not fetch WHOIS information.")
    except Exception as e:
        await ran.edit_text(f"Error: {str(e)}")


async def api_movie_info(client, message):
    ran = await message.reply_text("<code>Processing.....</code>")
    search = message.text.split(None, 1)[1] if len(message.command) != 1 else None
    if not search:
        await ran.edit_text("please, for example, find a movie")
        return
    type = search
    apikey = "212089e4" # don't share this by @xtsea 
    api_url = f"http://www.omdbapi.com/?apikey={apikey}&s={type}" # parameter check : http://www.omdbapi.com/
    response = requests.get(api_url)
    if response.status_code == 200:
        data_movie = response.json()
        try:
            search_title = data_movie["Search"][0]["Title"] # using [0] empty something 
            year_movie = data_movie["Search"][0]["Year"]
            imdb_code = data_movie["Search"][0]["imdbID"]
            movies = data_movie["Search"][0]["Type"]
            image_movie_url = data_movie["Search"][0]["Poster"]
        except Exception as e:
            await ran.edit_text(f"Error request {e}")
            return
        if search_title and year_movie and imdb_code and movies and image_movie_url:
            search_text = ""
            search_text += f"<b>Film title :</b> {search_title}\n"
            search_text += f"<b>Year :</b> {year_movie}\n"
            search_text += f"<b>Imdb ID :</b> {imdb_code}\n"
            search_text += f"<b>Type :</b> {movies}\n"
            await client.send_photo(message.chat.id, photo=image_movie_url, caption=search_text, reply_to_message_id=message.id)
        else:
            await ran.edit_text("No data for this Movies.")
    else:
        await ran.edit_text("Error: could not find Movies.")
    try:
        await ran.delete()
    except Exception:
        pass
