"""Emoji
Available Commands:
.dh"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 5)
    input_str = event.pattern_match.group(1)
    if input_str == "dh":
        await event.edit(input_str)
        animation_chars = [
            "الف",
            "باء",
            "تاء",
            "ثاء",
            "هيا ننكح العراب"
        ]

        for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i %5 ])
