import discord
from discord.ext import commands
import subprocess
import asyncio

class Kernal:
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='kernal')
    async def kernal(self, ctx):
        release = subprocess.getoutput("""uname -r""")
        embed = discord.Embed(colour=0xFF5722)
        embed.add_field(name="Kernal", value="{}".format(release))
        embed.set_author(name="Kernal Info", icon_url="https://cdn.discordapp.com/attachments/397570114997977098/479176660772454400/info2048bot.png")
        embed.set_footer(text='GhettoPi')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Kernal(bot))
