import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.group(name="help", invoke_without_command=True)
    async def help(self,ctx):
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
    async def help_mod(self,ctx):
        embed = discord.Embed(title="⚙️ Moderation Commands ⚙️")
        embed.add_field(name="⠀", value="`ban`, `unban`, `mute`, `unmute`, `kick` `clear`", inline=True)

        embed.set_footer(text="use >> before every command!")
        await ctx.send(embed=embed)

    @help.command(name="fun")
    async def help_fun(self,ctx):
        embed = discord.Embed(title=":smile: Fun Commands :smile:")
        embed.add_field(name="⠀", value="`Kill`, `Dox`, `waifurate`, `epicgamer`, `8ball`, `3name`, `highlow`, `microwave`, `repeat`, `gaytest`", inline=True)
        #If you are reading this then hello
        embed.set_footer(text="use >> before every command!")
        await ctx.send(embed=embed)

    @help.command(name="animals")
    async def help_animal(self,ctx):
        embed = discord.Embed(title="🐶Animal commands🐶")
        embed.add_field(name="⠀", value="`catfact`, `dogfact`, `pandafact`, `foxfact`, `birdfact`, `koalafact`, `kangaroofact`, `racoonfact`, `elephantfact`, `giraffefact`, `whalefact`, `dog`, `cat`, `panda`, `redpanda`, `bird`, `fox`, `koala`, `kangaroo`, `racoon`, `whale`")
        embed.set_footer(text="use >> before every command!")
        await ctx.send(embed=embed)
    



def setup(client):
    client.add_cog(Help(client))