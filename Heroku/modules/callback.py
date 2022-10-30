from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from Heroku.config import BOT_NAME, OWNER_USERNAME, UPDATE, SUPPORT, BOT_USERNAME

HELP_TEXT = """
مرحبا ! [{}](tg://user?id={})
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ أنا بوت تشغيل موسيقي في المكالمه الصوتيه ولدي الكثير من الميزات التي تعجبك
‣ أستطيع تشغيل ( الصوت + الفيديو )
‣ لدي تقريبًا جميع الميزات التي تحتاجها في بوت الموسيقى
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ انقر فوق زر المساعدة لمزيد من المعلومات.
"""


@Client.on_callback_query(filters.regex("home"))
async def home(_, query: CallbackQuery):
    await query.edit_message_text(f"{HELP_TEXT}".format(query.message.chat.first_name, query.message.chat.id),
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                    "➕ اضفني الى مجموعتك", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],
                [
                    InlineKeyboardButton(
                        "𝐒𝐎𝐔𝐑𝐂𝐄 𝐉𝐀𝐕𝐀", url=f"https://t.me/JAVA_telthon"),
                    InlineKeyboardButton(
                    "المساعدة", callback_data="others") 
                ]
           ]
        ),
    )






@Client.on_callback_query(filters.regex("others"))
async def others(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""مرحبا [{query.message.chat.first_name}](tg://user?id={query.message.chat.id})

انقر فوق الأزرار الواردة أدناه لمعرفة المزيد عني :""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐒𝐎𝐔𝐑𝐂𝐄 𝐉𝐀𝐕𝐀", url=f"https://t.me/JAVA_telthon"),
                    InlineKeyboardButton(
                        "𝐒𝐀𝐋𝐀𝐇 𝐇𝐄𝐌𝐃𝐀𝐍", url=f"https://t.me/Salah_officiall")
                ],
                [
                    InlineKeyboardButton(
                        "اوامر التشغيل", callback_data="credit"),
                    InlineKeyboardButton(
                        "السورس", callback_data="repoinfo")
                ],
                [
                    InlineKeyboardButton("⬅️ رجــوع", callback_data="home")
                ]
           ]
        ),
    )


@Client.on_callback_query(filters.regex("credit"))
async def credit(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**🤖 أوامر البوت العادية :-

» /play او تشغيل و (اسم الاغنيه)  - لتشغيل الموسيقي
» /skip - تخطي الأغنية
» /end - ايقاف تشغيل الموسيقى
» /pause - أوقف التشغيل مؤقتًا
» /resume - استئناف التشغيل
» /mute - كتم المساعد 
» /search - (إسم الأغنية)



⚙ بعض الأوامر الإضافية :-

» /examine - لاختبار حالة تشغيل البوت
» /start - بدأ البوت
» /id - لجلب ايديك
» /repo - لجلب كود مصدر السورس
» /rmd - حذف كل التنزيلات
» /clean - نظف ملفات التخزين
» /gcast - بث رسالتك


𓆩𝐒𝐎𝐔𝐑𝐂𝐄 𝐉𝐀𝐕𝐀𓆪 ](https://t.me/JAVA_tlethon)**""",
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


@Client.on_callback_query(filters.regex("repoinfo"))
async def repoinfo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""سورس جافا ميوزك""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⬅️ رجــوع", callback_data="others")
                ],
            ]
        ),
        disable_web_page_preview=True,
    )
