# Modules
import discord
import os
import asyncpg
from discord.ext import commands
# from discord.ext.commands import

# Connecting database
async def create_db_pool():
    bot.pg_con = await asyncpg.create_pool(...)

bot = commands.Bot(command_prefix='dr 'or when_mentioned_or)
# bot.remove_command('help')

# Load/Unload/Reload
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
<<<<<<< HEAD
bot.run(TOKEN)
=======
bot.run("TOKEN")
>>>>>>> fafbc6b866da3532972f922f4236671f570972d1
