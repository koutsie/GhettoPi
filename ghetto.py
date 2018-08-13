import discord
import asyncio
import os
import subprocess
import json
import traceback
import subprocess
from discord.ext import commands
import logging

logging.basicConfig(level=logging.CRITICAL)
#from botconf import Conf

client = discord.Client()

@client.event
async def on_ready():
    print("v1.03")
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("Logged into", len(client.servers), "servers")
    while True:
        servers = str(len(client.servers))
        users = str(len(set(client.get_all_members())))
        await client.change_presence(game=discord.Game(name=' Bootup: See logs!', type=1, url='https://twitch.tv/koutsie'))
        await asyncio.sleep(20)
        await client.change_presence(game=discord.Game(name='over ' + servers + ' shards...', type=2, url='https://opi,koutsie.eu/'))
        await asyncio.sleep(20)
        await client.change_presence(game=discord.Game(name='the ' + users + ' users', type=2, url='https://opi,koutsie.eu/'))
        await asyncio.sleep(20)
        await client.change_presence(game=discord.Game(name='logs...', type=2, url='https://opi,koutsie.eu/'))
        await asyncio.sleep(30)
        await client.change_presence(game=discord.Game(name=' https://opi.koutsie.eu/', type=2, url='https://https://opi,koutsie.eu/'))
        await asyncio.sleep(20)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('.neo'):
        msg = await client.send_message(message.channel, 'Please wait (Stage 1/3 - Running ./neo.sh)')
        subprocess.getoutput("./neo.sh")
        await client.edit_message(msg, 'Please wait (Stage 2/3 - Copiling output)')
        await asyncio.sleep(1.5)
        await client.edit_message(msg, 'Please wait (Stage 3/3 - Uploading...)')
        await asyncio.sleep(1)
        link = open('link.link').read().splitlines()
        await client.edit_message(msg, link)
        await asyncio.sleep(5)
        subprocess.getoutput("> link.link")
        return

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('.help'):
        await client.send_message(message.channel, """```
+------------------------------------------------------------------------+
|             _____  _            _    _          _____  _               |
|             / ____++ +          + +  + +        +  __ \(_)             |
|            + +  __ | +__    ___ | +_ | +_  ___  | +__) +_              |
|            | | +_ ++ '_ \  / _ \| __++ __+/ _ \ |  ___/| +             |
|            + +__+ || + + ++  __/+ +_ + +_| (_) ++ +    | |             |
|             \_____++_+ +_+ \___+ \__+ \__+\___/ +_+    +_+             |
|                                                                        |
+------------------------------------------------------------------------+
|                                                                        |
| .help - Shows this help menu                                           |
|                                                                        |
| .neo - Fetches system info                                             |
|                                                                        |
| .speedtest - Runs a speedtest                                          |
|                                                                        |
|                                                                        |
|                                                                   1.03 |
+------------------------------------------------------------------------+
```""")
        return

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('.speedtest'):
        msg = await client.send_message(message.channel, 'Running: `speedtest-cli`')
        speed = subprocess.getoutput("speedtest-cli --simple")
        await client.edit_message(msg, '```' + speed + '```')


client.run('')
