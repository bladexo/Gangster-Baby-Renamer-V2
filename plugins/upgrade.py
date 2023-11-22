"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**PREMIIUM PLAN NOT AVAILABLE AT THE MOMENT**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/MR_DINNO1")], 
        			[InlineKeyboardButton("Paytm",url = "https://p.paytm.me/xCTH/vo37hii9"),
        			InlineKeyboardButton("Cancel",callback_data = "cancel") 
	   ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgrade(bot,message):
	text = """**PREMIUM PLAN NOT AVAILABLE AT THE MOMMENT**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/MR_DINNO1")], 
        			[InlineKeyboardButton("Paytm",url = "https://p.paytm.me/xCTH/vo37hii9"),
        			InlineKeyboardButton("Paytm",url = "https://p.paytm.me/xCTH/vo37hii9")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
