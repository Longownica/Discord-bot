import discord
from discord.ext import commands

class event_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id
        if message_id == 1091371609593483375:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)

            if payload.emoji.name == "🦜":
                role = discord.utils.get(guild.roles, name="Krakow")
            elif payload.emoji.name == "🐦":
                role = discord.utils.get(guild.roles, name="Warszawa")
            elif payload.emoji.name == "🐧":
                role = discord.utils.get(guild.roles, name="Gdansk")
            elif payload.emoji.name == "🦆":
                role = discord.utils.get(guild.roles, name="Wroclaw")
            elif payload.emoji.name == "🦒":
                role = discord.utils.get(guild.roles, name="Poznan")

            if role is not None:
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)


    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        message_id = payload.message_id
        if message_id == 1091371609593483375:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)

            if payload.emoji.name == "🦜":
                role = discord.utils.get(guild.roles, name="Krakow")
            elif payload.emoji.name == "🐦":
                role = discord.utils.get(guild.roles, name="Warszawa")
            elif payload.emoji.name == "🐧":
                role = discord.utils.get(guild.roles, name="Gdansk")
            elif payload.emoji.name == "🦆":
                role = discord.utils.get(guild.roles, name="Wroclaw")
            elif payload.emoji.name == "🦒":
                role = discord.utils.get(guild.roles, name="Poznan")

            if role is not None:
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)


    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel_id = 1091034220559867915
        await channel_id.send(f'Welcome {member.mention}.')

    
async def setup(bot):
    await bot.add_cog(event_cog(bot))