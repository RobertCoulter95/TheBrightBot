# bot.py
import os

import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

# load cogs
startup_extensions = ['cogs.utils', 'cogs.community']
for extension in startup_extensions:
    bot.load_extension(extension)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def load(extension_name: str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} loaded.".format(extension_name))


@bot.event
async def on_command_error(ctx, error):
    # If error is handled locally, return
    if hasattr(ctx.command, 'on_error'):
        return
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send('Stuff broke')
    if isinstance(error, commands.errors.CommandNotFound):
        await ctx.send('That no exist')


bot.run(TOKEN)
