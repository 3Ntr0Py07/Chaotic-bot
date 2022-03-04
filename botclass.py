import os
import discord
from discord.ext import commands
import time



class DaCommands(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.last_msg = None

    @commands.command(name="status")
    @commands.has_role('The One and Only Entropy')
    async def setstatus(self, ctx: commands.Context, *, text: str):
        await self.bot.change_presence(activity=discord.Game(name=text))

    @commands.command(name='hello',pass_context=True)
    async def hello(self,ctx: commands.Context):
        await ctx.reply('hello')

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = self.bot.get_channel(946895128545624207)

        if not channel:
            await print('not working')
            return

        await channel.send(f"Welcome, {member}!")

    @commands.command(name='close',pass_context=True)
    @commands.has_role('The One and Only Entropy')
    async def exits(self,ctx: commands.Context):
        await ctx.send('Closed')
        try:
            await quit()
        except:
            os.system('clear')

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
   # @commands.event()
    #async def on_ready(self, ctx: commands.Context):
     #   await self.bot.change_presence(activity=discord.Game(name='.nothin'))


def setup(client: commands.Bot):
    client.add_cog(DaCommands(client))