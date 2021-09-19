from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "Yeahhh Menu Music of @LelouchXRobot",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•Support•", url="https://t.me/lelouchsupportchat"
                    ),
                    InlineKeyboardButton(
                        "⚡•Credits•⚡", url="https://t.me/Psycho_Bots"
                    )
                ],
            ]
        )
    )