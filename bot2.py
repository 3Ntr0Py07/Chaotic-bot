import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
#import yeet

#esc = True

#TOKEN = os.getenv('DISCORD_TOKEN')


class myclient(discord.Client):
    
    async def on_ready(ctx):
        print('ok')
    
    async def on_member_join(ctx, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
            await guild.Allgemein.send(to_send)

    async def on_message(ctx, self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith('.hello'):
            await message.reply('Hello!', mention_author=True)


intents = discord.Intents.default()
intents.members = True
#intents.all = True
client = myclient(intents=intents)
client.run('OTQ2NzgzMTAyMTQxODc0MjU2.YhjueQ.ZYkX3R20ZLWm4Lro6oU_Z65UFzU')