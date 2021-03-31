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
    

    @commands.command()
    async def waifurate(self, ctx):
        number = random.randint(1, 100)
        if 25 > number:
            embed = discord.Embed()
            embed.add_field(name="BruhBot Waifu Rater", value=f"You are {number}/100 waifu :nauseated_face:")
            await ctx.send(embed=embed)
        elif number > 25 and number < 50:
            embed = discord.Embed()
            embed.add_field(name="BruhBot Waifu Rater", value=f"You are {number}/100 waifu :confused:")
            await ctx.send(embed=embed)
        elif number > 50 and number < 75:
            embed = discord.Embed()
            embed.add_field(name="WBruhBot Waifu Rater", value=f"You are {number}/100 waifu :relieved:")
            await ctx.send(embed=embed)
        elif number > 75:
            embed = discord.Embed()
            embed.add_field(name="BruhBot Waifu Rater", value=f"You are {number}/100 waifu :open_mouth:")
            await ctx.send(embed=embed)

    @commands.command(aliases=["hi", "hello"])
    async def e(self, ctx):
        responces = ["hi, how are you?", "yes, im here!", "hello!", "Hi!", "Im BruhBot, nice to meet you!", "Hey!"]

        await ctx,send(f"{random.choice(responces)}")


    


    @commands.command()
    async def insult(self, ctx):
        insult_like = ["smells like", "looks like", ""]






    @commands.command()
    async def yomamma(self, ctx):
        yomammaso = ["fat", "ugly", "old", "stupid"]
        selection = random.choice(yomammaso)
        if selection == "fat":
            print("a")
        elif selection == "ugly":
            print("b")




    @commands.command()
    async def kill(self, ctx, member: discord.Member, ):
        deaths = [f"{ctx.author.name} ripped off {member.mention}'s head", f"{member.mention} got hit by a train", f"{member.mention} fell off a cliff",
                 f"{ctx.author.name} sliced {member.mention} into 30 pieces", f"you tried to shoot {member.mention}, but it ricochet and exploded your head",
                 f"{member.mention} watched the emoji movie and died of cringe", f"{member.mention} got karate kicked in the head", f"{ctx.author.name} pulled out {member.mention}'s guts"
                 , f"{member.mention} died of death", f"{member.mention} choked on a toothbrush", f"{member.mention} got spiked by a cactus", f"{ctx.author.name} smited {member.mention} with lightning",
                 f"{ctx.author.name} shoved a crystal down {member.mention}'s throat", f"{member.mention}'s intestines got grinded up"]

        await ctx.send(f"{random.choice(deaths)}")





def setup(client):
    client.add_cog(Fun(client))
