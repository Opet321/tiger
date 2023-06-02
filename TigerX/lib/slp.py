# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#

from TigerX import *
from ..lib import *

from random import choice


RUN_STRINGS = [
    "Where do you think you're going?",
    "Huh? what? did they get away?",
    "ZZzzZZzz... Huh? what? oh, just them again, nevermind.",
    "Get back here!",
    "Not so fast...",
    "Look out for the wall!",
    "Don't leave me alone with them!!",
    "You run, you die.",
    "Jokes on you, I'm everywhere",
    "You're gonna regret that...",
    "You could also try /kickme, I hear that's fun.",
    "Go bother someone else, no-one here cares.",
    "You can run, but you can't hide.",
    "Is that all you've got?",
    "I'm behind you...",
    "You've got company!",
    "We can do this the easy way, or the hard way.",
    "You just don't get it, do you?",
    "Yeah, you better run!",
    "Please, remind me how much I care?",
    "I'd run faster if I were you.",
    "That's definitely the droid we're looking for.",
    "May the odds be ever in your favour.",
    "Famous last words.",
    "And they disappeared forever, never to be seen again.",
    '"Oh, look at me! I\'m so cool, I can run from a bot!" - this person',
    "Yeah yeah, just tap /kickme already.",
    "Here, take this ring and head to Mordor while you're at it.",
    "Legend has it, they're still running...",
    "Unlike Harry Potter, your parents can't protect you from me.",
    "Fear leads to anger. Anger leads to hate. Hate leads to suffering. If you keep running in fear, you might "
    "be the next Vader.",
    "Multiple calculations later, I have decided my interest in your shenanigans is exactly 0.",
    "Legend has it, they're still running.",
    "Keep it up, not sure we want you here anyway.",
    "You're a wiza- Oh. Wait. You're not Harry, keep moving.",
    "NO RUNNING IN THE HALLWAYS!",
    "Hasta la vista, baby.",
    "Who let the dogs out?",
    "It's funny, because no one cares.",
    "Ah, what a waste. I liked that one.",
    "Frankly, my dear, I don't give a damn.",
    "My milkshake brings all the boys to yard... So run faster!",
    "You can't HANDLE the truth!",
    "A long time ago, in a galaxy far far away... Someone would've cared about that. Not anymore though.",
    "Hey, look at them! They're running from the inevitable banhammer... Cute.",
    "Han shot first. So will I.",
    "What are you running after, a white rabbit?",
    "As The Doctor would say... RUN!",
]


