from pyrogram.types import InlineKeyboardButton

import config
from RamoMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضف البوت الي جروبك او قناتك🎸", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="قناة السورس🎸", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضف البوت الي جروبك او قناتك🎸",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="الاوامر🎸", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="المطور🎸", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="قناة السورس🎸", url=config.SUPPORT_CHAT),
        ],
        [
        
            InlineKeyboardButton(text="𝑹𝑨𝑴𝑶 || رامـــــــو", url=f"https://t.me/C_lxl_C"),
        ],
    ]
    return buttons
