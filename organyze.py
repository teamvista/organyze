# This example requires the 'members' privileged intents

import discord
import bot_config
from discord.ext import commands
import random

description = '''Organyze - A structured, fun approach to bullet journaling on Discord.
'''

intents = discord.Intents.default()
intents.members = True

bot_token = bot_config.token
print(bot_token)

bot = commands.Bot(command_prefix='!org ', description=description, intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def about(ctx):
    """About this bot (ping test)"""
    await ctx.send("Organyze - A structured, fun approach to bullet journaling on Discord.")

bot.run(bot_token)
