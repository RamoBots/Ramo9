import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from RamoMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from RamoMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["رامو","المبرمج رامو ","مبرمج السورس"," المطور ","مطور السورس♕"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/f9d90e1ae27f9b53cc59c.mp4",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[𝑹𝑨𝑴𝑶 || رامـــــــو]❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @C_lxl_C ❫
◉ 𝙸𝙳      : ❪ `6236388211` ❫
◉ 𝑪𝑯    : ❪ @R_surce ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝑹𝑨𝑴𝑶 || رامـــــــو", url=f"https://t.me/C_lxl_C"), 
                 ],[
                   InlineKeyboardButton(
                        "🎸𓏺𝗦𝗼𝘂𝗿𝗰𝗲ᯓ𝑹𝑨𝑴𝑶𖠛🎸", url=f"https://t.me/R_surce"),
                ],

            ]

        ),

    )
