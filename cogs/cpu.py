import discord
from discord.ext import commands
import subprocess
import asyncio
import requests

class CPU:
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='cpu')
    async def uptime(self, ctx):
        uptime = subprocess.getoutput("""lscpu""")
        embed = discord.Embed(colour=0xFF5722)
        r = requests.post('https://ghetto.you-dont-see.me/documents', data=uptime)
        js = r.json()
        embed.add_field(name="CPU Information", value='https://ghetto.you-dont-see.me/{}'.format(js['key']))
        embed.set_author(name="CPU", icon_url="https://cdn.discordapp.com/attachments/350607106044592132/479189377508048897/kernal2048kek.png")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(CPU(bot))
