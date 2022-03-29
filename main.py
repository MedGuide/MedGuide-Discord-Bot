import discord
import os
import asyncpg
from discord.ext import commands
# from discord.ext.commands import

async def create_db_pool():
    bot.pg_con = await asyncpg.create_pool(database="medguide",user="postgres",password="abelroy")

bot = commands.Bot(command_prefix='dr 'or when_mentioned_or)
# bot.remove_command('help')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Unloaded {extension}')

@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'Reloaded {extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

# @bot.event
# async def on_ready():
#     print("Ready.")
#
# @bot.command()
# async def check(ctx):
#     await ctx.send("Check.")
#
# @bot.command()
# async def survey(ctx):
#     await ctx.send("Under maintenance.")

bot.loop.run_until_complete(create_db_pool())
bot.run("TOKEN")
