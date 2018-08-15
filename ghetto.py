import discord
from discord.ext import commands
import asyncio
import subprocess
import os
import json
import traceback
import requests
from discord.utils import find



def get_prefix(bot, message):
    prefixes = ['.']
    return commands.when_mentioned_or(*prefixes)(bot, message)

cog = ['cogs.cpu', 'cogs.help', 'cogs.kernal', 'cogs.speedtest', 'cogs.uptime', 'cogs.stats', 'cogs.owner']

bot = commands.Bot(command_prefix=get_prefix, description='A bot for something.')

if __name__ == '__main__':
    for extension in cog:
        bot.load_extension(extension)

#while True:
    #r = requests.post(url=GITHUB_API+"/gists")

@bot.event
async def on_ready():
    print("v1.04")
    print("Logged in as GhettoPi")
    while True:
        cpu = subprocess.getoutput("""/home/koutsie/Statbot/temp.sh""")
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=' cpu: ' + cpu))
        await asyncio.sleep(30)
        mem = subprocess.getoutput("""free -m  | grep ^Mem | tr -s ' ' | cut -d ' ' -f 3""")
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=' used ram: ' + mem + "mb / 400mb"))
        await asyncio.sleep(30)
        uptime = subprocess.getoutput("""uptime -p""")
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name= uptime))
        await asyncio.sleep(30)
        release = subprocess.getoutput("""uname -r""")
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=" version: " + release))
        await asyncio.sleep(30)

bot.run('', bot=True, reconnect=True)
