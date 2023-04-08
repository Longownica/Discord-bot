from discord.ext import commands
import random 

@commands.command()
async def choice(ctx, *args):
    """ Answer with a random choice from list given by user """
    await ctx.send(random.choice(args))

async def setup(bot):
    bot.add_command(choice)