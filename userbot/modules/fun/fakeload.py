# Made by @DneZyeK

import asyncio
import re
import time

from time import sleep

from ..help import add_help_item
from userbot.events import register


@register(outgoing=True, pattern='^.fl(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(1)
	await typew.edit("`start loading...`")
	sleep(1)
	await typew.edit("0%")
	number = 1
	await typew.edit(str(number) + "%   ▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████████▌")
	sleep(1)
	await typew.edit("`Halahh Tertypu kamu bang sat!`")
	# I did it for two hours :D just ctrl+c - crtl+v


add_help_item(
    "fakeload",
    "Fun",
    "Fake load :D",
    """
    `.fl`
    """
)
