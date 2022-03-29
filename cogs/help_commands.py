import discord
from discord.ext import commands, tasks

class Help_Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # @commands.group(aliases=['menu','h'])
    # async def help(self, ctx):
    #     embed = discord.Embed(title="MedGuide",colour=discord.Colour.teal())
    #     embed.add_field(
    #         name = ""
    #     )
    #     await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help_Commands(bot))
