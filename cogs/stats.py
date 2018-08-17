import discord
from discord.ext import commands
import subprocess
import asyncio
import json
import requests
import time
from datetime import datetime

class Stats:
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='stats')
    async def kernal(self, ctx):
        mem = subprocess.getoutput("""free -m  | grep ^Mem | tr -s ' ' | cut -d ' ' -f 3""")
        cpu = subprocess.getoutput("""/home/koutsie/Statbot/temp.sh""")
        uptime = subprocess.getoutput("""uptime -p""")
        embed = discord.Embed(title="Stats", colour=0xFF5722)
        embed.add_field(name="CPU Temp", value=cpu)
        embed.add_field(name="Memory", value=mem)
        embed.add_field(name="Uptime", value=uptime)
        embed.add_field(name="Gist Stats", value="gistlink")
        header = {'Content-Type': 'application/json', 'Authorization': 'githubapi'}
        await ctx.send(embed=embed)
        data = {"description": "Stats for GhettoPi", "files":{"Stats":{"content": "servers={}\ncpu={}\nmaxmem={}\nmemory={}".format(self.bot.guilds, cpu, '400MB', mem)}}}
        while True:
            r = requests.patch(url='gistlink', headers=header, data=json.dumps(data))
            print("posting")
            print(r.text)
            await asyncio.sleep(30)

    @commands.command()
    async def ping(self, ctx):
        t1 = time.perf_counter()
        await ctx.channel.trigger_typing()
        t2 = time.perf_counter()
        pong = f"<:thinkpings:468089741754236950> **Pong!** `{str(round((t2 - t1) * 1000))}ms`"
        embed = discord.Embed(description=pong, color=0xFF5722)
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Stats(bot))
