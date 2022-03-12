
# Global Librarys
__pipList__ = []
import os
while True:
    try:
        import discord
        from discord.ext import commands
        from dotenv import load_dotenv
        import threading
    except ModuleNotFoundError as _err:
        if str(_err) in __pipList__:
            raise _err
        __pipList__.append(str(_err))
        libName = str(_err).split("'")[1]
        print("Install " + libName)
        os.system("pip install " + libName)
        os.system("pip install python-" + libName)
        os.system("pip install py" + libName)
        continue
    break

# Local Librarys
import botclass
from localDebuger import Debuger

Debug = Debuger("BOT MAIN")

load_dotenv()
tken = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='&', intents =intents)
client.remove_command('help')
client.load_extension('botclass')
@client.event
async def on_ready():
    Debug.Log(f'{Debug.Colors.BLUE}OK{Debug.Colors.ENDC}')
    #print('Messages')
    #client.loop.create_task(botclass.fetchenable())
    pass


#print('\n'+tken+'\n')

client.run(tken)
try:
    botclass.ShutdownBot()
except Exception as _err:
    print("3")
    print(_err.with_Traceback(None))
    os.system("pause")
    print("4")
print("5")
os.system('clear')
print("6")

