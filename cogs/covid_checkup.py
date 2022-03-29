import discord
from discord.ext import commands, tasks

class Covid_Checkup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def highlowint(a):
        if a.lower() == 'high':
            return 1
        else:
            return 0

    @commands.command(aliases=["covid check","checkcovid"])
    async def covidcheck(self, ctx):

        def check(ms):
            return ms.channel == ctx.message.channel and ms.author == ctx.message.author

        def checkyn(ms):
            return ms.channel == ctx.message.channel and ms.author == ctx.message.author# and return ms.message == ("y"or"n")

        await ctx.send(content="What is your age?")
        msg1 = await self.bot.wait_for('message',check=check)
        age = msg1.content

        await ctx.send("Where do you live? [Write your Pincode]")
        msg2 = await self.bot.wait_for('message',check=check)
        pincode = msg2.content

        await ctx.send("Do you have FEVER in the last 6 days? [Enter yes/no]")
        msg01 = await self.bot.wait_for('message',check=checkyn)
        fever = msg01.content

        await ctx.send("Do you have COUGH in the last 6 days? [Enter yes/no]")
        msg02 = await self.bot.wait_for('message',check=checkyn)
        cough = msg02.content

        await ctx.send("Do you have TIREDNESS in the last 6 days? [Enter yes/no]")
        msg03 = await self.bot.wait_for('message',check=checkyn)
        tiredness = msg03.content

        await ctx.send("Do you have LOSS OF TASTE in the last 6 days? [Enter yes/no]")
        msg04 = await self.bot.wait_for('message',check=checkyn)
        loss_of_taste = msg04.content

        await ctx.send("Do you have DIFFICULTY BREATHING in the last 6 days? [Enter yes/no]")
        msg05 = await self.bot.wait_for('message',check=checkyn)
        difficulty_breathing = msg05.content

        name = ctx.message.author
        embed = discord.Embed(title="Covid Check Report",color=discord.Colour.teal())
        embed.add_field(name="Age",value=f"{age}",inline=True)
        embed.add_field(name="Pincode",value=f"{pincode}",inline=False)
        embed.add_field(name="Symptoms",value=f"""
        Fever : {fever}
        Cough : {cough}
        Tiredness : {tiredness}
        Loss of Taste : {loss_of_taste}
        Difficulty Breathing : {difficulty_breathing}
        """,inline=False)

        embed.set_footer(text=f"For User {name}")
        await ctx.send(embed=embed)

        if fever.lower() == ('yes'or'y'):
            fever = 1
        else:
            fever = 0
        if cough.lower() == ('yes' or 'y'):
            cough = 1
        else:
            cough = 0
        if tiredness.lower() == ('yes' or 'y'):
            tiredness = 1
        else:
            tiredness=0
        if loss_of_taste.lower() == ("yes" or "y"):
            loss_of_taste=1
        else:
            loss_of_taste=0
        if difficulty_breathing.lower() == ("yes"or"y"):
            difficulty_breathing=1
        else:
            difficulty_breathing=0


        user_id = int(ctx.message.author.id)
        data = await self.bot.pg_con.fetch("SELECT * FROM symptoms WHERE user_id = $1",user_id)
        if not data:
            await self.bot.pg_con.execute("INSERT INTO symptoms(user_id, age, pincode, fever, cough, tiredness, loss_of_taste, difficulty_breathing) VALUES($1,$2, $3,$4,$5,$6,$7,$8)",user_id, int(age),int(pincode),fever,cough,tiredness, loss_of_taste, difficulty_breathing)

        

def setup(bot):
    bot.add_cog(Covid_Checkup(bot))
