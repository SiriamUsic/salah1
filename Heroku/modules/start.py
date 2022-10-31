import asyncio

from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.errors import FloodWait, UserNotParticipant
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatJoinRequest

from time import time
from datetime import datetime

from Heroku.setup.filters import command
from Heroku.config import BOT_NAME, OWNER_USERNAME, UPDATE, SUPPORT, BOT_USERNAME

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)

IMG = ["https://telegra.ph/file/9cbae99908382932e51f0.png", "https://telegra.ph/file/9870433b0c155ecf2ad07.png", "https://telegra.ph/file/c6efbd77d1d931c45d0c2.jpg", "https://telegra.ph/file/f9d97a7cde8b79f4ab0a3.png"]
HELP_TEXT = """
مرحبا ! {}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ أنا بوت تشغيل موسيقي في المكالمه الصوتيه ولدي الكثير من الميزات التي تعجبك
‣ أستطيع تشغيل ( الصوت + الفيديو )
‣ لدي تقريبًا جميع الميزات التي تحتاجها في بوت الموسيقى
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ انقر فوق زر المساعدة لمزيد من المعلومات ℹ️.
"""


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(f"{HELP_TEXT}".format(message.from_user.mention()),
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ اضفني الى مجموعتك", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],
                [
                    InlineKeyboardButton(
                        "𝐒𝐎𝐔𝐑𝐂𝐄 𝐉𝐀𝐕𝐀", url=f"https://t.me/{UPDATE}"),
                    InlineKeyboardButton(
                        "المساعدة ⁉️", callback_data="others")
                ]
           ]
        ),
    )



@Client.on_message(command(["ping","البينج"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("جاري حساب سرعة البوت...")
    delta_ping = time() - start
    await m_reply.edit_text("سرعة البوت \n" f"`{delta_ping * 1000:.3f} MS`")
@Client.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    ass_uname = (await user.get_me()).username
    bot_id = (await c.get_me()).id
    for member in m.new_chat_members:
        if member.id == bot_id:
            return await m.reply(
                "🍾️ **شـكرا لإضـافتـي إلـى المجـموعـة !**\n\n"
                "**قـم بتـرقيتـي كـمـشـرف عـن المـجـموعـة ، وإلا فلـن أتمـكن مـن الـعـمل بـشـكل صـحيـح ، ولا تنـسـى الـكتابـة /userbotjoin لـدعـوة المـساعـد.**\n\n"
                "**بـمجـرد الانـتهـاء ، اكـتـب** /reload",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("𝐒𝐎𝐔𝐑𝐂𝐄 𝐉𝐀𝐕𝐀", url=f"https://t.me/JAVA_telthon"),
                            InlineKeyboardButton("𝐉𝐀𝐕𝐀 𝐒𝐔𝐏𝐏𝐎𝐑𝐓", url=f"https://t.me/JAVA_Supports")
                        ],
                        [
                            InlineKeyboardButton("حـسـاب المساعـد", url=f"https://t.me/{ass_uname}")
                        ]
                    ]
                )
            )

@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **الدليل الأساسي لاستخدام هذا الروبوت:**

1.) **أولا ، أضفني إلى مجموعتك.**
2.) **بعد ذلك ، قم بترقيتي كمسؤول ومنح جميع الأذونات باستثناء المسؤول المجهول.**
3.) **بعد ترقيتي ، اكتب /reload في مجموعة لتحديث بيانات المسؤولين.**
3.) **اضف @{ASSISTANT_NAME} إلى مجموعتك أو اكتب / userbotjoin لدعوته.**
4.) **قم بتشغيل مكالمة صوتيه أولاً قبل البدء في تشغيل الفيديو / الموسيقى.**
5.) **في بعض الأحيان ، يمكن أن تساعدك إعادة تحميل الروبوت باستخدام الأمر / reload في إصلاح بعض المشكلات.**

📌 **إذا لم ينضم المساعد إلى الدردشة المرئية ، فتأكد من تشغيل دردشة الفيديو بالفعل ، أو اكتب / userbotleave ثم اكتب / userbotjoin مرة أخرى.**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 ︙رجــــــوع", callback_data="start")]]
        ),
    )