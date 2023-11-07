# This example requires the 'message_content' intent.

import discord
import random
import json
from discord.ext import commands

secret = open("secret.json")
secretData = json.load (secret)

TOKEN = secretData['TOKEN']

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

def get_Channel(guild_id):
    print(guild_id)
    #announcements only works with specific channels

    if guild_id == 359896709624758273:
        return bot.get_channel(373626380786597888)
    elif guild_id == 772317775485861969:
        return bot.get_channel(772323209671344148)
    elif guild_id == 939701223144185867:
        return bot.get_channel(939714632929665034)
    

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user} {bot.user.name} {bot.user.id}')
    
@bot.event
async def on_member_join(member):
    print("JOOINED")
    channel = get_Channel(member.guild.id)
    print(f"{member} has joined the server")
    await channel.send(f'Welcome to server {member.mention}! :D')
    #add gif welcoming

@bot.event
async def on_member_remove(member):
    print("left")
    channel = get_Channel(member.guild.id)
    print(f"{member} has left the server")
    await channel.send(f'BYE BYE {member.mention}! meow D:')
    #add gif shooting them

@bot.command()
async def meow(ctx):
    await ctx.send('MEOW MEOW!')

@bot.command()
async def echo(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def coinflip(ctx):
    meow = "meow"
    if random.random() > .5:
        meow = "tails"
    else:
        meow = "heads"
    await ctx.send(meow)

@bot.command()
async def test(ctx):
    embed = discord.Embed(title="My Title", description="My Description", color=0x0000FF)
    embed.set_image(url="https://media.discordapp.net/attachments/1094037396485570641/1096738285700780032/RobloxStudioBeta_lj3HrUER2e.gif")
    embed.add_field(name="Field Name", value="Field Value")
    embed.set_footer(text="My Footer")

    await ctx.send(embed=embed)

#token
bot.run(TOKEN)