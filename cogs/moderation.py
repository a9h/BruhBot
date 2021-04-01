import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client




    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self,ctx,member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedrole = discord.utils.get(guild.roles, name="muted")

        if not mutedrole:
            mutedrole = await guild.create_role(name="muted")
            for channel in guild.channels:
                await channel.set_permissions(mutedrole, speak=False, send_messages=False, read_message_history=True, read_messages=True)
        await member.add_roles(mutedrole, reason=reason)

        if reason == None:
            await ctx.send (f"Muted {member.mention}")
            await member.send(f"You were muted in the server {guild.name}")

        elif reason != None:
            await ctx.send (f"Muted {member.mention} for {reason}")
            await member.send(f"You were muted in the server {guild.name} for {reason}")

        




def setup(client):
    client.add_cog(Moderation(client))