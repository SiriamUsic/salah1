import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import *
from random import choice
from Heroku import cloner, ASSUSERNAME, BOT_NAME
from Heroku.config import API_ID, API_HASH
IMG = ["https://telegra.ph/file/9cbae99908382932e51f0.png", "https://telegra.ph/file/9870433b0c155ecf2ad07.png", "https://telegra.ph/file/c6efbd77d1d931c45d0c2.jpg", "https://telegra.ph/file/f9d97a7cde8b79f4ab0a3.png"]
MESSAGE = "مرحبا بك في صانع بوتات ميوزك سورس جافا \n•══•| [𓆩𝐒𝐎𝐔𝐑𝐂𝐄 𝐉𝐀𝐕𝐀𓆪](https://t.me/JAVA_tlethon) |•══•\n لصنع بوت ارسل /JAVA توكن بوتك \n♕ مثال :- /JAVA 5649142057:AAFc7vostaFh7fabHhfnd7fAYwOn8"

@cloner.on_message(filters.private & filters.command("start"))
async def hello(client, message: Message):
    buttons = [
           [
                InlineKeyboardButton("✘ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ", url="t.me/JAVA_telthon"),
            ],
            [
                InlineKeyboardButton("✘ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url="t.me/JAVA_Supports"),
            ],
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(message.chat.id, f"{choice(IMG)}", caption=MESSAGE, reply_markup=reply_markup)

##Copy from here 

# © By Itz-Zaid Your motherfucker if uh Don't gives credits.
@cloner.on_message(filters.private & filters.command("JAVA"))
async def clone(bot, msg: Message):
    chat = msg.chat
    text = await msg.reply("استخدم الامر كدا :\n\n /JAVA وحط توكنك هنا")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("جاري صنع البوت الخاص بك")
                   # change this Directry according to ur repo
        client = Client(":memory:", API_ID, API_HASH, bot_token=phone, plugins={"root": "Heroku.modules"})
        await client.start()
        user = await client.get_me()
        await msg.reply(f"تم صنع بوتك بنجاح \n•══•| [ 𓆩𝐒𝐎𝐔𝐑𝐂𝐄 𝐉𝐀𝐕𝐀𓆪 ](https://t.me/JAVA_tlethon) |•══•\n اسم بوتك : @{user.username} \nالحساب المساعد : @{ASSUSERNAME}\n\n أضف الآن البوت والمساعد الخاصين بك إلى الدردشة الخاصة بك!\n•══•| [ 𓆩𝐒𝐎𝐔𝐑𝐂𝐄 𝐉𝐀𝐕𝐀𓆪 ](https://t.me/JAVA_tlethon) |•══•\n\nشكرا لاستخدامك سورس جافا.")
    except Exception as e:
        await msg.reply(f"**حدث خطأ :** `{str(e)}`\nاضغط /start للبدء من جديد.")
#End
##This code fit with every pyrogram Codes just import then @Client Xyz!

