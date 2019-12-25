# discordclient.py

import os
from dotenv import load_dotenv

import discord

# My own user created modules
import openweathermapapi

# Loads the .env located in the '.' or current directory
load_dotenv()
# Sets the 'token' variable to the value os.getenv() calls on 'DISCORD_TOKEN'
token = os.getenv('DISCORD_TOKEN')

# Creates a client
client = discord.Client()

# Sets a new definition to client.event(on_ready())
# on_ready() is when the bot boots up
@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")
    '''for channel in client.get_all_channels():
        if (type(channel) is discord.TextChannel):
            try:
                #await channel.send(f"Howdy y\'all it\'s me {client.user}!")
                #await channel.send("shut up Joaquin >:(")
            except discord.Forbidden:
                pass'''
# Sets a new definition to client.event(on_message(message))
# on_message(message) is when a message is sent in a text channel the bot can see
# Parameter (message) is the message that was sent to the text channel
@client.event
async def on_message(message):
    if (message.author.bot): # Will only react to messages sent from non-bots
        return
    elif (message.content[0] == '+'): # '+' is how to call the bot
        channel = message.channel
        if (message.content[1:] == ''):
            await channel.send("Did sssomebody call")
        elif (message.content[1:6] == 'copy '):
            await channel.send(message.content[6:])
        elif (message.content[1:9] =='weather '):
            weatherText = openweathermapapi.requestWeatherData(message.content[9:])
            await channel.send(weatherText)
        elif (message.content[1:9] == 'Joaquin'):
            await channel.send(":angry:")
        else:
            await channel.send("Command doesss not exissst")

client.run(token)