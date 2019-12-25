# discordbot.py

import os
from dotenv import load_dotenv

from discord.ext import commands
from discord import Guild

# My own user created modules
import cog

# Loads the .env located in the '.' or current directory
load_dotenv()
# Sets the 'token' variable to the value os.getenv() calls on 'DISCORD_TOKEN'
token = os.getenv('DISCORD_TOKEN')

# Creates a bot with all calls to the bot requiring a '+' as a prefix
bot = commands.Bot(command_prefix='+')

@bot.event
async def on_ready():
    print(f"{bot.user.name} ready and online")

@bot.event
async def on_message(message):
    channel = message.channel
    author = message.author
    joaquin = channel.guild.get_member(260275649665695744)
    if (author == joaquin and channel.id == 314917657709379587):
        await channel.send(f"Shut up Joaquin :angry:")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        await ctx.send(error)
    elif isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send(error)
    elif isinstance(error, commands.errors.BadArgument):
        await ctx.send(error)
    else:
        await ctx.send(error)
        raise error

# Add API cog to the bot
bot.add_cog(cog.API(bot))
bot.add_cog(cog.BasicCommands(bot))

bot.run(token)