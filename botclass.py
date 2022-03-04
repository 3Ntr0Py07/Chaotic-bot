from attr import attributes
import discord
from discord.ext import commands


class DaCommands(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command(name='hello')
    async def hello(ctx: commands.context):
        await ctx.reply('hello')

    @commands.command(name="ping")
    async def ping(ctx: commands.Context):
        await ctx.send(f'ping! ' + str(round(commands.latency * 1000)) + 'ms')

    @commands.command(name='close')
    async def exits(ctx: commands.Context):
        await ctx.send('Closed')
        await quit()

    '''@commands.event()
    async def on_ready(self, ctx: commands.Context):
        await self.bot.change_presence(activity=discord.Game(name='.nothin'))

'''
def setup(client: commands.Bot):
    client.add_cog(DaCommands(client))