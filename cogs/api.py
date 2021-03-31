import discord
from discord.ext import commands
import requests

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def dogfact(self, ctx):
        response = requests.get("https://some-random-api.ml/facts/dog")
        fact = response.json()
        url = (fact["fact"])
        await ctx.send(url)
        

    @commands.command()
    async def catfact(self, ctx):
        response = requests.get("https://some-random-api.ml/facts/cat")
        fact = response.json()
        url = (fact["fact"])
        await ctx.send(url)

    @commands.command()
    async def foxfact(self, ctx):
        response = requests.get("https://some-random-api.ml/facts/fox")
        fact = response.json()
        url = (fact["fact"])
        await ctx.send(url)


    @commands.command()
    async def pandafact(self, ctx):
        response = requests.get("https://some-random-api.ml/facts/panda")
        fact = response.json()
        url = (fact["fact"])
        await ctx.send(url)

    @commands.command()
    async def birdfact(self, ctx):
        response = requests.get("https://some-random-api.ml/facts/bird")
        fact = response.json()
        url = (fact["fact"])
        await ctx.send(url)


    @commands.command()
    async def koalafact(self, ctx):
        response = requests.get("https://some-random-api.ml/facts/koala")
        fact = response.json()
        url = (fact["fact"])
        await ctx.send(url)



    @commands.command()
    async def kangaroofact(self, ctx):
        response = requests.get("https://some-random-api.ml/facts/kangaroo")
        fact = response.json()
        url = (fact["fact"])
        await ctx.send(url)

    @commands.command()
    async def racoonfact(self, ctx):
        response = requests.get("https://some-random-api.ml/facts/racoon")
        fact = response.json()
        url = (fact["fact"])
        await ctx.send(url)
    
    @commands.command()
    async def elephantfact(self, ctx):
        response = requests.get("https://some-random-api.ml/facts/elephant")
        fact = response.json()
        url = (fact["fact"])
        await ctx.send(url)

    @commands.command()
    async def giraffefact(self, ctx):
        response = requests.get("https://some-random-api.ml/facts/giraffe")
        fact = response.json()
        url = (fact["fact"])
        await ctx.send(url)

    @commands.command()
    async def whalefact(self, ctx):
        response = requests.get("https://some-random-api.ml/facts/whale")
        fact = response.json()
        url = (fact["fact"])
        await ctx.send(url)

    @commands.command()
    async def dog(self, ctx):
        response = requests.get("https://some-random-api.ml/img/dog")
        fact = response.json()
        url = (fact["link"])
        embed = discord.Embed(title="Here is your dog picture!")
        embed.set_image(url=url)
        embed.set_footer(text="use >> before every command!")
        await ctx.send(embed=embed)
    
    @commands.command()
    async def cat(self, ctx):
        response = requests.get("https://some-random-api.ml/img/cat")
        fact = response.json()
        url = (fact["link"])
        embed = discord.Embed(title="Here is your cat picture!")
        embed.set_image(url=url)
        embed.set_footer(text="use >> before every command!")
        await ctx.send(embed=embed)

    @commands.command()
    async def whale(self, ctx):
        response = requests.get("https://some-random-api.ml/img/whale")
        fact = response.json()
        url = (fact["link"])
        embed = discord.Embed(title="Here is your whale picture!")
        embed.set_image(url=url)
        embed.set_footer(text="use >> before every command!")
        await ctx.send(embed=embed)

    
    @commands.command()
    async def panda(self, ctx):
        response = requests.get("https://some-random-api.ml/img/panda")
        fact = response.json()
        url = (fact["link"])
        embed = discord.Embed(title="Here is your panda picture!")
        embed.set_image(url=url)
        embed.set_footer(text="use >> before every command!")
        await ctx.send(embed=embed)

    @commands.command()
    async def redpanda(self, ctx):
        response = requests.get("https://some-random-api.ml/img/red_panda")
        fact = response.json()
        url = (fact["link"])
        embed = discord.Embed(title="Here is your red panda picture!")
        embed.set_image(url=url)
        embed.set_footer(text="use >> before every command!")
        await ctx.send(embed=embed)

    @commands.command()
    async def kangaroo(self, ctx):
        response = requests.get("https://some-random-api.ml/img/kangaroo")
        fact = response.json()
        url = (fact["link"])
        embed = discord.Embed(title="Here is your kangaroo picture!")
        embed.set_image(url=url)
        embed.set_footer(text="use >> before every command!")
        await ctx.send(embed=embed)


    @commands.command()
    async def racoon(self, ctx):
        response = requests.get("https://some-random-api.ml/img/racoon")
        fact = response.json()
        url = (fact["link"])
        embed = discord.Embed(title="Here is your racoon picture!")
        embed.set_image(url=url)
        embed.set_footer(text="use >> before every command!")
        await ctx.send(embed=embed)


    @commands.command()
    async def bird(self, ctx):
        response = requests.get("https://some-random-api.ml/img/birb")
        fact = response.json()
        url = (fact["link"])
        embed = discord.Embed(title="Here is your bird picture!")
        embed.set_image(url=url)
        embed.set_footer(text="use >> before every command!")
        await ctx.send(embed=embed)


    @commands.command()
    async def koala(self, ctx):
        response = requests.get("https://some-random-api.ml/img/koala")
        fact = response.json()
        url = (fact["link"])
        embed = discord.Embed(title="Here is your koala picture!")
        embed.set_image(url=url)
        embed.set_footer(text="use >> before every command!")
        await ctx.send(embed=embed)


    @commands.command()
    async def fox(self, ctx):
        response = requests.get("https://randomfox.ca/floof/")
        fact = response.json()
        url = (fact["image"])
        embed = discord.Embed(title="Here is your fox picture!")
        embed.set_image(url=url)
        embed.set_footer(text="use >> before every command!")
        await ctx.send(embed=embed)





def setup(client):
    client.add_cog(Example(client))
