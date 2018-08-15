import discord
from discord.ext import commands
import subprocess
import asyncio

class Help:
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='Help')
    async def help(self, ctx):
        embed = discord.Embed(title='Help',
                              description="All the commands are avaliable at our site.",
                              colour=0xFF5722)
        embed.add_field(name="Website", value="https://opi.koutsie.eu/")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/397570114997977098/479171019114938368/help2048bot.png")
        embed.set_footer(text='GhettoPi')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
