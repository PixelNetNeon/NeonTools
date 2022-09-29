########################################################################################################################################################################
#       ::::    ::: :::::::::: ::::::::  ::::    ::: ::::::::::: ::::::::   ::::::::  :::        :::::::: 
#      :+:+:   :+: :+:       :+:    :+: :+:+:   :+:     :+:    :+:    :+: :+:    :+: :+:       :+:    :+: 
#     :+:+:+  +:+ +:+       +:+    +:+ :+:+:+  +:+     +:+    +:+    +:+ +:+    +:+ +:+       +:+         
#    +#+ +:+ +#+ +#++:++#  +#+    +:+ +#+ +:+ +#+     +#+    +#+    +:+ +#+    +:+ +#+       +#++:++#++   
#   +#+  +#+#+# +#+       +#+    +#+ +#+  +#+#+#     +#+    +#+    +#+ +#+    +#+ +#+              +#+    
#  #+#   #+#+# #+#       #+#    #+# #+#   #+#+#     #+#    #+#    #+# #+#    #+# #+#       #+#    #+#     
# ###    #### ########## ########  ###    ####     ###     ########   ########  ########## ########       
########################################################################################################################################################################
from email.mime import image
from multiprocessing.connection import wait
from multiprocessing.sharedctypes import Value
from optparse import Option
from random import choices
from time import sleep
from typing import Optional

import discord
from discord import app_commands

from typing import Literal, Union, NamedTuple
from enum import Enum

import os
from dotenv import load_dotenv

import json, requests

####################################################################################
# Intents & Stuff.
####################################################################################

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        self.synced = False

        #async def setup_hook(self):
            #await self.wait_until_ready()
            #if not self.synced:
                #await self.tree.sync()
                #self.synced = True 
            
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await self.tree.sync()
            self.synced = True 
            print(f'Logged in as {client.user} (ID: {client.user.id})')
            print('------')

intents = discord.Intents.default()
client = MyClient(intents=intents)

####################################################################################
# Commands.
####################################################################################

@client.tree.command()
async def hello(interaction: discord.Interaction):
    """Says hello!"""
    await interaction.response.send_message(f'Hi, {interaction.user.mention} :wave:')

@client.tree.command()
async def opennotify(interaction: discord.Interaction, action: Literal['iss-now','astros']):
    """Uses Open-Notify To Get The Lastest Space Info. Right Now Just A Embed Test."""
    if action == 'iss-now':
        url = requests.get("http://api.open-notify.org/iss-now.json")
        text = url.text
        data = json.loads(text)
        user = data

        info=discord.Embed(title='Current Position Of The ISS', description=user['iss_position'], color=0x000000)
        info.set_footer(text='http://api.open-notify.org/iss-now.json')
    elif action == 'astros':
        url = requests.get("http://api.open-notify.org/astros.json")
        text = url.text
        data = json.loads(text)
        user = data

        info=discord.Embed(title='Current Amount Of People In Space', description='TBD!', color=0x000000)
        info.set_footer(text='http://api.open-notify.org/astros.json')
    await interaction.response.send_message(embed=info)

@client.tree.command()
@app_commands.describe(
    first_value='The first value you want to add something to',
    second_value='The value you want to add to the first value',
)
async def add(interaction: discord.Interaction, first_value: int, second_value: int):
    """Adds two numbers together."""
    await interaction.response.send_message(f'{first_value} + {second_value} = {first_value + second_value}')

@client.tree.command()
@app_commands.describe(
    http='The HTTP Input For Da Ketteh',
    embed='Allows You To Send The Message As A Embed.',
)
async def httpcat(interaction: discord.Interaction, http: int, embed: Optional[bool]):
    """Sends A Image From https://http.cat That Uses A Http Response! How Cool Is That?"""
    if embed == True:
        info=discord.Embed(title=f'https://http.cat/{http}', color=0x000000)
        info.set_image(url=f'https://http.cat/{http}')
        await interaction.response.send_message(embed=info)
    #elif embed == False:
    else:
        await interaction.response.send_message(f'https://http.cat/{http}')
        

####################################################################################
# Testing.
####################################################################################
@client.tree.command()
async def test1(interaction: discord.Interaction, member: Optional[discord.Member], year: Optional[int]):
    """Says hello!"""
    print(member)
    info=discord.Embed(title='https://http.cat/422', color=0x000000)
    info.set_image(url='https://http.cat/422')
    await interaction.response.send_message(embed=info)

####################################################################################
# Run
####################################################################################

load_dotenv()

token = os.getenv("DISCORD_TOKEN_TEST")

client.run(token)
