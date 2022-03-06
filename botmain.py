import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import botclass

#esc = True
load_dotenv()
tken = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='.', intents =intents)
client.load_extension('botclass')
@client.event
async def on_ready():
    pass

#print('\n'+tken+'\n')

try:
    client.run(tken)
except RuntimeError('Event loop is closed'):
    os.system('clear')
    quit()
