import discord
import random
from discord.ext import commands

"""This Class is for commands that are just for fun."""


class Community(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Community(bot))
