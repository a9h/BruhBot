import discord
from discord.ext import commands
import random




client = commands.Bot(command_prefix=">>")
client.remove_command("help")



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print("BruhBot Activated")
    await client.change_presence(status=discord.Status.online, activity=discord.Game(">>Help"))

@client.command()
async def mute(ctx,member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedrole = discord.utils.get(guild.roles, name="muted1582")

    if not mutedrole:
        mutedrole = await guild.create_role(name="muted1582")
        for channel in guild.channels:
            await channel.set_permissions(mutedrole, speak=False, send_messages=False, read_message_history=True, read_messages=True)
    await member.add_roles(mutedrole, reason=reason)
    await ctx.send (f"Muted {member.mention} for {reason}")
    await member.send(f"You were muted in the server {guild.name} for {reason}")

@client.command()
async def unmute(ctx,member: discord.Member):
    guild = ctx.guild
    mutedrole = discord.utils.get(guild.roles, name="muted1582")
    await member.remove_roles(mutedrole)
    await ctx.send(f"Unmuted user {member.mention}")
    await member.send(f"You were unmuted in the server {guild.name}")


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send("user " + member.display_name + " has been kicked")



@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send("user " + member.display_name + " has been banned")

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"unbanned {user.mention}")
            return





@client.group(name="help", invoke_without_command=True)
async def help(ctx):
    embed = discord.Embed(title="BruhBot command list!", description="(Currency coming soon!)")
    embed.add_field(name="Fun 😊", value="`>>help fun`", inline=True)
    embed.add_field(name="Image 📷", value="`>>help image`", inline=True)
    embed.add_field(name="Memey 😂", value="`>>help memey`", inline=True)
    embed.add_field(name="Moderation⚙️", value="`>>help moderation`", inline=True)
    embed.add_field(name="Utility", value="`>>help utility`", inline=True)
    embed.add_field(name="Placeholder", value="Placeholder", inline=True)
    embed.set_footer(text="use >> before every command!")
    await ctx.send(embed=embed)

@help.command(name="moderation")
async def help_mod(ctx):
    embed = discord.Embed(title="⚙️ Moderation Commands ⚙️")
    embed.add_field(name="⠀", value="`ban`, `unban`, `mute`, `unmute`, `kick` `clear`", inline=True)


    embed.set_footer(text="use >> before every command!")
    await ctx.send(embed=embed)



@client.command(aliases=["8ball", "eightball"])
async def _8ball(ctx, *, question):
    responces = ["It is certain.",
"It is decidedly so.",
"Without a doubt.",
"Yes - definitely.",
"You may rely on it.",
"As I see it, yes.",
"Most likely.",
"Outlook good.",
"Yes.",
"Signs point to yes.",
"Reply hazy, try again.",
"Ask again later.",
"Better not tell you now.",
"Cannot predict now.",
"Concentrate and ask again.",
"Don't count on it.",
"My reply is no.",
"My sources say no.",
"Outlook not so good.",
"Very doubtful."]

    await ctx.send(f"```question: {question}\nAnswer: {random.choice(responces)}```")


@client.command(aliases=["McName", "3Letter"])
async def _3letterword(ctx):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
               "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
               "y", "z" "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    await ctx.send(f"```your 3 letter word is: {random.choice(letters)}{random.choice(letters)}{random.choice(letters)}```")




@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)




@client.command()
async def ping(ctx):
    await ctx.send(f"pong! {round(client.latency * 1000)}ms")




client.run('Nzk5MjY3NjE5MzY2NTAyNDcx.YABF-g.oEc10kG2Lgb0OKwZzSkUosZo0WY')