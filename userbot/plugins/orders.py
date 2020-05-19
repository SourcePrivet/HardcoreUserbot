"""Emoji
Available Commands:
.oreders"""

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
    if input_str == "oreders":
        await event.edit(input_str)
        animation_chars = [
            ".moon
.smoon
.earth
.fap
.Oof
.heart
.lovestory
.fuk
.wtf
.ok
.hack
.pornhub
.lucky
.heart
.load
.square
.up
.round
.anim
.monkey
.fnl
.hand
.cnt
.kk
.clock
.congo
.ding
.dfork
.eye
.chod
.sqh
.vquickheal
.fuck
.sux
.kiss
.windows
.macos
.linux
.stock
.os
.snake
.squ
.think
.lol
.virus
.wahack",
           
        ]

        for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i %5 ])
