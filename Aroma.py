'''
Authors: Autumn Harrison & Jayden Davis
Date: 2023-11-06
Course: CSCI 2910 
Document Name: Aroma.py


'''
import discord
from discord.ext import commands
import random
from CookingTips import cooking_tips
import requests

#Json Stuff
response = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?f=a')
print(response.status_code)
print(response.json())

response_data = response.json()
meals = response_data =['meals']

for meal in meals:
    MealName = response.json()['meals'][0]['strMeal']
    MealCategory = response.json()['meals'][0]['strCategory']
    MealArea = response.json()['meals'][0]['strArea']
    MealDescription = response.json()['meals'][0]['strInstructions']

    print("**Meal Name**:", MealName)
    print("**Meal Category**:", MealCategory)
    print("**Meal Origins**:", MealArea)
    print("**Meal Description**:", MealDescription)

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
#BOT COMMANDS

 #create a list of all commands users can use
command_list = '''🍽️ **Aroma Commands** 🍽️
Check out these command delicacies:
• `!commands` - Display all of my usable commands at any time.
• `!bonjour` - Come say hi to me! (You could get some XP . . . just saying.) 😄
• `!aboutAroma` - Learn more about me. 📖
• `!tips` - Randomly unlock kitchen secrets to discover cooking tips. 🍳✨
'''
  #add more later

#command_msg = f"Check out these command delicacies:\n" + "-----Aroma Commands-----\n" + "\n".join(command_list)
    
@bot.command()
async def commands(ctx):
    await ctx.send(f"{ctx.author.mention} \n {command_list}")

@bot.command()
async def bonjour(ctx): 
    await ctx.send(f'Bonjour {ctx.author.mention}! :3')

@bot.command() 
async def aboutAroma(ctx): 
    mission_statement = (
        "🍽️ **Mission Statement** 🍽️\n\n"
        "As the Aroma bot, my goal is to take you on a culinary adventure like no other. 🌮🍕🍜\n\n"
        "📚 **What I Bring to the Table** 📚\n"
        "Discover a world of delightful recipes. Save your favorites. Share with friends.\n"
        "Simplify your cooking experience with a vast recipe database. Find recipes based on ingredients, names, or origins. 🌎🥘🍳\n\n"
        "🎮 **The Secret Ingredient** 🎮\n"
        "I bring a game-like atmosphere to the kitchen! Earn achievement badges 🏅, gain experience points, top the leaderboards 📊,\n"
        "enjoy features like recipe roulette 🎲 and fun recipe quizzes ❓.\n\n"
        "🍁🌻 **Seasonal Recommendations** 🌞❄️\n"
        "Stay fresh with my seasonal recipe suggestions that match the current season. 🍁🌻\n\n"
        "Ready to embark on a flavorful journey with me? 😊"
    )
    await ctx.send(f"{ctx.author.mention} \n {mission_statement}")

@bot.command()
async def tips(ctx): 
    origin_channel = bot.get_channel(1171269987525197837)

    if origin_channel:
        random_tip = random.choice(cooking_tips)
        last_hyphen_index = random_tip.rfind('-')  # Find the last hyphen
        if last_hyphen_index != -1:
            tip = random_tip[:last_hyphen_index].strip()  # Extract the tip
            author = random_tip[last_hyphen_index + 1:].strip()  # Extract the author
            tip_message = f"🍳 Cooking Tip 🍳\n\n**Tip**: {tip}\n\n**Author**: {author}"
            await ctx.send(f"{ctx.author.mention}, \n {tip_message}")
        
    '''random_tip = random.choice(cooking_tips)
        await ctx.send(f"{ctx.author.mention}, here's a cooking tip: \n {random_tip}")'''


#-------------------------------------------
#BOT EVENTS

#List of Welcome Messages
welcome_messages = [
     
     "Welcome to the Kitchen, {mention}!",
     "A new sous-chef has appeared, hey {mention}!",
     "Cooking up a warm welcome for {mention}!",
     "Hey, {mention}! Ready to cook?",
     "New chef in town: {mention}!",
     "Bonjour, {mention}!",
 ]
 
 #New member join message
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
bot.run('MTE3MTI3NTA5OTMxMjIzNDU3OQ.GmZvb3.N3JfoYTwLBSKk-yFZO9Qlzoa09_rm5tQvA28jI')