import discord
from discord.ext import commands
import random
import praw
import requests 
import os
import json




reddit = praw.Reddit(client_id =  "lHqFX0eMpjvenA", client_secret = "4XnYG-_BLGHZ855EEGWnKHwXLiSy6A", 
username = "Diamond_1213", password = "iLkTI9L9cjZQk", user_agent = "pythonpraw", check_for_async=False)


    


"""
8 888888888o             8 888888888o.             8 8888      88           8 8888        8
8 8888    `88.           8 8888    `88.            8 8888      88           8 8888        8
8 8888     `88           8 8888     `88            8 8888      88           8 8888        8
8 8888     ,88           8 8888     ,88            8 8888      88           8 8888        8
8 8888.   ,88'           8 8888.   ,88'            8 8888      88           8 8888        8
8 8888888888             8 888888888P'             8 8888      88           8 8888        8
8 8888    `88.           8 8888`8b                 8 8888      88           8 8888888888888
8 8888      88           8 8888 `8b.               ` 8888     ,8P           8 8888        8
8 8888    ,88'           8 8888   `8b.               8888   ,d8P            8 8888        8
8 888888888P             8 8888     `88.              `Y88888P'             8 8888        8

8 888888888o                 ,o888888o.               8888888 8888888888
8 8888    `88.            . 8888     `88.                   8 8888
8 8888     `88           ,8 8888       `8b                  8 8888
8 8888     ,88           88 8888        `8b                 8 8888
8 8888.   ,88'           88 8888         88                 8 8888
8 8888888888             88 8888         88                 8 8888
8 8888    `88.           88 8888        ,8P                 8 8888
8 8888      88           `8 8888       ,8P                  8 8888
8 8888    ,88'            ` 8888     ,88'                   8 8888
8 888888888P                 `8888888P'                     8 8888     


Made by A9H#8923
Github https://github.com/a9h
"""


client = commands.Bot(command_prefix=">>")
client.remove_command("help")



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print("BruhBot Activated")
    print("Developed by A9H#8923")
    await client.change_presence(status=discord.Status.online, activity=discord.Game(">>Help"))



@client.command()
async def load(ctx, extention):
    client.load_extension(f"cogs.{extention}")


@client.command()
async def reload(ctx, extention):
    client.unload_extension(f"cogs.{extention}")
    client.load_extension(f"cogs.{extention}")
    await ctx.send("Cog has been reloaded. Please only use this feature if you are a developer")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")









@client.command()
@commands.has_permissions(manage_messages=True)
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
@commands.has_permissions(manage_messages=True)
async def unmute(ctx,member: discord.Member):
    guild = ctx.guild
    mutedrole = discord.utils.get(guild.roles, name="muted1582")
    await member.remove_roles(mutedrole)
    await ctx.send(f"Unmuted user {member.mention}")
    await member.send(f"You were unmuted in the server {guild.name}")


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    await member.send(f"You were kicked from the server {guild.name}")
    await member.kick(reason=reason)
    await ctx.send("User " + member.display_name + " has been kicked")


@client.command()
async def meme(ctx):
    subreddit = reddit.subreddit("memes")
    all_subs = []
    top = subreddit.top(limit = 50)
    for submission in top:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url

    embed = discord.Embed(title = name)
    embed.set_image(url = url)
    await ctx.send(embed = embed)



@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    await member.send(f"You were banned from the server {guild.name}")
    await member.ban(reason=reason)
    await ctx.send("user " + member.display_name + " has been banned")

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    guild = ctx.guild
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
    embed.add_field(name="Fun :smile:", value="`>>help fun`", inline=True)
    embed.add_field(name="Image 📷", value="`>>help image`", inline=True)
    embed.add_field(name="Memey 😂", value="`>>help memey`", inline=True)
    embed.add_field(name="Moderation⚙️", value="`>>help moderation`", inline=True)
    embed.add_field(name="Utility🛠️", value="`>>help utility`", inline=True)
    embed.add_field(name="Animals🐶", value=">>help animals", inline=True)
    embed.set_footer(text="use >> before every command!")
    await ctx.send(embed=embed)

@help.command(name="moderation")
async def help_mod(ctx):
    embed = discord.Embed(title="⚙️ Moderation Commands ⚙️")
    embed.add_field(name="⠀", value="`ban`, `unban`, `mute`, `unmute`, `kick` `clear`", inline=True)

    embed.set_footer(text="use >> before every command!")
    await ctx.send(embed=embed)

@help.command(name="fun")
async def help_fun(ctx):
    embed = discord.Embed(title=":smile: Fun Commands :smile:")
    embed.add_field(name="⠀", value="`Kill`, `Dox`, `waifurate`, `epicgamer`, `8ball`, `3name`", inline=True)
    #If you are reading this then hello
    embed.set_footer(text="use >> before every command!")
    await ctx.send(embed=embed)

