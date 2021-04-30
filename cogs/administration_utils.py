import discord
import random
from discord.ext import commands

"""This class is for commands and utilities for the purpose of managing a discord server.
This includes but is not limited to, banning users, managing roles, creating channels, setting welcome messages, etc"""


class AdministrationUtils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    bot = commands.Bot(command_prefix='!')

    @commands.command(name='create-channel')
    @commands.has_role('admin')
    async def create_channel(self, ctx, channel_name='real-python'):
        guild = ctx.guild
        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        if not existing_channel:
            print(f'Creating a new channel: {channel_name}')
            await guild.create_text_channel(channel_name)
        else:
            ctx.send('That channel already exists.')

    @bot.event
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.text_channels, name="welcome")
        await channel.send(f"Welcome {member.name}!!!")


def setup(bot):
    bot.add_cog(AdministrationUtils(bot))
