import discord
from discord.ext import commands
import requests

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def dogcog(self, ctx):
        response = requests.get("https://some-random-api.ml/facts/dog")
        fact = response.json()
        url = (fact["fact"])
        await ctx.send(url)
        



def setup(client):
    client.add_cog(Example(client))
