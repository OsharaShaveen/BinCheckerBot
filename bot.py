import requests
from telethon import events, Button, TelegramClient
import os
import logging


logging.basicConfig(level=logging.INFO)

try:
    API_ID = int(os.environ.get("API_ID", 6))
    API_HASH = os.environ.get("API_HASH", None)
    TOKEN = os.environ.get("TOKEN", None)
except ValueError:
    print("You forgot to fullfill vars")
    print("Bot is quitting....")
    exit()
except Exception as e:
    print(f"Error - {str(e)}")
    print("Bot is quitting.....")
    exit()
except ApiIdInvalidError:
    print("Your API_ID or API_HASH is Invalid.")
    print("Bot is quitting.")
    exit()

bot = TelegramClient('bin', API_ID, API_HASH)
bin = bot.start(bot_token=TOKEN)

@bin.on(events.NewMessage(pattern="^[!?/]start$"))
async def start(event):
    if event.is_group:
        await event.reply("**Bin-Checker is Alive**")
        return
    await event.reply(f"**🫡 𝗛𝗘𝗬 {event.sender.first_name}**\n**ɪᴍ ᴀ ʙɪɴ ᴄʜᴇᴄᴋᴇʀ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ʙɪɴꜱ ᴡᴏʀᴋɪɴɢ ᴏʀ ɴᴏᴛ** 🥹\n ᴇɴᴛᴇʀ /help ᴛᴏ ᴍᴏʀᴇ ɪɴꜰᴏ ✅\n𝙋𝙊𝙒𝙀𝙍𝘿 𝘽𝙔 - white-devil-cc-generator.ml 𝘼𝙉𝘿 white-devil-bin-checker.ml\nᴛʜᴀɴᴋꜱ ꜰᴏʀ ᴜꜱɪɴɢ ᴍᴇ 🙂", buttons=[
    [Button.url("𝘿𝙀𝙑𝙀𝙇𝙊𝙋𝙀𝙍", "https://t.me/WhiteDevilOp999")]
    ])

@bin.on(events.NewMessage(pattern="^[!?/]help$"))
async def help(event):
    text = """
**Welcome to HelpMenu:**

__අනේහ් මට උදව් කරන්ඩහ්__

- /start - To Start Me :)
- /help - To Get Help Menu
- /bin - To check is your bin valid or not
"""
    await event.reply(text, buttons=[[Button.url("Sᴏᴜʀᴄᴇ Cᴏᴅᴇ", "https://github.com/OsharaShaveen/BinCheckerBot")]])

@bin.on(events.NewMessage(pattern="^[!?/]bin"))
async def binc(event):
    xx = await event.reply("`Processing.....`")
    try:
        input = event.text.split(" ", maxsplit=1)[1]

        url = requests.get(f"https://bins-su-api.now.sh/api/{input}")
        res = url.json()
        vendor = res['data']['vendor']
        type = res['data']['type']
        level = res['data']['level']
        bank = res['data']['bank']
        country = res['data']['country']
        me = (await event.client.get_me()).username

        valid = f"""
<b>✅ 𝙑𝘼𝙇𝙄𝘿 𝘽𝙄𝙉 ✅:</b>

<b>ʙɪɴ ➫</b> <code>{input}</code>
<b>ꜱᴛᴀᴛᴜꜱ ➫</b> <code>Valid Bin</code>
<b>ᴠᴇɴᴅᴏʀ ➫</b> <code>{vendor}</code>
<b>ᴛʏᴘᴇ ➫</b> <code>{type}</code>
<b>ʟᴇᴠᴇʟ ➫</b> <code>{level}</code>
<b>ʙᴀɴᴋ ➫</b> <code>{bank}</code>
<b>ᴄᴏᴜɴᴛʀʏ ➫</b> <code>{country}</code>

<b>𝘾𝙃𝙀𝘾𝙆𝙀𝙍 - @{me}</b>
<b>𝙐𝙎𝙀𝙍-𝙄𝘿 - {event.sender_id}</b>
"""
        await xx.edit(valid, parse_mode="HTML")
    except IndexError:
       await xx.edit("🫡 ρℓєαѕє єηтєя вιη тσ ¢нє¢к 🫡\n__`/bin yourbin`__")
    except KeyError:
        me = (await event.client.get_me()).username
        await xx.edit(f"**➤ ɪɴᴠᴀʟɪᴅ ʙɪɴ:**\n\n**Bin -** `{input}`\n**Status -** `🚫 𝗜𝗡𝗩𝗔𝗟𝗜𝗗 𝗕𝗜𝗡 🚫`\n\n**𝘾𝙃𝙀𝘾𝙆𝙀𝘿 𝘽𝙔-** @{me}\n**ᴜꜱᴇʀ-ɪᴅ** - ```{event.sender_id}```")

print ("Successfully Started")
bin.run_until_disconnected()
