from time import time
from datetime import datetime
from config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from helpers.decorators import authorized_users_only


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>✨ **Welcome {message.from_user.first_name}** \n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) memungkinkan Anda memutar musik di grup melalui obrolan suara telegram baru !**

💡 **temukan semua perintah bot dan cara kerjanya dengan mengklik » 📚 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗯𝘂𝘁𝘁𝗼𝗻 !**

❓ **untuk informasi tentang semua fitur boot ini ketik saja /help**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ Tambahkan saya ke Grup Anda ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                         "📚 Perintah", url="https://telegra.ph/KEK-MUSIC-GUIDE-08-25"
                    ),
                    InlineKeyboardButton(
                        "💝 Donate", url=f"https://t.me/Biarenakliatnyaaa")
                ],[
                    InlineKeyboardButton(
                        "👥 Official Group", url=f"https://t.me/Jarak_Virtual"
                    ),
                    InlineKeyboardButton(
                        "📣 Official Channel", url=f"https://t.me/storeglitter")
                ],[
                    InlineKeyboardButton(
                        "📌 Click to ask", url="https://t.me/Biarenakliatnyaaa")
                ],[
                    InlineKeyboardButton(
                        "🧪 Source Code 🧪", url="https://t.me/Virtuallnihboss"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""✅ **bot sedang berjalang**\n<b>💠 **uptime:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✨ Group", url=f"https://t.me/Jarak_Virtual"
                    ),
                    InlineKeyboardButton(
                        "📣 Channel", url=f"https://t.me/storeglitter"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 **Hello** {message.from_user.mention()}, **silakan ketuk tombol di bawah ini untuk melihat pesan bantuan yang dapat Anda baca untuk menggunakan bot ini**</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="❔ BAGAIMANA MENGGUNAKAN SAYA", url=f"https://t.me/{BOT_USERNAME}?start=help"
                    )
                ]
            ]
        )
    )

@Client.on_message(command("help") & filters.private & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hello {message.from_user.mention()}, welcome to help menu ✨
\n📙 HOW TO USE ME ?
\n1. first add me to your group.
2. promote me as admin and give all permission.
3. then, add @{ASSISTANT_NAME} to your group or type /userbotjoin.
3. make sure you turn on the voice chat first before start playing music.
\n💁🏻‍♀️ **commands for all user:**
\n/play (song name) - play song from youtube
/ytp (song name) - play song from youtube directly
/stream (reply to audio) - play song using audio file
/playlist - show the list song in queue
/song (song name) - download song from youtube
/search (video name) - search video from youtube detailed
/vsong (video name) - download video from youtube detailed
/lyric - (song name) lyrics scrapper
/vk (song name) - download song from inline mode
\n👷🏻‍♂️ **commands for admins:**
\n/player - show the music playing status
/pause - pause the music streaming
/resume - resume the music was paused
/skip - skip to the next song
/end - stop music streaming
/userbotjoin - invite assistant join to your group
/reload - for refresh the admin list
/cache - for cleared admin cache
/auth - authorized user for using music bot
/deauth - unauthorized for using music bot
/control - open the player settings panel
/delcmd (on | off) - enable / disable del cmd feature
/silent - mute the music player on voice chat
/unsilent - unmute the music player on voice chat
/musicplayer (on / off) - disable / enable music player in your group
\n🎧 channel streaming commands:
\n/cplay - stream music on channel voice chat
/cplayer - show the song in streaming
/cpause - pause the streaming music
/cresume - resume the streaming was paused
/cskip - skip streaming to the next song
/cend - end the streaming music
/admincache - refresh the admin cache
\n🧙‍♂️ command for sudo users:
\n/userbotleaveall - order the assistant to leave from all group
/gcast - send a broadcast message trought the assistant
/stats - show the bot statistic
\n👨🏻‍✈️ owner only:
\n/broadcast - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot
\n🎊 **commands for fun:**
\n/chika - check it by yourself
/wibu - check it by yourself
/randomh - check it by yourself
/asupan - check it by yourself
/truth - check it by yourself
/dare - check it by yourself
\n💡 version 0.6.5 (latest)
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✨ GROUP", url=f"https://t.me/Jarak_Virtual"
                    ),
                    InlineKeyboardButton(
                        "📣 CHANNEL", url=f"https://t.me/storeglitter"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👩🏻‍💻 DEVELOPER", url=f"https://t.me/Biarenakliatnyaaa"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "🏓 `SEPONG!!`\n"
        f"⚡️ `{delta_ping * 1000:.3f} ms`"
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@authorized_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status: ✅ Online\n\n"
        f"• **⏳uptime:** `{uptime}`\n"
        f"• **⏱️start time:** `{START_TIME_ISO}`"
    )
