import asyncio, subprocess
import time, re, io
from userbot import bot, BOTLOG, BOTLOG_CHATID, CMD_HELP
from telethon import events, functions, types
from telethon.events import StopPropagation
from telethon.tl.functions.messages import ExportChatInviteRequest
from telethon.tl.functions.contacts import BlockRequest
from telethon.tl.functions.channels import LeaveChannelRequest, CreateChannelRequest, DeleteMessagesRequest
from collections import deque
from telethon.tl.functions.users import GetFullUserRequest
from userbot.events import register
from userbot.utils import admin_cmd

@borg.on(admin_cmd("leave$"))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`I iz Leaving dis Kensur Group kek!`")
        time.sleep(3)
        if '-' in str(e.chat_id):
            await bot(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit('`Sar This is Not A Chat`')

@borg.on(admin_cmd(";__;$"))
#@register(outgoing=True, pattern="^;__;$")
async def fun(e):
    t = ";__;"
    for j in range(10):
        t = t[:-1] + "_;"
        await e.edit(t)

@borg.on(admin_cmd("Oof$"))
#@register(outgoing=True, pattern="^Oof$")
async def Oof(e):
    t = "Oof"
    for j in range(15):
        t = t[:-1] + "of"
        await e.edit(t)

@borg.on(admin_cmd("ccry$"))
#@register(outgoing=True, pattern="^.cry$")
async def cry(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("(;´༎ຶД༎ຶ)")

@borg.on(admin_cmd("fp$"))
#@register(outgoing=True, pattern="^.fp$")
async def facepalm(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("🤦‍♂")

@borg.on(admin_cmd("moon$"))
#@register(outgoing=True, pattern="^.mmoon$")
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
		

@borg.on(admin_cmd("source$"))
#@register(outgoing=True, pattern="^.source$")
async def source(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("t.me/visa4bin")

@borg.on(admin_cmd("readme$"))
#@register(outgoing=True, pattern="^.readme$")
async def reedme(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("read you")



@borg.on(admin_cmd("heart$"))		
#@register(outgoing=True, pattern="^.heart$")
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("❤️🧡💛💚💙💜🖤"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
		
@borg.on(admin_cmd("fap$"))
#@register(outgoing=True, pattern="^.fap$")
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🍆✊🏻💦"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)

@borg.on(admin_cmd("myusernames$"))
#@register(outgoing=True, pattern="^.myusernames$")
async def _(event):
    if event.fwd_from:
        return
    result = await bot(functions.channels.GetAdminedPublicChannelsRequest())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"- {channel_obj.title} @{channel_obj.username} \n"
    await event.edit(output_str)



CMD_HELP.update({
    "leave": "Leave a Chat"
})
CMD_HELP.update({
    ";__;": "You try it!"
})
CMD_HELP.update({
    "cry": "Cry"
})
CMD_HELP.update({
    "fp": "Send face palm emoji."
})
CMD_HELP.update({
    "moon": "Bot will send a cool moon animation."
})
CMD_HELP.update({
    "clock": "Bot will send a cool clock animation."
})
CMD_HELP.update({
    "readme": "Reedme."
})
CMD_HELP.update({
    "source": "Gives the source of your userbot"
})
CMD_HELP.update({
    "myusernames": "List of Usernames owned by you."
})
CMD_HELP.update({
    "oof": "Same as ;__; but ooof"
})
CMD_HELP.update({
    "earth": "Sends Kensar Earth animation"
})
CMD_HELP.update({
    "heart": "Try and you'll get your emotions back"
})
CMD_HELP.update({
    "fap": "Faking orgasm"
})
