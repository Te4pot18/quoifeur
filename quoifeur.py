import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='+', description="quoifeur")

@bot.event
async def on_ready():
    print('Bot ON')
    await bot.change_presence(activity=discord.Streaming(name=f'By Teapot', url='https://www.twitch.tv/tt'))

@bot.event 
async def on_message(message):
    if "quoi" in message.content or "Quoi" in message.content:
        await message.reply('feur !')

bot.run("")