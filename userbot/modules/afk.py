# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module which contains afk-related commands """
from random import choice, randint
from asyncio import sleep
from datetime import datetime

from telethon.events import StopPropagation

from userbot import (AFKREASON, COUNT_MSG, CMD_HELP, ISAFK, BOTLOG,
                     BOTLOG_CHATID, USERS, PM_AUTO_BAN)
from userbot.events import register

# ========================= CONSTANTS ============================
AFKSTR = [
    "Saya sedang sibuk sekarang. jika sangat penting anda bisa kirim nomor whatsapp pacarmu!\n#Bot",
    "Saya sedang tidak online sekarang. Jika memang penting, Tinggalkan pesan setelah bunyi beep:\n`beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeep`!\n#Bot",
    "Mungkin belum saatnya kita bertemu.\n#Bot",
    "Aku Akan Balik Sebentar Lagi dan Jika tidak...,\ntunggulah lebih lama :v.\n#Bot",
    "Aku sedang tidak disini. \nYang pasti Aku sedang berada di suatu tempat.\n#Bot",
    "Aku bukan orang yang spesial tapi aku selalu ada bersamamu,Kecuali sekarang aja sih.\n#Bot",
    "Ada 3 hal di duinia ini yang tidak bisa kuhitung, jumlah bintang di langit, ikan di laut dan cintaku padamu.\n#Bot",
    "Rasa sayangku ke kamu kaya pas powerangers waktu gak ada monster nggak berubah.\n#Bot",
    "Coba cari aku kearah ini\n---->\n#Bot",
    "Coba cari aku kearah ini\n<----\n#Bot",
    "Mohon Tinggalkan Pesan Yang penting kepadaku, Jika Tak Penting Ya udah.\n#Bot",
    "Sudah! Jangan ada hubungan lagi, Aku tau kau selingkuh!.\n#Bot",
    "Jika Aku Onlen,Aku bakal memberitahumu dimana aku.\nTapi aku tidak, \nJadi tanyakan aku saat aku kembali...\n#Bot",
    "Aku Pergi!\nAku tidak tahu kapan aku kembali!\nKuharap Beberapa menit setelah pesan ini!\n#Bot",
    "Ane lagi Gak Ada Sekarang :(, \nJadi Harap lampirkan Nama, alamat, nomer wa pacarmu, dan sertakan fotonya ya!\n#Bot",
    "Maap Yak, Ane Lagi kagak Disini,\nJadi Rasakan Kebebasan Mengobrol Dengan Userbot Ku ini.\nDan Aku akan kembali sebentar lagi.\n#Bot",
    "Aku Yakin Kamu Menunggu pesan balasan dariku!\n#Bot",
    "Hidup sangatlah singkat,\nPerbanyak lah hidup ini dengan ibadah..\nJangan nonton JAV mulu!\n#Bot",
    "Aku tidak disini sekarang..\nTetapi Jika Aku disini...\nMemang kamu mau menjalin hubungan kembali denganku?\n#Bot",
]
# =================================================================


