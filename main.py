from pyrogram import Client, filters

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import os
import aiohttp
import asyncio
import json
import sys
import time
from youtubesearchpython import SearchVideos
from pyrogram import filters, Client
from youtube_dl import YoutubeDL
from youtube_dl.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)



API_ID = "5642193"
API_HASH = "c28fc9ac88530587236175da89184d75"
BOT_TOKEN = "6297344590:AAFbBHK9PioaIS0sZnH0jR4a4Sp7859Rt_4"


INSANE = Client(
    name="insane test bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

START_BUTTONS =[[
    InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url="https://t.me/Resso_offical_bot?startgroup=true")
    ],[
    InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="t.me/INSANEX3"),
    InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/INSANEX3_SUPPORT")
    ]]

@INSANE.on_message(filters.command("start"))
async def start_cmd(Client, message):
    await message.reply_photo(
        photo="https://telegra.ph/file/da545a93169c6e91d4c98.jpg",
        caption="ʜᴇʏ, \n \n ɪ'ᴍ ᴀ ᴛᴇʟᴇɢʀᴀᴍ sᴛʀᴇᴀᴍɪɴɢ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇ. sᴜᴘᴘᴏʀᴛɪɴɢ ᴘʟᴀᴛғᴏʀᴍs ʟɪᴋᴇ ʏᴏᴜᴛᴜʙᴇ,ʀᴇssᴏ....ᴇᴛᴄ \n \n A ᴘᴏᴡᴇғᴜʟ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ᴀɴᴅ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs.",
        reply_markup =InlineKeyboardMarkup (START_BUTTONS)
  
    )
    
INSANE_BUTTONS =[[
    InlineKeyboardButton("Owner", url="https://t.me/insanex3")
    ]]
    
@INSANE.on_message(filters.command("owner"))
async def owner_cmd(client, message):
    await message.reply_photo(
        photo="https://telegra.ph/file/a42e0a1e09e4ca442fe3b.jpg",
        reply_markup =InlineKeyboardMarkup (INSANE_BUTTONS)
    )


@INSANE.on_message(filters.private & ~filters.bot & ~filters.command("help") & ~filters.command("start") & ~filters.command("s"))
async def a(client, message):
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
        print(query)
        m = message.reply('`Searching... Please Wait...`')
        ydl_opts = {"format": "bestaudio[ext=m4a]"}
        try:
            results = []
            count = 0
            while len(results) == 0 and count < 6:
                if count>0:
                    time.sleep(1)
                    results = YoutubeSearch(query, max_results=1).to_dict()
                    count += 1
    
    
                      
                    

                  
                

                            
 
print("INSANE Bot started ")
INSANE.run()