@help.command(name="animals")
async def help_animal(ctx):
    embed = discord.Embed(title="🐶Animal commands🐶")
    embed.add_field(name="⠀", value="`catfact`, `dogfact`, `pandafact`, `foxfact`, `birdfact`, `koalafact`, `kangaroofact`, `racoonfact`, `elephantfact`, `giraffefact`, `whalefact`, `dog`, `cat`, `panda`, `redpanda`, `bird`, `fox`, `koala`")
    embed.set_footer(text="use >> before every command!")
    await ctx.send(embed=embed)


@client.command()
async def dog(ctx):
    response = requests.get("https://some-random-api.ml/facts/koala")
    fact = response.json()
    url = (fact["fact"])
    await ctx.send(url)


@client.command()
async def iphonex(ctx, url: str):
    async with aiohttp.ClientSession() as ses:
        async with ses.get(f"https://nekobot.xyz/api/imagegen?type=iphonex&image={url}") as r:
            if r.status in range(200, 299):
                data = await r.json()
                url = data["message"]
                embed = discord.Embed(title = "MOM IM ON AN IPHONE!")
                embed.set_image(url=url)
                await ctx.send(embed=embed)
                await ses.close
            else:
                await ctx.send("error making request")
                await ses.close




@client.command()
async def waifurate(ctx):
    number = random.randint(1, 100)
    if 25 > number:
        embed = discord.Embed()
        embed.add_field(name="Waifu rate machine", value=f"You are {number}/100 waifu :nauseated_face:")
        await ctx.send(embed=embed)
    elif number > 25 and number < 50:
        embed = discord.Embed()
        embed.add_field(name="Waifu rate machine", value=f"You are {number}/100 waifu :confused:")
        await ctx.send(embed=embed)
    elif number > 50 and number < 75:
        embed = discord.Embed()
        embed.add_field(name="Waifu rate machine", value=f"You are {number}/100 waifu :relieved:")
        await ctx.send(embed=embed)
    elif number > 75:
        embed = discord.Embed()
        embed.add_field(name="Waifu rate machine", value=f"You are {number}/100 waifu :open_mouth:")
        await ctx.send(embed=embed)



@client.command()
async def kill(ctx, member: discord.Member, ):
    deaths = [f"{ctx.author.name} ripped off {member.mention}'s head", f"{member.mention} got hit by a train", f"{member.mention} fell off a cliff",
              f"{ctx.author.name} sliced {member.mention} into 30 pieces", f"you tried to shoot {member.mention}, but it ricochet and exploded your head",
              f"{member.mention} watched the emoji movie and died of cringe", f"{member.mention} got karate kicked in the head", f"{ctx.author.name} pulled out {member.mention}'s guts"
              , f"{member.mention} died of death", f"{member.mention} choked on a toothbrush", f"{member.mention} got spiked by a cactus", f"{ctx.author.name} smited {member.mention} with lightning",
              f"{ctx.author.name} shoved a crystal down {member.mention}'s throat", f"{member.mention}'s intestines got grinded up"]

    await ctx.send(f"{random.choice(deaths)}")


@client.command(aliases=["dox", "doxx"]) #THIS IS A JOKE FEATURE AND ONLY PROVIDES FAKE ADDRESSES
async def autodox(ctx, member: discord.Member):
    s = open("address.txt", "r")
    m = s.readlines()
    l = []
    for i in range(0, len(m) - 1):
        x = m[i]
        z = len(x)
        a = x[:z - 1]
        l.append(a)
    l.append(m[i + 1])
    o = random.choice(l)
    await ctx.send(f"{member.mention} lives at " + (o))
    s.close()




@client.command()
async def balance(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"] 
    bank_amt = users[str(user.id)]["bank"] 

    embed = discord.Embed(Title = f"{ctx.author.name}'s balance")
    embed.add_field(name = "Wallet balance",value = wallet_amt)
    embed.add_field(name = "Bank balance",value = bank_amt)
    await ctx.send(embed=embed)


@client.command()
async def beg(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()
    earnings = random.randrange(101)

    await ctx.send(f"someone gave you {earnings} coins!")

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json", "w") as f:
        users = json.dump(users,f)




async def open_account(user):


    users = await get_bank_data()
   

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0


    with open("mainbank.json", "w") as f:
        users = json.dump(users,f)
    return True
    

    

async def get_bank_data():
        with open("mainbank.json", "r") as f:
            users = json.load(f)
        
        return users




    


















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


@client.command(aliases=["McName", "3Letter", "3char", "3name"])
async def _3letterword(ctx):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
               "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
               "y", "z" "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    await ctx.send(f"```your 3 letter name is: {random.choice(letters)}{random.choice(letters)}{random.choice(letters)}```")




@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)




@client.command()
async def ping(ctx):
    await ctx.send(f"pong! {round(client.latency * 1000)}ms")

@client.command()
async def author(ctx):
    embed = discord.Embed(color=0xd60000)
    embed.add_field(name="Made by A9H#8923", value="https://github.com/a9h", inline=True)
    embed.add_field(name="‎", value="Fun Fact: this is the only colored embed in BruhBot", inline=False)
    await ctx.send(embed=embed)


client.run("Nzk5MjY3NjE5MzY2NTAyNDcx.YABF-g.VsTXoKeHRFJiHXRIWew9HjSeD7w")
