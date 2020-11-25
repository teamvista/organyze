# This example requires the 'members' privileged intents

import discord
import bot_config
from discord.ext import commands

version_num = '0.0.1'

description = f'''Organyze - A structured, fun approach to bullet journaling on Discord.
Version {version_num} | Powered by discord.py
'''

intents = discord.Intents.default()
intents.members = True

bot_token = bot_config.token
cmd_prefix = bot_config.prefix

bot = commands.Bot(command_prefix=cmd_prefix, description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})!')
    print('------')

@bot.command()
async def about(ctx):
    """About this bot (ping test)"""
    await ctx.send(description)

@bot.command()
async def daily(ctx):
    """Read in a daily log."""
    await ctx.send("Daily command sent.")
    pass

@bot.command()
async def add(ctx, kind: str, text: str):
    """Add a bullet."""
    await ctx.send(f"Added a bullet with type {kind} and text: {text}")
    pass

@bot.command()
async def add_sub_blt(ctx, id: int, kind: str, text: str):
    """Add an indented bullet."""
    pass

@bot.command(aliases=["del","remove"])
async def delete(ctx, id: int):
    """Delete a bullet by id."""
    await ctx.send(f"Deleted bullet {id}.")  # TODO: if ID exists
    pass

@bot.command(aliases=["edit"])
async def modify(ctx):
    """Edit a bullet's contents."""
    pass

@bot.command()
async def move(ctx, first_pos: int, second_pos: int):
    """Move a bullet to a different place in the list."""
    await ctx.send(f"Moved bullet {first_pos} to position {second_pos}.")
    pass

@bot.command()
async def display(ctx):
    """Display daily bullets."""
    await ctx.send(f"Normally, this would output all of your bullets, but my creator hasn't implemented this function yet!")
    pass

bot.run(bot_token)
