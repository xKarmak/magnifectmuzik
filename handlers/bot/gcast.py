# ππππ ππππ ππππ πππππ πππππππππ @Samilben | 
# ππππ« πππ«π¨ π©π©π₯π¬ ππ₯π’π¬π‘ ππ¨π§'π­ π«ππ¦π¨π―π π­π‘π’π¬ π₯π’π§π ππ«π¨π¦ π‘ππ«π π
 
 
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant
from config import SUDO_USERS

HERO_IMG = "https://telegra.ph/file/d9a88ee1910a034c62c79.jpg"

@Client.on_message(filters.command("gcast"))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        sas = await message.reply("`YayΔ±n baΕlΔ±yor, bekleyiniz βπ»`")
        if not message.reply_to_message:
            await sas.edit("**__Herhangi bir mesajΔ± bana ver__**")
            return
        hero = message.reply_to_message.text
        async for dialog in Client.iter_dialogs():
            try:
                await Client.send_message(dialog.chat.id, hero)
                sent = sent+1
                await hyper.edit(f"`YayΔ±nlanΔ±yor` \n\n**BaΕarΔ±lΔ± :** `{sent}` SohbetlerπΎ \n**BaΕarΔ±sΔ±z :** {failed} SohbetlerποΈ")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_photo(HERO_IMG, caption=f"BaΕarΔ±yla yapΔ±ldΔ±π§βββ­ \n\nBaΕarΔ±lΔ±**:** `{sent}` Sohbetler \n**baΕarΔ±sΔ±zβΉοΈ :** {failed} Sohbetler")
