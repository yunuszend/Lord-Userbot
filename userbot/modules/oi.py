from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^.yunus(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai Perkenalkan Namaku yunus`")
    sleep(3)
    await typew.edit("`Aku Adalah Kang Sadboy :(`")
    sleep(1)
    await typew.edit("`Btw Salam kenal yah | asal ku dari Padang:)`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.tolol(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Kamu Itu TOLOL!!`")
    sleep(1)
    await typew.edit("`HAHAHAHAHAHA MAMPUS 🏹`")
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