SLAP_TEMPLATES = [
    "{user2} was shot by {user1}.",
    "{user2} walked into a cactus while trying to escape {user1}.",
    "{user2} drowned whilst trying to escape {user1}.",
    "{user2} fell into a patch of cacti.",
    "{user2} went up in flames.",
    "{user2} burned to death.",
    "{user2} was burnt to a crisp whilst fighting {user1}.",
    "{user2} was struck by lightning.",
    "{user2} was slain by {user1}.",
    "{user2} was killed by magic.",
    "{user2} starved to death.",
    "{user2} fell out of the world.",
    "{user2} was knocked into the void by {user1}.",
    "{user2}'s bones are scraped clean by the desolate wind.",
    "{user2} fainted.",
    "{user2} is out of usable Pokemon! {user2} whited out!.",
    "{user2} is out of usable Pokemon! {user2} blacked out!.",
    "{user2} says goodbye to this cruel world.",
    "{user2} got rekt.",
    "{user2} was sawn in half by {user1}.",
    "{user2}'s melon was split by {user1}.",
    "{user2} was sliced and diced by {user1}.",
    "{user2}'s death put another notch in {user1}'s axe.",
    "{user2} died from {user1}'s mysterious tropical disease.",
    "{user2} played hot-potato with a grenade.",
    "{user2} was knifed by {user1}.",
    "{user2} ate a grenade.",
    "{user2} is what's for dinner!",
    "{user2} was terminated by {user1}.",
    "{user2} was shot before being thrown out of a plane.",
    "{user2} has encountered an error.",
    "{user2} died and reincarnated as a goat.",
    "{user1} threw {user2} off a building.",
    "{user2} got a premature burial.",
    "{user1} spammed {user2}'s email.",
    "{user1} hit {user2} with a small, interstellar spaceship.",
    "{user1} put {user2} in check-mate.",
    "{user1} RSA-encrypted {user2} and deleted the private key.",
    "{user1} put {user2} in the friendzone.",
    "{user1} slaps {user2} with a DMCA takedown request!",
    "{user2} died of hospital gangrene.",
    "{user2} got a house call from Doctor {user1}.",
    "{user1} beheaded {user2}.",
    "{user2} got stoned...by an angry mob.",
    "{user1} sued the pants off {user2}.",
    "{user2} was one-hit KO'd by {user1}.",
    "{user1} sent {user2} down the memory hole.",
    "{user2} was a mistake. - '{user1}' ",
    "{user1} checkmated {user2} in two moves.",
    "{user2} was made redundant.",
    "{user1} {hits} {user2} with a bat!.",
    "{user1} {hits} {user2} with a Taijutsu Kick!.",
    "{user1} {hits} {user2} with X-Gloves!.",
    "{user1} {hits} {user2} with a Jet Punch!.",
    "{user1} {hits} {user2} with a Jet Pistol!.",
    "{user1} {hits} {user2} with a United States of Smash!.",
    "{user1} {hits} {user2} with a Detroit Smash!.",
    "{user1} {hits} {user2} with a Texas Smash!.",
    "{user1} {hits} {user2} with a California Smash!.",
    "{user1} {hits} {user2} with a New Hampshire Smash!.",
    "{user1} {hits} {user2} with a Missouri Smash!.",
    "{user1} {hits} {user2} with a Carolina Smash!.",
    "{user1} {hits} {user2} with a King Kong Gun!.",
    "{user1} {hits} {user2} with a baseball bat - metal one.!.",
    "*Serious punches {user2}*.",
    "*Normal punches {user2}*.",
    "*Consecutive Normal punches {user2}*.",
    "*Two Handed Consecutive Normal Punches {user2}*.",
    "*Ignores {user2} to let them die of embarassment*.",
    "*points at {user2}* What's with this sassy... lost child?.",
    "*Hits {user2} with a Fire Tornado*.",
    "{user1} pokes {user2} in the eye !",
    "{user1} pokes {user2} on the sides!",
    "{user1} pokes {user2}!",
    "{user1} pokes {user2} with a needle!",
    "{user1} pokes {user2} with a pen!",
    "{user1} pokes {user2} with a stun gun!",
    "{user2} is secretly a Furry!.",
    "Hey Everybody! {user1} is asking me to be mean!",
    "( ･_･)ﾉ⌒●~* (･.･;) <-{user2}",
    "Take this {user2}\n(ﾉﾟДﾟ)ﾉ ))))●~* ",
    "Here {user2} hold this\n(｀・ω・)つ ●~＊",
    "( ・_・)ノΞ●~*  {user2},Shinaeeeee!!.",
    "( ・∀・)ｒ鹵~<≪巛;ﾟДﾟ)ﾉ\n*Bug sprays {user2}*.",
    "( ﾟДﾟ)ﾉ占~<巛巛巛.\n-{user2} You pest!",
    "( う-´)づ︻╦̵̵̿╤── \(˚☐˚”)/ {user2}.",
    "{user1} {hits} {user2} with a {item}.",
    "{user1} {hits} {user2} in the face with a {item}.",
    "{user1} {hits} {user2} around a bit with a {item}.",
    "{user1} {throws} a {item} at {user2}.",
    "{user1} grabs a {item} and {throws} it at {user2}'s face.",
    "{user1} launches a {item} in {user2}'s general direction.",
    "{user1} starts slapping {user2} silly with a {item}.",
    "{user1} pins {user2} down and repeatedly {hits} them with a {item}.",
    "{user1} grabs up a {item} and {hits} {user2} with it.",
    "{user1} ties {user2} to a chair and {throws} a {item} at them.",
    "{user1} gave a friendly push to help {user2} learn to swim in lava.",
    "{user1} bullied {user2}.",
    "Nyaan ate {user2}'s leg. *nomnomnom*",
    "{user1} {throws} a master ball at {user2}, resistance is futile.",
    "{user1} hits {user2} with an action beam...bbbbbb (ง・ω・)ง ====*",
    "{user1} ara ara's {user2}.",
    "{user1} ora ora's {user2}.",
    "{user1} muda muda's {user2}.",
    "{user2} was turned into a Jojo reference!",
    "{user1} hits {user2} with {item}.",
    "Round 2!..Ready? .. FIGHT!!",
]

