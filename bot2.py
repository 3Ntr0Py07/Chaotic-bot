import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')

@bot.command()
async def hello(ctx):
    await ctx.reply('Hello')

bot.run(TOKEN)
print('running')
os.system('pause')