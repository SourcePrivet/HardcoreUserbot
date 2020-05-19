"""Check if userbot alive."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**`𝕊𝕆𝕌ℝℂ𝔼 𝔹𝕐 𝔻ℍ𝕌ℝ𝔾ℍ𝔸𝕄 :- @visa4bin `**\n\n"
                     "**✅Bot Made By:- @visa4bin\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n**"
                     "**✅Database Status: Databases functioning normally!**\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n💞source channel @visa4bin!\n"
                     f"`user`: {DEFAULTUSER}\n"
                     "[source](https://t.me/visa4bin)")
