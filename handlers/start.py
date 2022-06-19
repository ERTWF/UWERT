import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.delete()
    await message.reply_sticker("CAACAgUAAxkBAAEENxZiNtPdibVkMsjLZrUG9NK4hotHQgAC2wEAAoM12VSdN9ujxVtnUyME")
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**━━━━━━━━━━━━━━━━━━
 هلا عمري {message.from_user.mention()} !
  انا بوت استطيع تشغيل الاغاني في المكالمات
  المرئيه الجديده على Telegram اضفني لكروبك
  امنحني صلاحبات اضغط زر الاوامر لمعرفة 
  كيف تشغيلي اكتب /انضم لكي يدخل 
  حساب المساعد الى المجموعه حقك
━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "☬ اضفني الى مجموعتك ☬", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        "👨‍💻 مطور البوت 👨‍💻", url=f"https://t.me/{me}"
                    ),
                    InlineKeyboardButton(
                        "🥇 كروب الدعم 🥇", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ],[
                    InlineKeyboardButton(
                        "👷‍♂ الاوامر 👷‍♂", url=f"https://telegra.ph/%F0%9D%99%B2%E1%B4%8F%E1%B4%8D%E1%B4%8D%E1%B4%80%C9%B4%E1%B4%85s-04-06"
                    ),
                    InlineKeyboardButton(
                        "🌐 قناة البوت الرسمية 🌐", url="https://t.me/VFF35"
                    )]
            ]
       ),
    )

