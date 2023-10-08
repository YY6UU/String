from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""أهلًا {msg.from_user.mention},

هذا هو {me2},
يمكنك استخراج كود تيرمكس وبايروجرام من هنا

من : [حيدر](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="استخراج الجلسة", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("𝗞𝗔𝗜𝗗𝗢", url="https://t.me/kaido_q"),
                    InlineKeyboardButton("المطور", user_id=OWNER_ID)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
