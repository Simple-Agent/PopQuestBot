import discord
from discord.ext import commands
import random

# Bot setup
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Initialize users data
users_data = {}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    await bot.process_commands(message)

    # Simulate gaining XP
    user_id = str(message.author.id)
    if user_id not in users_data:
        users_data[user_id] = {'xp': 0, 'level': 1}
    users_data[user_id]['xp'] += random.randint(10, 20)
    await check_level_up(user_id, message.channel)

async def check_level_up(user_id, channel):
    user_data = users_data[user_id]
    xp, level = user_data['xp'], user_data['level']
    next_level_xp = level * 100
    if xp >= next_level_xp:
        user_data['level'] += 1
        await channel.send(f'{channel.guild.get_member(int(user_id)).mention} has leveled up to level {level + 1}!')

token = 'YOUR_BOT_TOKEN_HERE'

bot.run(token)
