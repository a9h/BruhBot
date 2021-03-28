import discord
from discord.ext import commands
import time
import random

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def microwave(self, ctx, item="mksdmjsdjdsjfjdsnfjdsnscmjdcvjdfnjvndfhvdfvfd"):
        if item == "mksdmjsdjdsjfjdsnfjdsnscmjdcvjdfnjvndfhvdfvfd":
            await ctx.send("Bro... you need to put something in the microwave. Next time try >>microwave <item>")
        else:
            await ctx.send("Mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
            time.sleep(2)
            await ctx.send("BEEP BEEP BEEP")
            time.sleep(1)
            await ctx.send(f"Your {str(item)} is ready!")


    @commands.command()
    async def highlow(self, ctx, *, member: discord.Member = None):
        number = random.randrange(1, 100)
        hint_def = random.randrange(1, 100)

        if number > 50:
            hint = random.randrange(50, 100)

        elif number < 50:
            hint = random.randrange(1, 50)

        embed=discord.Embed(title="High-Low game!", description=(f"A hidden number between 1 and 100 has been chosen.\n The hint is {hint}"))
        await ctx.send(embed=embed)

        def check(m):
            return m.author.id == ctx.author.id
        
        guess = await self.client.wait_for("message", check=check)
        if guess.content == "high" or guess.content == "low":
            if guess.content == "high" and hint < number:
                await ctx.send(f"WELL DONE! YOU ARE CORRECT!!!! THE NUMBER WAS {number}")
            elif guess.content == "low" and hint > number:
                await ctx.send(f"WELL DONE! YOU ARE CORRECT!!!! THE NUMBER WAS {number}")
            elif guess.content == "low" and number > hint or guess.content == "high" and number < hint:
                await ctx.send(f"INCORRECT!! anyway the number was {number}")

        else:
            await ctx.send(f"Are you dumb?? You need to say either high or low not just {guess.content}")
    




def setup(client):
    client.add_cog(Fun(client))
