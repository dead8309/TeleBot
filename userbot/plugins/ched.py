from telethon import events
import random, re
from userbot.utils import admin_cmd
import asyncio
import io

@borg.on(admin_cmd(pattern="chodna ?(.*)"))
async def _(chodna):
	name = chodna.pattern_match.group(1)
	await chodna.edit(f"{name} Ki")
	await asyncio.sleep(0.9)
	await chodna.edit("Gaand Maro")
	await asyncio.sleep(0.9)
	await chodna.edit("Tab Tak")
	await asyncio.sleep(0.8)
	await chodna.edit("Jab Tak")
	await asyncio.sleep(0.8)
	await chodna.edit(f"{name} Ki Gaand")
	await asyncio.sleep(0.9)
	await chodna.edit("Me Ched Na")
	await asyncio.sleep(0.9)
	await chodna.edit("Ho Gaie")
	await asyncio.sleep(0.9)
	await chodna.edit("🥺🥺🥺")
	await asyncio.sleep(0.8)
	await chodna.edit(f"{name} Ki Gaand Maro Tab Tak Jab Tak {name} Ki Gaand Me Ched Na Ho Gaie 🥺🥺🥺")
	await asyncio.sleep(3)
	await chodna.edit("#Plugin Made by @dead_yt")
	await asyncio.sleep(8)
	await chodna.delete()