ITEMS = [
    "cast iron skillet",
    "angry meow",
    "cricket bat",
    "wooden cane",
    "shovel",
    "toaster",
    "book",
    "laptop",
    "rubber chicken",
    "spiked bat",
    "heavy rock",
    "chunk of dirt",
    "ton of bricks",
    "rasengan",
    "spirit bomb",
    "100-Type Guanyin Bodhisattva",
    "rasenshuriken",
    "Murasame",
    "ban",
    "chunchunmaru",
    "Kubikiribōchō",
    "rasengan",
    "spherical flying kat",
]

THROW = [
    "throws",
    "flings",
    "chucks",
    "hurls",
]

HIT = [
    "hits",
    "whacks",
    "slaps",
    "smacks",
    "bashes",
    "pats",
]

TRUTH = [
    "Siapa pirst lope mu?"
    "Ngaku! Pernah curi duit orang tua ga?",
    "Berapa jumlah mantan lu?",
    "Ceritakan masalah paling kamu ingat saat di sekolah",
    "Pilih cowo ganteng atau cowo kaya? Tapi ga ganteng",
    "Apabila kamu cewe bersedia kah untuk menjadi pacar owner ku @xtsea",
    "Momen paling paling terbaik menurut lu selama idup apa?",
    "Sebutkan 100 hal tentang teman kamu",
    "Pilih cewe cantik atau cewe jadi²an?",
    "Apa ketakutan yang paling besar menurut kamu?",
    "Ceritakan hal sebelum kamu putus sama pacar",
    "Tipe cewe idaman lu seperti apa? tete besarkah? Coba sebutkan seperti apa tipe lu",
    "Tipe cowo idaman kamu seperti apa?",
    "Coba tag orang yang paling kamu sayang disini.",
    "Hayoo, kapan terakhir kali kamu anu?",
    "Ceritakan kisah idup lu :')",
    "@rencprx menurut ku dia ganteng, coba deh kamu chat, trus ajak pacaran hehe ⚠️WARNING ini khusus cewe ya!",
  
]

DARE = [
     "Tampilkan foto paling memalukan di ponsel Anda"
     "Tampilkan lima orang terakhir yang Anda kirimi chat dan apa isi pesannya",
     "Bilang, aku jelek 5 kali dengan voice note",
     "Makan bawang putih mentah",
     "Ratakan 100 squad di pubg atau free fire",
     "Simpan tiga es batu di mulutmu sampai meleleh",
     "Katakan sesuatu yang kotor kepada orang di sebelah kirimu. Kamu punya teman!",
     "Berikan pijatan kaki pada orang di sebelah kanan Anda",
     "Masukkan 10 cairan berbeda yang tersedia ke dalam cangkir dan minumlah",
     "Ucapkan kata pertama yang muncul di pikiranmu",
     "Berikan lap dance kepada seseorang pilihan Anda",
     "Lepaskan empat pakaian",
     "Suka 15 posting pertama di umpan berita Facebook Anda",
     "Makan sesendok garam",
     "Pejamkan matamu sampai kamu pergi lagi",
     "Kirim sex ke orang terakhir di kontak telepon Anda",
     "Pamerkan wajah orgasme Anda",
     "Makan pisang dengan menggoda",
     "Kosongkan dompet Anda dan tunjukkan kepada semua orang apa yang ada di dalamnya",
     "Lakukan perayapan seksi terbaikmu",
     "Berpura-puralah menjadi orang di sebelah kananmu selama 10 menit",
     "Makan camilan tanpa menggunakan tangan",
     "Katakan dua hal jujur ​​tentang semua orang dalam grup",
     "Twerk sebentar",
     "Cobalah membuat anggota grup tertawa secepat mungkin",
     "Cobalah untuk memasukkan seluruh kepalan tanganmu ke dalam mulutmu",
     "Ceritakan kepada semua orang kisah memalukan tentang dirimu",
     "Coba jilat sikumu",
     "Posting selfie tertua di ponsel Anda di Instagram Stories",
     "Ceritakan kisah paling menyedihkan yang kamu tahu",
     "Melolong seperti serigala selama dua menit",
     "Menari tanpa musik selama dua menit",
     "Tari tiang dengan tiang imajiner",
     "Biarkan orang lain menggelitikmu dan mencoba untuk tidak tertawa",
     "Masukkan makanan ringan ke dalam mulut Anda sekaligus sebanyak yang Anda bisa",
     "Kirim selfie terbaru Anda.",
     "Kirim selfie terjelekmu.",
     "Kirim tangkapan layar riwayat pencarian facebook Anda",
     "Kirim tangkapan layar galeri Anda.",
     "Kirim tangkapan layar kotak masuk messenger Anda",
     "Katakan sesuatu yang sangat intim.",
     "Kirim tangkapan layar kotak masuk twitter Anda",
     "Kirim tangkapan layar layar beranda Anda.",
     "Kirim cover lagu favoritmu. ",
     "Lakukan lelucon lirik pada seseorang dan kirimkan buktinya.",
     "Akui kalo lu naksir temen sekelas lu saat ini. ❤️",
     "Ungkapkan siapa cinta sejatimu.",
     "Kirim tangkapan layar galeri Anda.",
     "Jadikan gambar gebetanmu sebagai wallpaper chat.",
     "Bilang ke @xtsea bahwa dia ganteng",
]


