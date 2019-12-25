# cog.py

from discord import File
from discord.ext import commands
from random import randrange

# My OpenWeatherAPI module
from openweathermapapi import requestWeatherData

class API(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name= 'weather', help= 'Given a zip code returns the weather.')
    async def weather(self, ctx, zipCode: int):
        await ctx.send(requestWeatherData(zipCode))


class BasicCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name= 'copy', help= 'Sends a copy of the specified message to the same channel.')
    async def copy(self, ctx, *args):
        await ctx.send(' '.join(args))

    @commands.command(name= 'hello', help= 'Greets the user.')
    async def hello(self, ctx):
        await ctx.send(f"Hello, {ctx.message.author}.")

    @commands.command(name= 'image', help= 'Sends a picture of a python.')
    async def image(self, ctx):
        filePath = "images\\snake1.jpg"
        discordFile = File(filePath)
        await ctx.send(file= discordFile)

    @commands.command(name= 'roll', help= 'Rolls X (numDice) with max value of Y (maxDiceValue).')
    async def roll(self, ctx, numDice: int, maxDiceValue: int):
        outputString = ''
        sum = 0
        for i in range(numDice):
            randomInteger = randrange(maxDiceValue)
            sum += randomInteger + 1
            outputString += f"Dice #{i + 1}: {randomInteger + 1}\n"
        outputString += f"Sum is: {sum}"
        await ctx.send(outputString)
