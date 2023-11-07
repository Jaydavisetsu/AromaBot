'''
Authors: Autumn Harrison & Jayden Davis
Date: 2023-11-06
Course: CSCI 2910 
Document Name: Aroma.py


'''
import discord
from discord.ext import commands
import random

#Create a bot instance
intents = discord.Intents.all()
intents.members = True
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix="!", )
guild = bot.get_guild(1171269987525197837)


#Print a status message when Aroma is ready
@bot.event
async def on_ready(): 
    print(f'Logged in as {bot.user.name}')

#-------------------------------------------
#Simple Commands? 

 #create a list of all commands users can use
command_list = [
    "!command1 - Description of command 1",
    "!command2 - Description of command 2",
    "!command3 - Description of command 3",
    #add more later
]
command_msg = f"Check out these command delicacies:\n" + "-----Aroma Commands-----\n" + "\n".join(command_list)
    
@bot.command()
async def commands(ctx):
    await ctx.send(command_msg)

@bot.command()
async def bonjour(ctx): 
    await ctx.send(f'Bonjour {ctx.author.mention}! :3')

#-------------------------------------------
#Greeting New Joins

#List of Welcome Messages
welcome_messages = [
     
     "Welcome to the Kitchen, {mention}!",
     "A new sous-chef has appeared, hey {mention}!",
     "Cooking up a warm welcome for {mention}!",
     "Hey, {mention}! Ready to cook?",
     "New chef in town: {mention}!",
     "Bonjour, {mention}!",
 ]
 
@bot.event
async def on_member_join(member): 
    origin_channel = bot.get_channel(1171269987525197837)

    if origin_channel: 
        #random welcome messages
        random_welcome = random.choice(welcome_messages)

        #customize so that it will @ the user
        welcome_msg = random_welcome.format(mention=member.mention)

        # Format commands again
        command_msg = f"To get you started, explore my array of commands:\n" + "-----Aroma Commands-----\n" + "\n".join(command_list)

        # Send the welcome message with the list of commands to the channel
        await origin_channel.send(welcome_msg)
        await origin_channel.send(command_msg)

        


#Run the bot with token
bot.run('MTE3MTI3NTA5OTMxMjIzNDU3OQ.Gn2HkF.KZ84vMS9_1roKDtB3K6wVSZE3o5HAAe-Sm2Buk')