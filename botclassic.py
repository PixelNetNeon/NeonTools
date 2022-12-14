from cmath import inf
from lib2to3.pgen2 import token
from pydoc import doc
import string
#discord stuff
import discord
from discord.ext import commands
#windows notifications
from plyer import notification
#python stuff idfk
import asyncio
import random
#logging
import discord
import logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
import urllib.request

import os
from dotenv import load_dotenv



####################################################################################
# Intents
####################################################################################

intents = discord.Intents.default()
intents.members = True

####################################################################################
# Command Prefix
####################################################################################

bot = commands.Bot(command_prefix='nt!',intents=intents)

####################################################################################
# Bot events
####################################################################################
print('neontools is loading. please wait')
@bot.event
async def on_ready():
    #print('Logged on as {0}!'.format(self.user))
    print('NeonTools Has Loaded And Is Now Ready >:D')
    game = ['Satisfactory','ROBLOX','Team Fortress 2','Terraria']
    #await bot.change_presence(activity=discord.Game(name=f'{random.choice(game)}'))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Going Under A Rewrite To Support Slash Commands"))
        #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType., name="i want this to support multiple stuff"))
     
   

####################################################################################
# Commands
####################################################################################
@bot.command()
async def ping(ctx):
    await ctx.send('pong :ping_pong:')

@bot.command()
async def server(ctx):
    await ctx.send('Check https://github.com/PixelNetNeon/NeonTools/issues/7')

@bot.command()
async def opensource(ctx):
    await ctx.send('Oh Yeah I Totally Forgot That I Am Open Source! Have A Link: https://github.com/PixelNetNeon/NeonTools')

@bot.command()
async def about(ctx):
    info=discord.Embed(title='NeonTools', description='The Offical NeonTools Discord Bot.', color=0xc9fbff)
    await ctx.send(embed=info)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

####################################################################################
# Fun Commands
####################################################################################

@bot.command()
async def annoythedev(ctx):
    await ctx.send('alr sending him a windows notification lol')
    #userAvatar = ctx.message.author.avatar_url
    notification.notify(title= 'heheheha',
                    message= ctx.message.author.name + ' Annoyed You Heheheha',
                    app_icon = None,
                    timeout= 10,
                    toast=False)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    await ctx.send(':neutral_face:')
    #for i in range(times):
        #await ctx.send(content)

@bot.command()
async def profile(ctx, *, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    userAvatar = member.avatar_url
    await ctx.send(userAvatar)

@bot.command()
async def embedtest(ctx, times: int):
    info=discord.Embed(title='Title', description='description', color=0x000000)
    for x in range(times): #range(10)
        info.add_field(name='this is a field', value='this is a value', inline=True)
    await ctx.send(embed=info)

####################################################################################
# API [fun]
####################################################################################

import json, requests

@bot.command()
async def space(ctx, *, arg):
    #print(ctx, arg)
    if arg == 'iss':
        url = requests.get("http://api.open-notify.org/iss-now.json")
        text = url.text
        data = json.loads(text)
        user = data

        info=discord.Embed(title='Current Position Of The ISS', description=user['iss_position'], color=0x000000)
        info.set_footer(text='http://api.open-notify.org/iss-now.json')
        await ctx.send(embed=info)
    elif arg == 'astros':
        url = requests.get("http://api.open-notify.org/astros.json")
        text = url.text
        data = json.loads(text)
        user = data

        numberofpeopleformat = '{people} People Currently In Space Right Now'

        info=discord.Embed(title='Current Number Of Astronauts In Space', description=numberofpeopleformat.format(people = user['number']), color=0x000000)
        info.set_footer(text='http://api.open-notify.org/astros.json')

        #footer = user['number']

        #for x in range(footer): #range(10):

        #    info.add_field(name=user['name'], value='this is a value', inline=True)
        #    #info.add_field(name='this is a field', value='this is a value', inline=True)

        await ctx.send(embed=info)
    else:
        await ctx.send('I Could Not Understand Your Request. Please Type In `nt!space iss` or `nt!space astros`')

####################################################################################
# Run
####################################################################################

load_dotenv()

token = os.getenv("DISCORD_TOKEN")

bot.run(token)
