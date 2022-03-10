# Global Librarys
__pipList__ = []
import os
while True:
    try:
        from asyncio import Task, tasks
        import asyncio
        from distutils.log import debug
        from pickle import FALSE, TRUE
        import discord
        from discord.ext import commands
        from discord.ext import tasks
        import time
        from dotenv import load_dotenv
        import hashlib
        from datetime import datetime
        import webbrowser
    except ModuleNotFoundError as _err:
        if str(_err) in __pipList__:
            raise _err
        __pipList__.append(str(_err))
        libName = str(_err).split("'")[1]
        print("Install " + libName)
        os.system("pip install " + libName)
        os.system("pip install python-" + libName)
        continue
    break

# Local Librarys
import gitty
from dataHandler import ChancelIDs
from localDebuger import Debuger
from botmain import Debug

Debug = Debuger("BOT CLASS")

load_dotenv()

PASSWORD = os.getenv('PASSWORD')

ht = ['&status [Neuer Status] [Passwort]','&hello','&close [Passwort]','&ping','&snipe','&wipe [Nummer der Nachrichten]','&help']
hd = ['Status des Bots ändern','Keine weiter Information','Bot Abschalten','Ping','Zeigt zuletzt gelöschte Nachricht','Löscht Nachrichten(Anzahl ohne den Command)','Zeigt diese Nachricht']

class DaCommands(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.last_msg = None

    @commands.command(name="status")
    async def setstatus(self, ctx: commands.Context, *args):
        ps =  hashlib.sha256()
        ps.update(bytes(args[1],'utf-8'))
        if  str(ps.digest()) == PASSWORD:
            await ctx.channel.purge(limit=1)
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
            await Debug.Log('not working')
            return
        await guild.system_channel.send(f"Welcome, {member}!")
    
    @commands.command(name='close',pass_context=True)
    async def exits(self,ctx: commands.Context,* , pw):
        if pw == None:
            ctx.send('You are missing a password')
        ps =  hashlib.sha256()
        ps.update(bytes(pw,'utf-8'))
        if  str(ps.digest()) == PASSWORD:
            await ctx.channel.purge(limit=1)
            await ctx.send('Shutting Down')
            time.sleep(10)
            await ctx.channel.purge(limit=1)
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
    
    @commands.command(name='help')
    async def helper(self,ctx: commands.Context):
        embed = discord.Embed(title= 'Help', description=str(datetime.now()),colour = 0x87CEEB)
        for i in range(len(hd)):
            embed.add_field(name=ht[i],value=hd[i],inline=False)
        await ctx.send(embed=embed)

    @commands.command(name='git.fetch')
    async def fetch_git(self,ctx):
        if (not gitty.CheckGitIsUse()):
            await ctx.send("Git Hub is currently WIP. Pleas wait.")
            return
        changed,changes,number = gitty.botinfo()
        channelId = ChancelIDs.Load("GitCommitChannel") # 941243211056304178
        if (channelId == None):
            channel = ctx
        else:
            channel = self.bot.get_channel(channelId)
        await channel.purge(limit=100000)
        if not changed:
            return
        Debug.Log(number)
        for i in range(number):
            auth,com,allfiles,url,sha = gitty.CommitData(changes[i])
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
