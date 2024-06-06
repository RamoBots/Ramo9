import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from RamoMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from RamoMusic import app
from random import  choice, randint

                

@app.on_message(
    command(["سورس","السورس","السورس♡"])

)
async def huhh(client: Client, message: Message):
    await message.reply_video(
        video="https://graph.org/file/f9d90e1ae27f9b53cc59c.mp4",
        caption="⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙶𝚁𝙾𝚄𝙿", url=f"https://t.me/Z_vxxz"), 
                    InlineKeyboardButton(
                        "𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url=f"https://t.me/R_surce"),
                  ],[
                    InlineKeyboardButton(
                        "𝑹𝑨𝑴𝑶 || رامـــــــو", url=f"https://t.me/C_lxl_C"),
                  ],[
                    InlineKeyboardButton(
                        "ضف البوت الي مجموعتك او قناتك🎸", url=f"https://t.me/{app.username}?startgroup=true"),
                ],

            ]

        ),

    )
