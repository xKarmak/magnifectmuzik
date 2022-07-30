# 𝐃𝐎𝐍𝐓 𝐌𝐄𝐒𝐒 𝐖𝐈𝐓𝐇 𝐂𝐎𝐃𝐄𝐒 𝐂𝐎𝐏𝐘𝐑𝐈𝐆𝐇𝐓 @SHAILENDRA34 | 
# 𝐃𝐞𝐚𝐫 𝐏𝐞𝐫𝐨 𝐩𝐩𝐥𝐬 𝐏𝐥𝐢𝐬𝐡 𝐃𝐨𝐧'𝐭 𝐫𝐞𝐦𝐨𝐯𝐞 𝐭𝐡𝐢𝐬 𝐥𝐢𝐧𝐞 𝐟𝐫𝐨𝐦 𝐡𝐞𝐫𝐞 🌚


from helpers.filters import command
from pyrogram import Client as bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import (BOT_NAME, SUPPORT_GROUP, OWNER_USERNAME, BOT_USERNAME)


@bot.on_message(filters.command("start"))
def start_(bot, message):
    
    START_TEXT = """**⭐ Merhaba {}\n\n▫️Ben {} \n\n▫️Basit bir müzik botuyum .\n\n▫️Beni Grubunuza ekleyip yönetici yapın ve müziğin keyfini çıkarın !**"""

    START_BUTTON = [
                [
                    InlineKeyboardButton(text="🎉 Beni Gruba Ekleyin 🎉", url=f"http://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
                [
                    InlineKeyboardButton(text="📝 Destek ", url=f"https://t.me/Starbotdestek"),
                    InlineKeyboardButton(text="🇹🇷 Kanal ", url="https://t.me/StarBotKanal"),
                ],                
                [                    
                    InlineKeyboardButton(text="📚 Tüm Komutlar ", url="https://t.me/Mp3MuzikNews"),
                ],
                
            ]
    message.reply_text(
        START_TEXT.format(message.from_user.mention, BOT_NAME, SUPPORT_GROUP),
        reply_markup=InlineKeyboardMarkup(START_BUTTON)
    )
    message.delete()

@bot.on_message(filters.command("hsusueue"))
def help_(bot, message):
    HELP_TXT = """Merhaba {}\nişte yardım menüsü \nGrubuna ekleyerek müzik keyfine başlayabilirsiniz @{} sorununuz nedir? 💫"""
    
    HELP_BUTTON = [
        [
            InlineKeyboardButton(text="🕹️ Temel komutlar", callback_data="basic_"),
            InlineKeyboardButton(text="🕹️ Admin komutlar", callback_data="admin_cmd"),
        ],
        [
            InlineKeyboardButton(text="🗑 Kapat", callback_data="close_"),
            InlineKeyboardButton(text="⬅️ Geri", callback_data="HOME"),
        ],
    ]
    message.reply_text(
        HELP_TXT.format(message.from_user.first_name, SUPPORT_GROUP),
        reply_markup=InlineKeyboardMarkup(HELP_BUTTON)
    )
    message.delete()

@bot.on_callback_query()
def callback_query(Client, callback: CallbackQuery):
    if callback.data == "help_":
    
        HELP_TXT = f"""Merhaba işte yardım menüsü istediğiniz seçeneğinizi seçin ve keşfedin \nHer türlü yardım veya sorun için katılın @{SUPPORT_GROUP} Sorununuz nedir 💫?"""
    
        HELP_BUTTON = [
            [
                InlineKeyboardButton(text="🕹️ Temel komutlar", callback_data="bcd"),
                InlineKeyboardButton(text="🕹️ Admin komutlar", callback_data="admin"),
            ],
            [
                InlineKeyboardButton(text="🗑 Kapat", callback_data="close_"),
                InlineKeyboardButton(text="⬅️ Geri", callback_data="HOME"),
            ],
        ]
        callback.edit_message_text(
            HELP_TXT,
            reply_markup=InlineKeyboardMarkup(HELP_BUTTON)
        )
    elif callback.data == "HOME":
 
        START_TEXT = f"""Merhaba, ben {BOT_NAME} \nBasit ve gecikmesiz bir bottur\nHerhangi bir sorun olduğunda katılın 👉 @{SUPPORT_GROUP}\nya da help butonuna basınız  /help """
        START_BUTTON = [
                [
                    InlineKeyboardButton(text="Kanal 💫", url=f"https://t.me/SamilBots"),
                    InlineKeyboardButton(text="Beni gruba ekle ➕", url=f"http://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
                [
                    InlineKeyboardButton(text="Sahibim ⭐", url=f"https://t.me/{OWNER_USERNAME}"),
                    InlineKeyboardButton(text="Sohbet Grubu ✨", url="https://t.me/Sohbetimalfa"),
                ],                
                [                    
                    InlineKeyboardButton(text="Komutlar 🕹️", callback_data="help_"),
                ],
                
            ]
        
        callback.edit_message_text(
            START_TEXT,
            reply_markup=InlineKeyboardMarkup(START_BUTTON)
        )
    elif callback.data == "bcd":
        B_HELP = """
`ʙᴀsɪᴄ ᴄᴏᴍᴍᴀɴᴅs :- `

/oynat (Sorgu, yt linki, ses dosyası ) - bu komutu kullanın ve müziğin keyfine bakın 
/ytp (sorgu) - Daha gelişmiş muzik aramak için kullanın 
/bul (Sorgu) - Bu komutla sevdiginiz şarkıları indirebilirsiniz 
/ara (sorgu) - YouTube de arama yapar 
"""
        BUTTON = [
            [
                InlineKeyboardButton(text="🗑 Kapat", callback_data="close_"),
                InlineKeyboardButton(text="⬅️ Geri", callback_data="help_"),
            ],
        ]
        callback.edit_message_text(
            B_HELP,
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
    elif callback.data == "admin":
        A_HELP = """
`Admin komutlar :-`

/durdur - Çalan müziği durdurur
/devam - duran müziği devam ettirir
/atla - sıradaki şarkıya geçer 
/son - şarkıyı sonlandırır
/katil - asistanı gruba ekler


`Sudo komutlar :-`

/rmf - Dosyayı veri tabanından temizler 
/rmw - Veri tabanınından ham dosyaları temizler
/clean - Dosyaları sunucudan temizler
/gcast - küresel mesaj yayınlamak için 
"""
        BUTTON = [
            [
                InlineKeyboardButton(text="🗑 kapat", callback_data="close_"),
                InlineKeyboardButton(text="⬅️ Geri", callback_data="help_"),
            ],
        ]
        callback.edit_message_text(
            A_HELP,
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
    elif callback.data == "close_":
        callback.message.delete()
