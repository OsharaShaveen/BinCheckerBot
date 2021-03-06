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
    await event.reply(f"**ð«¡ ððð¬ {event.sender.first_name}**\n**Éªá´ á´ ÊÉªÉ´ á´Êá´á´á´á´Ê Êá´á´ á´á´ á´Êá´á´á´ Êá´á´Ê ÊÉªÉ´ê± á´¡á´Êá´ÉªÉ´É¢ á´Ê É´á´á´** ð¥¹\n á´É´á´á´Ê /help á´á´ á´á´Êá´ ÉªÉ´ê°á´ â\nðððððð¿ ð½ð - white-devil-cc-generator.ml ð¼ðð¿ white-devil-bin-checker.ml\ná´Êá´É´á´ê± ê°á´Ê á´ê±ÉªÉ´É¢ á´á´ ð", buttons=[
    [Button.url("ð¿ðððððððð", "https://t.me/WhiteDevilOp999")]
    ])

@bin.on(events.NewMessage(pattern="^[!?/]help$"))
async def help(event):
    text = """
**Welcome to HelpMenu:**

__à¶à¶±à·à·à· à¶¸à¶§ à¶à¶¯à·à· à¶à¶»à¶±à·à¶©à·à·__

- /start - To Start Me :)
- /help - To Get Help Menu
- /bin - To check is your bin valid or not
"""
    await event.reply(text, buttons=[[Button.url("Sá´á´Êá´á´ Cá´á´á´", "https://github.com/OsharaShaveen/BinCheckerBot")]])

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
<b>â ðð¼ððð¿ ð½ðð â:</b>

<b>ÊÉªÉ´ â«</b> <code>{input}</code>
<b>ê±á´á´á´á´ê± â«</b> <code>Valid Bin</code>
<b>á´ á´É´á´á´Ê â«</b> <code>{vendor}</code>
<b>á´Êá´á´ â«</b> <code>{type}</code>
<b>Êá´á´ á´Ê â«</b> <code>{level}</code>
<b>Êá´É´á´ â«</b> <code>{bank}</code>
<b>á´á´á´É´á´ÊÊ â«</b> <code>{country}</code>

<b>ð¾ððð¾ððð - @{me}</b>
<b>ðððð-ðð¿ - {event.sender_id}</b>
"""
        await xx.edit(valid, parse_mode="HTML")
    except IndexError:
       await xx.edit("ð«¡ ÏâÑÎ±ÑÑ ÑÎ·ÑÑÑ Ð²Î¹Î· ÑÏ Â¢Ð½ÑÂ¢Ðº ð«¡\n__`/bin yourbin`__")
    except KeyError:
        me = (await event.client.get_me()).username
        await xx.edit(f"**â¤ ÉªÉ´á´ á´ÊÉªá´ ÊÉªÉ´:**\n\n**Bin -** `{input}`\n**Status -** `ð« ðð¡ð©ðððð ððð¡ ð«`\n\n**ð¾ððð¾ððð¿ ð½ð-** @{me}\n**á´ê±á´Ê-Éªá´** - ```{event.sender_id}```")

print ("Successfully Started")
bin.run_until_disconnected()
