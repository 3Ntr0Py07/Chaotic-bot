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

bot.run('OTQ2NzgzMTAyMTQxODc0MjU2.YhjueQ.0KTAuCEYdvkwNVFL9dSuz4VNBb0')
print('running')
os.system('pause')