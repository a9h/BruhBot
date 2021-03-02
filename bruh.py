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
async def test(ctx):
    e = discord.Embed()
    e.set_image(url="p")
    await ctx.send(e=e)


@client.command()
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed()

    embed.add_field(name=">>help", value="Shows this list", inline=True)
    embed.set_author(name="BRUHBOT help commands", icon_url="")
    embed.add_field(name=">>ping", value="Returns pong with response time shown!", inline=True)
    embed.add_field(name=">>kick", value="Kicks the selected person. Requires kick permissions", inline=True)
    embed.add_field(name=">>ban", value="Bans the selected person.\nRequires ban permissions", inline=True)
    await ctx.send(embed=embed)




@client.command()
async def image(ctx):
    embed = discord.Embed()

    image = ["https://anthropocenemagazine.org/wp-content/uploads/2020/04/Panda-2.jpg", "http://getwallpapers.com/wallpaper/full/4/6/5/768307-free-download-panda-bear-background-2048x1365.jpg"]

    embed.set_image(url=f"{random.choice(image)}")
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


@client.command(aliases=["McName"])
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