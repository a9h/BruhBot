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
    async def (self, ctx):
        response = requests.get("")
        fact = response.json()
        url = (fact["link"])
        embed=Discord.embed(title="Here is you")






def setup(client):
    client.add_cog(Example(client))