@register(incoming=True, disable_edited=True)
async def mention_afk(mention):
    """ This function takes care of notifying the people who mention you that you are AFK."""
    global COUNT_MSG
    global USERS
    global ISAFK
    global afk_time
    global afk_start
    global afk_end
    not_afk = datetime.now()
    afk_end = not_afk.replace(microsecond=0)
    if mention.message.mentioned and not (await mention.get_sender()).bot:
        if ISAFK:
            now = datetime.now()
            afk_since = now - afk_time
            day = float(afk_since.seconds) // (24 * 3600)
            time = float(afk_since.seconds) % (24 * 3600)
            hours = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            seconds = time
            if day == 1:
                afk_str = "Yesterday"
            elif day > 1:
                if day > 6:
                    date = now + \
                        datetime.timedelta(
                            days=-day, hours=-hours, minutes=-minutes)
                    afk_str = date.strftime("%A, %Y %B %m, %H:%I")
                else:
                    wday = now + datetime.timedelta(days=-day)
                    afk_str = wday.strftime('%A')
            elif hours > 1:
                afk_str = f"`{int(hours)}Jam{int(minutes)}Menit` Lalu"
            elif minutes > 0:
                afk_str = f"`{int(minutes)}Menit{int(seconds)}Detik` Lalu"
            else:
                afk_str = f"`{int(seconds)}Detik` Lalu"
            if mention.sender_id not in USERS:
                if AFKREASON:
                    await mention.reply("[Offline]"
                                        f"\nKarena : `{AFKREASON}`."
                                        f"\nOffline Sejak: {afk_str}")
                else:
                    await mention.reply(str(choice(AFKSTR)))
                USERS.update({mention.sender_id: 1})
                COUNT_MSG = COUNT_MSG + 1
            elif mention.sender_id in USERS:
                if USERS[mention.sender_id] % randint(2, 4) == 0:
                    if AFKREASON:
                        await mention.reply("[Offline]"
                                            f"\nKarena: `{AFKREASON}`."
                                            f"\nOffline Sejak: {afk_str}")
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
    global afk_time
    global afk_start
    global afk_end
    not_afk = datetime.now()
    afk_end = not_afk.replace(microsecond=0)
    afk_str = "a while ago"
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
            now = datetime.now()
            afk_since = now - afk_time
            day = float(afk_since.seconds) // (24 * 3600)
            time = float(afk_since.seconds) % (24 * 3600)
            hours = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            seconds = time
            if day == 1:
                afk_str = "Yesterday"
            elif day > 1:
                if day > 6:
                    date = now + \
                        datetime.timedelta(
                            days=-day, hours=-hours, minutes=-minutes)
                    afk_since = date.strftime("%A, %Y %B %m, %H:%I")
                else:
                    wday = now + datetime.timedelta(days=-day)
                    afk_str = wday.strftime('%A')
            elif hours > 1:
                afk_str = f"`{int(hours)}Jam{int(minutes)} Menit` Lalu"
            elif minutes > 0:
                afk_str = f"`{int(minutes)}Menit{int(seconds)}Detik` Lalu"
            else:
                afk_str = f"`{int(seconds)}Detik` Lalu"
            if sender.sender_id not in USERS:
                if AFKREASON:
                    await sender.reply("[Offline]"
                                       f"\nKarena: `{AFKREASON}`."
                                       f"\nOffline Sejak: {afk_str}")
                else:
                    await sender.reply(str(choice(AFKSTR)))
                USERS.update({sender.sender_id: 1})
                COUNT_MSG = COUNT_MSG + 1
            elif apprv and sender.sender_id in USERS:
                if USERS[sender.sender_id] % randint(2, 4) == 0:
                    if AFKREASON:
                        await sender.reply("[Offline]"
                                           f"\nKarena: `{AFKREASON}`."
                                           f"\nOffline Sejak: {afk_str}")
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
    global afk_time
    global afk_start
    global afk_end
    afk_time = None
    afk_end = {}
    start1 = datetime.now()
    afk_start = start1.replace(microsecond=0)
    if string:
        AFKREASON = string
        await afk_e.edit(f"[Offline]\
        \nKarena: `{string}`")
    else:
        await afk_e.edit("[Offline]")
    if BOTLOG:
        await afk_e.client.send_message(BOTLOG_CHATID, "#AFK\nAnda Offline")
    ISAFK = True
    afk_time = datetime.now()
    raise StopPropagation


@register(outgoing=True)
async def type_afk_is_not_true(notafk):
    """ This sets your status as not afk automatically when you write something while being afk """
    global ISAFK
    global COUNT_MSG
    global USERS
    global AFKREASON
    global afk_time
    global afk_start
    global afk_end
    not_afk = datetime.now()
    afk_end = not_afk.replace(microsecond=0)
    if ISAFK:
        ISAFK = False
        msg = await notafk.respond("[Online]")
        await sleep(1)
        await msg.delete()
        if BOTLOG:
            await notafk.client.send_message(
                BOTLOG_CHATID,
                "Anda menerima " + str(COUNT_MSG) + " Pesan Dari " +
                str(len(USERS)) ",
            )
            for i in USERS:
                name = await notafk.client.get_entity(i)
                name0 = str(name.first_name)
                await notafk.client.send_message(
                    BOTLOG_CHATID,
                    "[" + name0 + "](tg://user?id=" + str(i) + ")" +
                    " Mengirimkan" + "`" + str(USERS[i]) + " Pesan`",
                )
        COUNT_MSG = 0
        USERS = {}
        AFKREASON = None


CMD_HELP.update({
    "afk":
    ".afk [Optional Reason]\
\nUsage: Mengatur status Menjadi AFK.\nMenjawab Ke Orang Yang Merepli Kamu Atau PM \
Memberi Tahu Bahwa Kamu AFK dengan(alasan).\n\n Otomatis MeMatikan AFK saat Anda mengetik kembali apa pun, di mana saja , Eh benerkan Gini? ðŸ˜‚.\
"
})
