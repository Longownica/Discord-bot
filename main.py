import discord
from discord.ext import commands
import settings


def run():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        print("READY")
        for mcog_file in settings.MCOG_DIR.glob("*.py"):
            if mcog_file.name != "__init__.py":
                await bot.load_extension(f"music-cog.{mcog_file.name[:-3]}")

        for cmd_file in settings.CMDS_DIR.glob("*.py"):
            if cmd_file.name != "__init__.py":
                await bot.load_extension(f"cmds.{cmd_file.name[:-3]}")

        for event_file in settings.EVENT_DIR.glob("*.py"):
            if event_file.name != "__init__.py":
                await bot.load_extension(f"event-cog.{event_file.name[:-3]}")

    bot.run(settings.DISCORD_API_SECRET)


if __name__ == "__main__":
    run()