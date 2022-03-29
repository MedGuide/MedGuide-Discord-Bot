import discord
from discord.ext import commands, tasks

class General(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(status=discord.Status.idle, activity = discord.Game(""))
        print("Bot is Running...")

    @commands.command(aliases=["general check"])
    async def generalcheck(self, ctx):

        def check(ms):
            return ms.channel == ctx.message.channel and ms.author == ctx.message.author

        def checkyn(ms):
            return ms.channel == ctx.message.channel and ms.author == ctx.message.author# and return ms.message == ("y"or"n")

        await ctx.send(content="What is your name? [Enter 'Anonymous' for anonymous entry]")
        msg0 = await self.bot.wait_for('message', check=check)
        name = msg0.content

        await ctx.send(content="What is your age?")
        msg1 = await self.bot.wait_for('message',check=check)
        age = msg1.content

        await ctx.send("Where do you live? [Write your Pincode]")
        msg2 = await self.bot.wait_for('message',check=check)
        pincode = msg2.content

        await ctx.send("Do you have Common Cold in the last 6 days? [Enter y/n]")
        msg01 = await self.bot.wait_for('message',check=checkyn)
        cold = msg01.content

        await ctx.send("Do you have Fatigue in the last 6 days? [Enter y/n]")
        msg02 = await self.bot.wait_for('message',check=checkyn)
        fatigue = msg02.content

        await ctx.send("Do you have Nausea in the last 6 days? [Enter y/n]")
        msg03 = await self.bot.wait_for('message',check=checkyn)
        nausea = msg03.content

        await ctx.send("Do you have Fever in the last 6 days? [Enter y/n]")
        msg04 = await self.bot.wait_for('message',check=checkyn)
        fever = msg04.content

        await ctx.send("Do you have Sore Throat in the last 6 days? [Enter y/n]")
        msg05 = await self.bot.wait_for('message',check=checkyn)
        sorethroat = msg05.content

        embed = discord.Embed(title="Covid Check Report", description=f"For {name}",color=discord.Colour.teal())
        embed.add_field(name="Age",value=f"{age}",inline=True)
        embed.add_field(name="Pincode",value=f"{pincode}",inline=False)
        embed.add_field(name="Symptoms",value=f"""
        Common Cold : {cold}
        Fatigue : {fatigue}
        Nausea : {nausea}
        Fever : {fever}
        Sore Throat : {sorethroat}
        """,inline=False)

        embed.set_footer(text=f"By User {ctx.author}")
        await ctx.send(embed=embed)

        await self.bot.pg_con.execute("INSERT INTO ")

    @commands.command()#PING
    async def ping(self, ctx):
        embed = discord.Embed(title = 'Pong !',colour = discord.Colour.green())
        embed.set_footer(text = f'Requested by {ctx.author}')
        embed.add_field(name='Bot Latency :',value=f'{round(self.bot.latency*100)} ms.\nNot Bad !? Not Good !?', inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(General(bot))
