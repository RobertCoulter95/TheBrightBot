import discord
import random
from discord.ext import commands


"""This Class is for commands that provide a useful utility.
Any commands that are for fun belong in community.py"""


class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # dice rolling, takes two params
    @commands.command(name='roll', help='Rolls dice. Two inputs <number of dice> <number of sides>')
    async def roll(self, ctx, number_of_dice: int, number_of_sides: int):
        if not number_of_dice or not number_of_sides:
            await ctx.send("Format should be !command <number of Dice> <number of sides>")
        dice = [
            str(random.choice(range(1, number_of_sides + 1)))
            for _ in range(number_of_dice)
        ]
        await ctx.send(', '.join(dice))

    @commands.command(name="choose", help='Chooses one of the options sent, separated by commas')
    async def choose(self, ctx, *choices: str):
        if not choices:
            await ctx.send("Please provide multiple options, separated by comma(s)")
        options_list = (' '.join(choices)).split(",")
        await ctx.send(random.choice(options_list))


def setup(bot):
    bot.add_cog(Utils(bot))
