import discord
import random
from discord.ext import commands

# Aktifkan permission untuk membaca pesan
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Daftar auto-balas: kata kunci => daftar respon
auto_responses = {
    "halo": [
        "Halo juga!",
        "Hai hai~ 👋",
        "Selamat datang! 😊"
    ],
    "makasih": [
        "Sama-sama!",
        "Senang bisa membantu!",
        "Kapan-kapan bantu aku balik ya 😄"
    ],
    "bye": [
        "Sampai jumpa!",
        "Jangan lupa kembali ya!",
        "Dadah 👋"
    ]
}

# (Optional) ID channel tertentu untuk auto-balas
allowed_channel_ids = []  # Contoh: [123456789012345678]

@bot.event
async def on_ready():
    print(f'✅ Bot {bot.user} sudah aktif!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # (Optional) Batasi hanya di channel tertentu
    if allowed_channel_ids and message.channel.id not in allowed_channel_ids:
        return

    msg = message.content.lower()

    # Cek apakah ada kata kunci dalam pesan
    for keyword, responses in auto_responses.items():
        if keyword in msg:
            response = random.choice(responses)
            await message.channel.send(f'{response}')
            break  # Stop setelah menemukan satu keyword

    await bot.process_commands(message)

# Jalankan bot
bot.run('TOKEN_BOT_KAMU')
