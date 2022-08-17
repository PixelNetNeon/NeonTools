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
# command line stuff
from sys import exit
#logging
import discord
import logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
import urllib.request

####################################################################################
# Command Prefix
####################################################################################

bot = commands.Bot(command_prefix='nt!')

####################################################################################
# Intents
####################################################################################

intents = discord.Intents.default()
intents.members = True

####################################################################################
# Bot events
####################################################################################
print('neontools is loading. please wait')
@bot.event
async def on_ready():
    #print('Logged on as {0}!'.format(self.user))
    print('NeonTools Has Loaded And Is Now Ready >:D')
    game = ['Satisfactory','ROBLOX','Team Fortress 2','Terraria']
    await bot.change_presence(activity=discord.Game(name=f'{random.choice(game)}'))
        #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType., name="i want this to support multiple stuff"))
     
   

####################################################################################
# Commands
####################################################################################
@bot.command()
async def ping(ctx):
    await ctx.send('pong :ping_pong:')

@bot.command()
async def opensource(ctx):
    await ctx.send('Oh Yeah I Totally Forgot That I Am Open Source! Have A Link: https://github.com/PixelNetNeon/NeonTools')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def annoythedev(ctx):
    await ctx.send('alr sending him a windows notification lol')
    #userAvatar = ctx.message.author.avatar_url
    notification.notify(title= 'heheheha',
                    message= ctx.message.author.name + ' Annoyed You Heheheha',
                    app_icon = None,
                    timeout= 10,
                    toast=False)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


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
# im having a mac and cheese party and everyone is invited yayyyy

####################################################################################
# Run
####################################################################################

bot.run('yourid')

