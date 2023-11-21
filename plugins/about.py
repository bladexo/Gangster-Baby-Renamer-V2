import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user

from helper.progress import humanbytes

@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"𝖡𝖮𝖳 :- <a href='https://t.me/RedRenamerV2bot'>𝚁 𝙴 𝙳</a>\𝖴𝗉𝖽𝖺𝗍𝖾𝗌 :- <a href='https://t.me/RedOfficiall'>𝚁𝙴𝙳 𝚄𝚙𝚍𝚊𝚝𝚎𝚜</a>\nTotal Renamed File :- {total_rename}\nTotal Size Renamed :- {humanbytes(int(total_size))} \n\n <a href='https://t.me/MRDINNO'>**R E D**</a> ❤️",quote=True)
