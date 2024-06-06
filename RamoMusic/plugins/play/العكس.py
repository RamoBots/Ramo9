import asyncio


import random
from RamoMusic import app
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from strings.filters import command
from pyrogram import filters, Client
import config



txt = [

            "**- اسرع واحد يدز العكس** ~ ( بارده)",


             "**- اسرع واحد يدز العكس** ~ ( اجيت)",
            

             "**- اسرع واحد يدز العكس*ذ ~ ( جبان)",
             
             
             "**- اسرع واحد يدز العكس** ~ ( مافهمت)",
             
               
             "**- اسرع واحد يدز العكس** ~ ( ميت)",
             
             
             "**- اسرع واحد يدز العكس** ~ ( وصخ)",
             
             
             "**- اسرع واحد يدز العكس** ~ ( جوعان)",
             
             
             "**- اسرع واحد يدز العكس** ~ ( زين)",
             
             
             "**- اسرع واحد يدز العكس** ~ ( قوي)",
             
             
             "**- اسرع واحد يدز العكس** ~ ( بطيء)",
 
            
            

        ]


        


@app.on_message(command(["العكس","العكس🎸", ""]))


async def cutt(client: Client, message: Message):


      a = random.choice(txt)


      await message.reply(


        f"{a}")
  
