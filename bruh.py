import discord
from discord.ext import commands
import random



client = commands.Bot(command_prefix=">>")
client.remove_command("help")



@client.event
async def on_ready(ctx):
    print('We have logged in as {0.user}'.format(client))
    print("BruhBot Activated")
    await ctx.send("BruhBot is active, type >>help for help!")
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
    e.set_image(url="https://i.imgur.com/5nqpFiF.jpg")
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
    author = ctx.message.author

    embed = discord.Embed()


    embed.set_image(url="https://anthropocenemagazine.org/wp-content/uploads/2020/04/Panda-2.jpg")
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


@client.command(name="cat")
async def cat(context):

    images = ["cat4.jpg", "cat3.jpg", "cat2.jpg", "cat1.png"]

    random_image = random.choice(images)
    await context.send(file=discord.File(random_image))




@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)




@client.command()
async def ping(ctx):
    await ctx.send(f"pong! {round(client.latency * 1000)}ms")




client.run('Nzk5MjY3NjE5MzY2NTAyNDcx.YABF-g.L3-KuENgE3F244QhOaTPMNP96UA')