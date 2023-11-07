'''
Authors: Autumn Harrison & Jayden Davis
Date: 2023-11-06
Course: CSCI 2910 
Document Name: Aroma.py


'''
import discord
from discord.ext import commands

#Create a bot instance
bot = commands.Bot(command_prefix='!')

#Print a message when Aroma is ready
@bot.event
async def on_ready(): 
    print(f'Logged in as {bot.user.name}')

# Greetings 
@bot.command()
async def hello(ctx): 
    await ctx.send('Hiii :3')

#Run the bot with token
bot.run('MTE3MTI3NTA5OTMxMjIzNDU3OQ.GDem8Q.PUWpU2ByHR9sbpUD4IZkKXzNWciIzuriyZDv9A')