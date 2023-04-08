from discord.ext import commands
import random
import countries

@commands.command()
async def country(ctx):
    """ Answer with a random country """
    await ctx.send(random.choice(countries.countries))

async def setup(bot):
    bot.add_command(country)