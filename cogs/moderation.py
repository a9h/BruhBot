import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client




    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self,ctx,member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedrole = discord.utils.get(guild.roles, name="muted1582")

        if not mutedrole:
            mutedrole = await guild.create_role(name="muted1582")
            for channel in guild.channels:
                await channel.set_permissions(mutedrole, speak=False, send_messages=False, read_message_history=True, read_messages=True)
        await member.add_roles(mutedrole, reason=reason)

        if reason == None:
            await ctx.send (f"Muted {member.mention}")
            await member.send(f"You were muted in the server {guild.name}")

        elif reason != None:
            await ctx.send (f"Muted {member.mention} for {reason}")
            await member.send(f"You were muted in the server {guild.name} for {reason}")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        await member.send(f"You were kicked from the server {guild.name}")
        await member.kick(reason=reason)
        await ctx.send("User " + member.display_name + " has been kicked")        



    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx,member: discord.Member):
        guild = ctx.guild
        mutedrole = discord.utils.get(guild.roles, name="muted1582")
        await member.remove_roles(mutedrole)
        await ctx.send(f"Unmuted user {member.mention}")
        await member.send(f"You were unmuted in the server {guild.name}")


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount : int):
        await ctx.channel.purge(limit=amount)


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        await member.send(f"You were banned from the server {guild.name}")
        await member.ban(reason=reason)
        await ctx.send("user " + member.display_name + " has been banned")



    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        guild = ctx.guild
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
         user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"unbanned {user.mention}")
            return


def setup(client):
    client.add_cog(Moderation(client))