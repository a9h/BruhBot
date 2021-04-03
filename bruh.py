import discord
from discord.ext import commands
import random
import praw
import requests 
import os
import json
import time
from pyfiglet import Figlet



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
    print("Developed by A9H#8923 and tomekcos")
    await client.change_presence(status=discord.Status.online, activity=discord.Game(">>Help"))


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandOnCooldown):  
        slowdown = ["BRUH! SLOW DOWN!", "Take a breather and STOP for a minute", "Ur going to fast, slow tf down", "Hey! would you mind slowing down!?"]
        message = ('The command {} is still on cooldown for {:.2f}'.format(ctx.command.name, error.retry_after))
        embed=discord.Embed()
        embed.add_field(name=(f"{random.choice(slowdown)}"), value=(message), inline=False)
        await ctx.send(embed=embed)
        


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


tokenopen = open("token.json", "r")
data = json.loads(tokenopen.read())
token = (data["token"])





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
@commands.cooldown(1, 6.0, commands.BucketType.user)
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
        

@client.command()
async def author(ctx):
    embed = discord.Embed(color=0xd60000)
    embed.add_field(name="Made by A9H#8923", value="https://github.com/a9h", inline=True)
    embed.add_field(name="‎", value="Fun Fact: this is the only colored embed in BruhBot", inline=False)
    await ctx.send(embed=embed)


client.run(token)
