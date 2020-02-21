# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module which contains afk-related commands """

from random import choice, randint
from asyncio import sleep

from telethon.events import StopPropagation

from userbot import (AFKREASON, COUNT_MSG, CMD_HELP, ISAFK, BOTLOG,
                     BOTLOG_CHATID, USERS, PM_AUTO_BAN)
from userbot.events import register

# ========================= CONSTANTS ============================
AFKSTR = [
    "Lagi sibuk pak. chat aja dulu nanti gw bales!",
    "Lagi ga megang HP. klo ada perlu, chat aja setelah bunyi beep:\n`beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeep`!",
    "Ciee kangen, nanti juga balik.",
    "Tunggu bentar klo ngga...,\nya lama hhe.",
    "Poco lagi ga ada, ga tau dimana.",
    "Roses are red,\nViolets are blue,\nLeave me a message,\nAnd I'll get back to you.",
    "Salah satu hal terbaik dalam hidup adalah…\nMenunggu aku kembali hhe.",
    "Bentar pak,\nKlo lama,\nYa bukan bentar hheh.",
    "Klo blm tau,\nPoco lg ga ada.",
    "Hello, ini chat AFK, ga bakal ku cuekin koq",
    "Aku sedang mengarungi 7 Lautan 7 Negara,\n7 Samudra and 7 Benua,\n7 Gunung and 7 Bukit,\n7 Daratan and 7 Tanjakan,\n7 Jurang and 7 Danau,\n7 Mata Air and 7 Padang Rumput,\n7 Kota and 7 Daerah,\n7 RW and 7 Rumah...\n\nPokoknya jauh!",
    "Lagi gak megang HP, teriakin aja layar HP pak, kali gw denger wkwkwk.",
    "gw pergi ke arah\n---->",
    "gw pergi ke arah\n<----",
    "Silahkan tinggalkan pesan.",
    "Poco lg AFK,\nChat aja terus gapapah.",
    "Klo ga AFK,\npasti gw bales.\n\nTp gw lagi AFK,\nChat aja dulu...",
    "Lagi AFK!\nGa tau sampe kapan\nPaling bentar lagi",
    "Saya lagi afk coba kirim nama, nomer, sama alamat nanti saya stalk haha.",
    "Maaf, lagi AFK.\nChat aja dulu.\nnanti gw balik.",
    "Cieee yg penasaran text selanjutnya wkwk",
    "Hidup itu hanya sementara, banyak yang bisa dilakukan...\nMakanya aku lagi melakukan sesuatu..",
    "lagi AFK pak...\nklo nggak...\n\nga muncul nih pesan",
]
# =================================================================


@register(incoming=True, disable_edited=True)
async def mention_afk(mention):
    """ This function takes care of notifying the people who mention you that you are AFK."""
    global COUNT_MSG
    global USERS
    global ISAFK
    if mention.message.mentioned and not (await mention.get_sender()).bot:
        if ISAFK:
            if mention.sender_id not in USERS:
                if AFKREASON:
                    await mention.reply(f"Maaf pak lagi AFK.\
                        \nGw lagi `{AFKREASON}`")
                else:
                    await mention.reply(str(choice(AFKSTR)))
                USERS.update({mention.sender_id: 1})
                COUNT_MSG = COUNT_MSG + 1
            elif mention.sender_id in USERS:
                if USERS[mention.sender_id] % randint(2, 4) == 0:
                    if AFKREASON:
                        await mention.reply(f"I'm still AFK.\
                            \nSoalnya gw lagi `{AFKREASON}`")
                    else:
                        await mention.reply(str(choice(AFKSTR)))
                    USERS[mention.sender_id] = USERS[mention.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1
                else:
                    USERS[mention.sender_id] = USERS[mention.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1


@register(incoming=True, disable_errors=True)
async def afk_on_pm(sender):
    """ Function which informs people that you are AFK in PM """
    global ISAFK
    global USERS
    global COUNT_MSG
    if sender.is_private and sender.sender_id != 777000 and not (
            await sender.get_sender()).bot:
        if PM_AUTO_BAN:
            try:
                from userbot.modules.sql_helper.pm_permit_sql import is_approved
                apprv = is_approved(sender.sender_id)
            except AttributeError:
                apprv = True
        else:
            apprv = True
        if apprv and ISAFK:
            if sender.sender_id not in USERS:
                if AFKREASON:
                    await sender.reply(f"Maaf pak lagi AFK.\
                    \nKarena lagi `{AFKREASON}`")
                else:
                    await sender.reply(str(choice(AFKSTR)))
                USERS.update({sender.sender_id: 1})
                COUNT_MSG = COUNT_MSG + 1
            elif apprv and sender.sender_id in USERS:
                if USERS[sender.sender_id] % randint(2, 4) == 0:
                    if AFKREASON:
                        await sender.reply(f"Poco masih AFK.\
                        \nDia lagi `{AFKREASON}`")
                    else:
                        await sender.reply(str(choice(AFKSTR)))
                    USERS[sender.sender_id] = USERS[sender.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1
                else:
                    USERS[sender.sender_id] = USERS[sender.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1


@register(outgoing=True, pattern="^.afk(?: |$)(.*)", disable_errors=True)
async def set_afk(afk_e):
    """ For .afk command, allows you to inform people that you are afk when they message you """
    message = afk_e.text
    string = afk_e.pattern_match.group(1)
    global ISAFK
    global AFKREASON
    if string:
        AFKREASON = string
        await afk_e.edit(f"AFK Doloe\
        \nMau `{string}`")
    else:
        await afk_e.edit("AFK Doloe")
    if BOTLOG:
        await afk_e.client.send_message(BOTLOG_CHATID, "#AFK\nLu AFK!")
    ISAFK = True
    raise StopPropagation


@register(outgoing=True)
async def type_afk_is_not_true(notafk):
    """ This sets your status as not afk automatically when you write something while being afk """
    global ISAFK
    global COUNT_MSG
    global USERS
    global AFKREASON
    if ISAFK:
        ISAFK = False
        await notafk.respond("Gw balik.")
        await sleep(2)
        if BOTLOG:
            await notafk.client.send_message(
                BOTLOG_CHATID,
                "Lu ada " + str(COUNT_MSG) + " Pesan dari " +
                str(len(USERS)) + " pas lu AFK",
            )
            for i in USERS:
                name = await notafk.client.get_entity(i)
                name0 = str(name.first_name)
                await notafk.client.send_message(
                    BOTLOG_CHATID,
                    "[" + name0 + "](tg://user?id=" + str(i) + ")" +
                    " ngirim lu " + "`" + str(USERS[i]) + " pesan`",
                )
        COUNT_MSG = 0
        USERS = {}
        AFKREASON = None


CMD_HELP.update({
    "afk":
    ".afk [Optional Reason]\
\nUsage: Sets you as afk.\nReplies to anyone who tags/PM's \
you telling them that you are AFK(reason).\n\nSwitches off AFK when you type back anything, anywhere.\
"
})
