from discord.ext import commands
import random

@commands.command()
async def rand(ctx, first: int, second: int):
    """ Answer with a number within first and second argument """
    await ctx.send(random.randint(first, second))

async def setup(bot):
    bot.add_command(rand)