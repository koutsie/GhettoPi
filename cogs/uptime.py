import discord
from discord.ext import commands
import subprocess
import asyncio

class Uptime:
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='uptime')
    async def uptime(self, ctx):
        uptime = subprocess.getoutput("""uptime -p""")
        embed = discord.Embed(colour=0xFF5722)
        embed.add_field(name="Time", value="The bot has been {}{}".format(uptime, "!"))
        embed.set_author(name="Uptime", icon_url="https://cdn.discordapp.com/attachments/397570114997977098/479171019114938369/uptime2048bot.png")
        embed.set_footer(text='GhettoPi')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Uptime(bot))
