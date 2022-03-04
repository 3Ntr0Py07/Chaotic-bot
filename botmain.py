import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

#esc = True
load_dotenv()
tken = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='.', intents =intents)
client.load_extension('botclass')
print('\n'+tken+'\n')
client.run(tken)
