# 𝐃𝐎𝐍𝐓 𝐌𝐄𝐒𝐒 𝐖𝐈𝐓𝐇 𝐂𝐎𝐃𝐄𝐒 𝐂𝐎𝐏𝐘𝐑𝐈𝐆𝐇𝐓 @Samilben | 
# 𝐃𝐞𝐚𝐫 𝐏𝐞𝐫𝐨 𝐩𝐩𝐥𝐬 𝐏𝐥𝐢𝐬𝐡 𝐃𝐨𝐧'𝐭 𝐫𝐞𝐦𝐨𝐯𝐞 𝐭𝐡𝐢𝐬 𝐥𝐢𝐧𝐞 𝐟𝐫𝐨𝐦 𝐡𝐞𝐫𝐞 🌚
 
 
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
        sas = await message.reply("`Yayın başlıyor, bekleyiniz ‍💻`")
        if not message.reply_to_message:
            await sas.edit("**__Herhangi bir mesajı bana ver__**")
            return
        hero = message.reply_to_message.text
        async for dialog in Client.iter_dialogs():
            try:
                await Client.send_message(dialog.chat.id, hero)
                sent = sent+1
                await hyper.edit(f"`Yayınlanıyor` \n\n**Başarılı :** `{sent}` Sohbetler👾 \n**Başarısız :** {failed} Sohbetler🗑️")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_photo(HERO_IMG, caption=f"Başarıyla yapıldı🧚‍♀⭐ \n\nBaşarılı**:** `{sent}` Sohbetler \n**başarısız☹️ :** {failed} Sohbetler")
