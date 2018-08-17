import discord
from discord.ext import commands
import subprocess
import asyncio
import speedtest

class Speedtest:
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='speedtest')
    async def speedtest(self, ctx):
        s = speedtest.Speedtest()
        s.get_best_server()
        s.download()
        s.upload()
        speed = s.results.share()
        embed = discord.Embed(colour=0xFF5722)
        embed.set_image(url=speed)
        embed.set_author(name="Speedtest", icon_url="https://cdn.discordapp.com/attachments/397570114997977098/479171018116562944/speedtest2048bot.png")
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Speedtest(bot))
