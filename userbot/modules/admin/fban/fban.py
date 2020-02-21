import asyncio

from telethon.tl.types import MessageEntityMentionName, MessageEntityMention

from ...help import add_help_item
from userbot import is_mongo_alive, bot
from userbot.events import register
from userbot.modules.admin.fban.fban_db import get_fban
from userbot.utils import parse_arguments, get_user_from_event


@register(outgoing=True, pattern=r"^\.fban(\s+[\S\s]+|$)")
async def fedban_all(msg):
    if not is_mongo_alive():
        await msg.edit("`Database connections failing!`")
        return

    reply_message = await msg.get_reply_message()

    params = msg.pattern_match.group(1) or ""
    args, text = parse_arguments(params, ['reason'])
    banid = None
    if reply_message:
        banid = reply_message.from_id
        banreason = args.get('reason', '[spam]')
    else:
        banreason = args.get('reason', '[fban]')
        if text.isnumeric():
            banid = int(text)
        elif msg.message.entities:
            ent = await bot.get_entity(text)
            if ent: banid = ent.id

    if "[spam]" in banreason:
        spamwatch = True
    else:
        spamwatch = False

    # Send the proof to Spamwatch in case it was spam
    # Spamwatch is a reputed fed fighting against spam on telegram
    
    if spamwatch:
    	if reply_message:
    		await reply_message.forward_to(-1001312712379)

    if not banid:
        return await msg.edit("**No user to fban**", delete_in=3)

    failed = dict()
    count = 1
    fbanlist = [i['chat_id'] for i in await get_fban()]

    for bangroup in fbanlist:
        async with bot.conversation(bangroup) as conv:
            await conv.send_message(f"/fban {banid} {banreason}")
            resp = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
            if "New FedBan" not in resp.text:
                failed[bangroup] = str(conv.chat_id)
            else:
                count += 1
                await msg.reply("**Fbanned in " + str(count) + " feds!**", delete_in=3)
            # Sleep to avoid a floodwait.
            # Prevents floodwait if user is a fedadmin on too many feds
            await asyncio.sleep(0.2)

    if failed:
        failedstr = ""
        for i in failed.keys():
            failedstr += failed[i]
            failedstr += " "
        await msg.reply(f"**Failed to fban in {failedstr}**", delete_in=3)
    else:
        await msg.reply("**Fbanned in all feds!**", delete_in=3)

    msg.delete()


add_help_item(
    "fedban",
    "Admin",
    "Userbot module containing various sites direct links generators",
    """
    `.fban`
    **Usage:** Reply to a user to fban them in all the groups provided by you!
    
    `.addfban`
    **Usage:** add groups to fban list.
    
    `.removefban`
    **Usage:** removes groups from the fban list.
    """
)
