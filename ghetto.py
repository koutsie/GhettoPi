import discord
from discord.ext import commands
import asyncio
import subprocess
import os
import json
import traceback
from discord.utils import find


bot = commands.Bot(command_prefix='.',pm_help = False)
client = discord.Client()

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
        release = subprocess.getoutput("""uname -r""")
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=" version: " + release))
        await asyncio.sleep(30)

@bot.event
async def on_message(message):
        if message.author.bot:
                return
        elif message.content == "<@478195294631231488>":
                await message.channel.send("Yes im alive!")

@bot.event
async def on_message(message):
        if message.author.bot:
                return
        elif message.content == ".uptime":
                uptime = subprocess.getoutput("""uptime -p""")
                await message.channel.send(uptime)


@bot.event
async def on_message(message):
        if message.author.bot:
                return
        elif message.content == ".speedtest":
            speedtest = subprocess.getoutput("""speedtest-cli --simple""")
            await message.channel.send(speedtest)
            await asyncio.sleep(1200)

@bot.event
async def on_message(message):
        if message.author.bot:
                return
        elif message.content == ".kernel":
                release = subprocess.getoutput("""uname -r""")
                await message.channel.send(release)
                
@bot.event
async def on_message(message):
        if message.author.bot:
                return
        elif message.content == ".help":
                helps = "https://opi.koutsie.eu/"
                await message.channel.send(helps)

bot.run('')
