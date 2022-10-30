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
MESSAGE = "مرحبا بك في صانع بوتات ميوزك سورس جافا"

@cloner.on_message(filters.private & filters.command("start"))
async def hello(client, message: Message):
    buttonsInlineKeyboard = [
           [
                InlineKeyboardButton("صنع بوت", callback_data="Salah"), 
            ],
            [
                InlineKeyboardButton("𝐒𝐎𝐔𝐑𝐂𝐄 𝐉𝐀𝐕𝐀", url="t.me/JAVA_tlethon"),
            ],
            ] 
            InlineKeyboardButton("𝐒𝐀𝐋𝐀𝐇 𝐇𝐄𝐌𝐃𝐀𝐍", url="t.me/Salah_officiall"),
            ],
            [
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


@Client.on_callback_query(filters.regex("Salah"))
async def credit(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**•══•| [ 𓆩𝐒𝐎𝐔𝐑𝐂𝐄 𝐉𝐀𝐕𝐀𓆪 ](https://t.me/JAVA_tlethon) |•══• \nطريقة صنع بوت \n• 1- ارسل /JAVA \n• 2- ارسل /JAVA توكن بوتك \nمثال : /JAVA 6554227635:hftuocadycFuzd \n 3- ستظهر لك رسالة تم صنع بوتك كدا تكون صنعت بوت ميوزك مجانا
 •══•| [ 𓆩𝐒𝐎𝐔𝐑𝐂𝐄 𝐉𝐀𝐕𝐀𓆪 ](https://t.me/JAVA_tlethon) |•══•**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⬅️ رجــوع", callback_data="others")
                ],
            ]
        ),
    )

@Client.on_callback_query(filters.regex("cls"))
async def reinfo(_, query: CallbackQuery):
    try:
        await query.message.delete()
        await query.message.reply_to_message.delete()
    except Exception:
        pass
#End
##This code fit with every pyrogram Codes just import then @Client Xyz!

