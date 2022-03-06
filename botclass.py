from asyncio import Task, tasks
import os
from pickle import FALSE, TRUE
import discord
from discord.ext import commands
from discord.ext import tasks
import time
from dotenv import load_dotenv
import hashlib
import gitty
from datetime import datetime
import webbrowser

load_dotenv()

PASSWORD = os.getenv('PASSWORD')



class DaCommands(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.last_msg = None

    @commands.command(name="status")
    async def setstatus(self, ctx: commands.Context, *args):
        ps =  hashlib.sha256()
        ps.update(bytes(args[1],'utf-8'))
        if  str(ps.digest()) == PASSWORD:
            await ctx.channel.purge(limit=2)
            await ctx.send(f'Status changed to {args[0]}')
            await self.bot.change_presence(activity=discord.Game(name=args[0]))
        else:
            await ctx.send('You cannot do that')                 

    @commands.command(name='hello',pass_context=True)
    async def hello(self,ctx: commands.Context,):
        await ctx.reply('hello')      

    @commands.Cog.listener()
    async def on_guild_join(self, guild, member):
        if not guild.system_channel:
            await print('not working')
            return
        await guild.system_channel.send(f"Welcome, {member}!")
    
    @commands.command(name='close',pass_context=True)
    async def exits(self,ctx: commands.Context,* , pw: str):
        ps =  hashlib.sha256()
        ps.update(bytes(pw,'utf-8'))
        if  str(ps.digest()) == PASSWORD:
            await ctx.channel.purge(limit=2)
            await ctx.send('Shutting Down')
            await ctx.bot.logout()
        else:
            await ctx.send('You cannot do that')

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        start_time = time.time()
        message = await ctx.send("Testing Ping...")
        end_time = time.time()

        await message.edit(content=f"Ping: {round(self.bot.latency * 1000)}ms\nAPI: {round((end_time - start_time) * 1000)}ms")
    

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        self.last_msg = message

    @commands.command(name="snipe")
    async def snipe(self, ctx: commands.Context):
        if not self.last_msg:  # on_message_delete hasn't been triggered since the bot started
            await ctx.send("There is no message to snipe!")
            return

        author = self.last_msg.author
        content = self.last_msg.content

        embed = discord.Embed(title=f"Message from {author}", description=content)
        await ctx.send(embed=embed)
    
    @commands.command(name='wipe')
    async def wipe(self, ctx, number):
        n = int(number)
        await ctx.channel.purge(limit=n+1)
    
    @commands.command(name='fetch')
    async def fetch_git(self,ctx):
        self.loop.create_task(fetch_git())


    
    @commands.command(name='join')
    async def jn(self,ctx:commands.Context,*,link:str):
        webbrowser.open(link)
    # @commands.event()
    #async def on_ready(self, ctx: commands.Context):
    #   await self.bot.change_presence(activity=discord.Game(name='.nothin'))



async def fetch_git(self,):
    changed,changes,number = gitty.botinfo()
    channel = self.bot.get_channel(946895128545624207)
    await channel.purge(limit=100000)
    if not changed:
        return
    for i in range(number):

        auth,curl,com,committer,allfiles,url,parents,sha = gitty.CommitData(changes[i])
            #print(f'{gitty.colors.CYAN}'+sha+f'{gitty.colors.ENDC}')
        embed = discord.Embed(title= 'Commit: '+ str(sha), description=str(datetime.now()),colour = 0x87CEEB)
        fstring = ''
        allc = ''
        alls = ''
        for x in range(len(allfiles)):
            fstring += 'SHA: ' + allfiles[x][0] + '\n'
            fstring += 'File: ' + allfiles[x][1] + '\n\n'
        embed.add_field(name='Author',value=auth, inline=True)
        embed.add_field(name='Description',value=str(com.message), inline=False)
        
        if not fstring == '':
            if len(fstring)<1024:
                embed.add_field(name='Files',value=fstring, inline=False)
            else:
                embed.add_field(name='Files',value='To Many To Display',inline=False)
        embed.add_field(name='URL',value=url, inline=False)
        await channel.send(embed=embed)



def setup(client: commands.Bot):
    client.add_cog(DaCommands(client))