SLAP_FUNNY_ENGLISH = [ 
    "I'm sorry, did my hand accidentally slap your face?",
    "Oh, I'm sorry. I thought you were a mosquito.",
    "You know you deserved that, right?",
    "I didn't slap you. I just high-fived your face!",
    "It's not a slap, it's a wake-up call!",
    "If I slapped you any harder, Google would've found your next of kin.",
    "You're lucky I didn't headbutt you!",
    "Don't worry, I'm a professional slapper.",
]

SLAP_LUCU_INDONESIA = [
    "Maaf, apakah tangan saya tidak sengaja menampar wajah Anda?",
    "Oh maafkan saya. Saya pikir Anda nyamuk.",
    "Anda tahu Anda pantas mendapatkannya, bukan?",
    "Aku tidak menamparmu. Aku baru saja melakukan high-five dengan wajahmu!",
    "Itu bukan tamparan, itu panggilan bangun!",
    "Jika saya menampar Anda lebih keras, Google akan menemukan kerabat terdekat Anda.",
    "Kau beruntung aku tidak menandukmu!",
    "Jangan khawatir, saya seorang penampar profesional.",

]


# code by @xtsea

async def truth_string_str(c, m):
    user = await c.get_users("me")
    if not user:
        return
    mention_user = user.mention
    first_name = user.first_name
    truth_random = choice(TRUTH)
    if first_name:
        await m.reply_text(f"{first_name}, {truth_random}")
    elif mention_user:
        await m.reply_text(f"{mention_user}, {truth_random}")
    else:
        await m.reply_text("Can't get the name.")

async def dare_string_str_2(c, m):
    user = await c.get_users("me")
    if not user:
        return
    mention_user = user.mention
    first_name = user.first_name
    dare_random = choice(DARE)
    if first_name:
        await m.reply_text(f"{first_name}, {dare_random}")
    elif mention_user:
        await m.reply_text(f"{mention_user}, {dare_random}")
    else:
        await m.reply_text("Can't get the name.")

async def slap_template_fixed(c, m):
    user1 = (await c.get_users("me")).first_name
    if m.reply_to_message and m.reply_to_message.from_user:
        user2 = m.reply_to_message.from_user.first_name
        temp = choice(SLAP_TEMPLATES)
        item = choice(ITEMS)
        hit = choice(HIT)
        throw = choice(THROW)
        response_message = temp.format(user1=user1, user2=user2, item=item, hits=hit, throws=throw)
        await c.send_message(m.chat.id, response_message)
    else:
        await m.reply_text("Please reply to a message to slap someone!")


async def slap_funny_lol_fixed(c, m):
    if m.reply_to_message and m.reply_to_message.from_user:
        username = m.reply_to_message.from_user.username
        mention =  m.reply_to_message.from_user.mention
        slap_text = choice(SLAP_FUNNY_ENGLISH)
        if username is not None:
            await c.send_message(m.chat.id, f"@{username}, {slap_text}")
        elif mention:
            await c.send_message(m.chat.id, f"{mention}, {slap_text}")
        else:
            return
    else:
        await m.reply_text("Please reply to a message to slap someone!")


async def slap_lucu_lol(c, m):
    if m.reply_to_message and m.reply_to_message.from_user:
        username = m.reply_to_message.from_user.username
        mention =  m.reply_to_message.from_user.mention
        slap_text = choice(SLAP_LUCU_INDONESIA)
        if username is not None:
            await c.send_message(m.chat.id, f"@{username}, {slap_text}")
        elif mention:
            await c.send_message(m.chat.id, f"{mention}, {slap_text}")
        else:
            return
    else:
        await m.reply_text("Please reply to a message to slap someone!")
