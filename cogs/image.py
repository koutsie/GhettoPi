import os
from PIL import Image, ImageDraw, ImageFont
import discord
from discord.ext import commands
import subprocess
import requests
import asyncio
from datetime import datetime
from pymongo import MongoClient
size = 228, 228

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.GhettoPi
biodb = db.bioset

class Profile:
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='profile')
    async def profile(self, ctx):
        invoker = str(ctx.message.author)
        fontsize = 45
        data = biodb.find_one({"_id": int(ctx.message.author.id)})
        await ctx.trigger_typing()
        url = "https://cdn.discordapp.com/avatars/{}/{}.{}".format(ctx.message.author.id, ctx.guild.get_member(ctx.message.author.id).avatar, 'jpg')
        response = requests.get(url)
        if response.status_code == 200:
            with open("/root/GhettoPi/Profiles/{}.jpg".format(str(ctx.message.author.id)), 'wb') as f:
                f.write(response.content)

        ja = str(ctx.guild.get_member(ctx.message.author.id).created_at)
        jg = str(ctx.guild.get_member(ctx.message.author.id).joined_at)
        """
        image (really inefficient)
        """
        string = data['bio']
        img = Image.open('/root/GhettoPi/file.png')
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("/root/GhettoPi/arial.ttf", fontsize, encoding="unic")
        stats = ImageFont.truetype("/root/GhettoPi/other.ttf", 33, encoding="unic")
        draw.text(xy=(780,40), text=invoker,fill=(255,255,255), font=font)
        draw.text(xy=(570,365), text="Joined Discord: {}".format(datetime.strptime(ja, "%Y-%m-%d %H:%M:%S.%f")),fill=(255,255,255), font=stats)
        draw.text(xy=(570,415), text="Joined Guild: {}".format(datetime.strptime(jg, "%Y-%m-%d %H:%M:%S.%f")),fill=(255,255,255), font=stats)
        draw.text(xy=(570,500), text='Bio: {}'.format('\n'.join(string[i:i+40] for i in range(0, len(string), 15))),fill=(255,255,255), font=stats)
        pfp = Image.open('/root/GhettoPi/Profiles/{}.jpg'.format(str(ctx.message.author.id)))
        img_w, img_h = pfp.size
        bg_w, bg_h = img.size
        new_width  = 270
        new_height = 270
        p = pfp.resize((new_width, new_height), Image.ANTIALIAS)
        img.paste(p, (18,18))
        simg = img.save('/root/GhettoPi/Images/{}.png'.format(str(ctx.message.author.id)))
        file = discord.File('/root/GhettoPi/Images/{}.png'.format(str(ctx.message.author.id)), filename="Profile.png")
        await ctx.send(file=file)
        os.remove('/root/GhettoPi/Images/{}.png'.format(str(ctx.message.author.id)))
        os.remove('/root/GhettoPi/Profiles/{}.jpg'.format(str(ctx.message.author.id)))

    @commands.command(name='bio')
    async def bio(self, ctx, *, bio: str):
        count = len(bio)
        bioset = {
            '_id': int(ctx.message.author.id),
            'bio': bio
        }
        if biodb.find_one({"_id": int(ctx.message.author.id)}):
            if not count > 75:
                biodb.delete_one({"_id": int(ctx.message.author.id)})
                bios = {
                    '_id': int(ctx.message.author.id),
                    'bio': bio
                }
                biodb.insert_one(bios)
                await ctx.send("Successfully updated bio.")
            else:
                await ctx.send("Please send a bio smaller than 75 characters.")
        else:
            if not count > 75:
                biodb.insert_one(bioset)
                await ctx.send("Successfully updated bio.")
            else:
                await ctx.send("Please send a bio smaller than 75 characters.")
def setup(bot):
    bot.add_cog(Profile(bot))
