from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^.yunus(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hallo Perkenalkan Nama Aku Yunus`")
    sleep(3)
    await typew.edit("`Hmm Aku Adalah Seorang Sadboy`")
    sleep(1)
    await typew.edit("`Aku Tinggal di Padang Salam Kenal Yah:)`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.lebay(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Lebay Gbblk`")
    sleep(3)
    await typew.edit("`Dasar Tolol,ngapain kek gitu!!?`")
    sleep(1)
    await typew.edit("`Dasar Lebay Alay Pulak Tuh🐒`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur`")
# Create by myself @localheart
