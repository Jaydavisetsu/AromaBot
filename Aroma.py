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
from RecipeList import Recipe_List
from RecipeList import Seasonal_List


'''#Json Stuff
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
'''

response = requests.get('https://opentdb.com/api.php?amount=50')
print(response.status_code)
print(response.json())

response_data = response.json()
Questions = response_data =['trivia_questions']

for question in Questions:
    Category = response.json()['category'][0]['category']
    Questions = response.json()['question'][0]['question']
    CorrectAnswer = response.json()['correctAnswer'][0]['correct_answer']
    IncorrectAnswers = response.json()['incorrectAnswer'][0]['incorrect_answers']

    print("**Category**:", Category)
    print("**Question**:", Questions)
    print("**Correct Answer**:", CorrectAnswer)
    print("**Incorrect Answers**:", IncorrectAnswers)


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
• `!tips` - Randomly unlock kitchen secrets to discover cooking tips. 🍳✨• `!tips` - Randomly unlock kitchen secrets to discover cooking tips. 🍳✨
• `!getRecipes` - Want to find a recipe? Use this command to get our DM started! 🍕🌮 
• `!xp` - Find out how much XP you have. 🎮
• `!leaderboard` - Explore your XP ranking among chefs. 🏆


'''
  #add more later

#command_msg = f"Check out these command delicacies:\n" + "-----Aroma Commands-----\n" + "\n".join(command_list)


@bot.command()
async def commands(ctx):
    await ctx.send(f"{ctx.author.mention} \n {command_list}")

#bot will say bonjour
@bot.command()
async def bonjour(ctx): 
    await ctx.send(f'Bonjour {ctx.author.mention}! :3')

    await ctx.message.add_reaction('❤️')

#bot will provide mission statement
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

#bot will randomly display tips
@bot.command()
async def tips(ctx): 
    origin_channel = bot.get_channel(1171269987525197837)

    if origin_channel:
        random_tip = random.choice(cooking_tips)
        last_hyphen_index = random_tip.rfind('-')  # Find the last hyphen
        if last_hyphen_index != -1:
            tip = random_tip[:last_hyphen_index].strip()  # Extract the tip
            author = random_tip[last_hyphen_index + 1:].strip()  # Extract the author
            tip_message = f"🍳 **Cooking Tip** 🍳\n\n**Tip**: {tip}\n\n**Author**: {author}"
            await ctx.send(f"{ctx.author.mention}, \n {tip_message}")
        
#uhhh bot will do something    
@bot.command()
async def recipelist(ctx): 
 await ctx.send(f"{ctx.author.mention} \n {Recipe_List}")

@bot.command()
async def seasonallist(ctx): 
 await ctx.send(f"{ctx.author.mention} \n {Seasonal_List}")


#bot will start the recipe dm process
@bot.command()
async def getRecipes(ctx):

   
        user = ctx.author

        initial_msg = (
        "🍲 **Welcome to the Recipe Search!**🍳\n\n"
        "** [NOTE]: Replace <ingredient> with YOUR ingredient . . .(e.g. Broccoli) ** \n"
        "To search for a recipe, use the following commands:\n"
        "- `!searchByIngredient <ingredient>` - Search recipes by ingredients you have on hand 🥦\n"
        "- `!searchByCuisine <cuisine>` - Search recipes by cuisines from all over the world! 🌎\n"
        "- `!searchByName <name>` - Search recipes by name (e.g. Apple Pie) 🍽️\n"
        "- `!searchByCategory <category>` - Search recipes based on category (e.g. seafood, pork, beef, etc.)\n"
        "- `!seasonalRecipe` - Stay updated with trending seasonal dishes! 🎲\n"

        )
        #send the dm 
        await user.send(initial_msg)


#bot will search by ingredient
@bot.command()
async def searchByIngredient(ctx):
    await ctx.send("Search is unavailable.")

#bot will search by cuisine
@bot.command()
async def searchByCuisine(ctx):
    await ctx.send("Search is unavailable.")

#bot will search by dish name
@bot.command()
async def searchByName(ctx):
    await ctx.send("Search is unavailable.")

#bot will search by category
@bot.command()
async def searchByCategory(ctx):
    await ctx.send("Search is unavailable.")

#bot will display seasonal recipe
@bot.command()
async def seasonalRecipe(ctx):
    await ctx.send("Unavailable.")

@bot.command()
async def xp(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author

    user_id = member.id
    xp = user_xp_data.get(user_id, 0)

    await ctx.send(f"{member.display_name} has {xp} XP!")

@bot.command()
async def leaderboard(ctx):
    # Sort users by XP in descending order
    users = ctx.guild.members

    sorted_users = sorted(users, key=lambda user: user_xp_data.get(user.id, 0), reverse=True)

    # Create a formatted leaderboard
    leaderboard_msg = "🏆 **Aroma XP Leaderboard** 🏆\n\n"

    for index, user in enumerate(sorted_users[:10], start=1):
        xp = user_xp_data.get(user.id, 0)
        leaderboard_msg += f"{index}. {user.display_name}: {xp} XP\n"
    # Send the leaderboard to the channel
    await ctx.send(leaderboard_msg)

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


#BEGIN IMPLEMENTING THE XP SYSTEM (EVENTS AND COMMANDS)     

XP_PER_MESSAGE = 5
XP_SEARCH_REWARD = 20
XP_REACT = 15
#XP_TRIVIA_SCORE = 0
user_xp_data = {}
xp_commands = ['!searchByIngredient', '!searchByCuisine', '!searchByName', '!searchByCategory', '!seasonalRecipe']


@bot.event
async def on_message(message):
    server = message.guild
    author = message.author

    if message.author.bot:
        return  # Ignore messages from bots

    # Check if the message command should count for XP
    if any(message.content.startswith(cmd) for cmd in xp_commands):
        await process_search_command(message.author, message.content)

    # This will prevent any messages starting with ! commands from counting
    if message.content.startswith('!'):
        await bot.process_commands(message)
        return
    
    
    user_id = message.author.id
    user_xp_data.setdefault(user_id, 0)
    user_xp_data[user_id] += XP_PER_MESSAGE

    await check_and_assign_roles(message.author, message)

    await bot.process_commands(message)

async def process_search_command(author, content):
    user_id = author.id
    user_xp_data.setdefault(user_id, 0)
    user_xp_data[user_id] += XP_SEARCH_REWARD


async def check_and_assign_roles(user, message):
    user_id = user.id
    xp = user_xp_data.get(user_id, 0)

    if xp >= 100:
        roles = [
            {'name': 'Novice Chef', 'xp_required': 100},
            {'name': 'Sous Chef', 'xp_required': 400},
            {'name': 'Culinary Artisan', 'xp_required': 600},
            {'name': 'Gourmet Maestro', 'xp_required': 1000},
            {'name': 'Master Chef', 'xp_required': 1500}
        ]

        for role_info in roles:
            role_name = role_info['name']
            xp_required = role_info['xp_required']

            role = discord.utils.get(message.guild.roles, name=role_name)

            if role and role not in user.roles and xp >= xp_required:
                try:
                    await user.add_roles(role)
                    await message.channel.send(f'{user.mention} has leveled up to {role_name}! 🌟')
                except Exception as e:
                    print(f'Unable to add roles: {e}')

@bot.command()
async def search(ctx):
    user_id = ctx.author.id
    user_xp_data.setdefault(user_id, 0)
    user_xp_data[user_id] += XP_SEARCH_REWARD
    await ctx.send(f"Congratulations Chef! You earned {XP_SEARCH_REWARD} XP for recipe hunting!")

@bot.command()
async def check_xp(ctx):
    user_id = ctx.author.id
    xp = user_xp_data.get(user_id, 0)
    await ctx.send(f"Your current XP: {xp}")


@bot.event
async def on_reaction_add(reaction, user):
        #check make sure its not Aroma
        if not user.bot: 
            # award xp
            user_id = user.id
            user_xp_data.setdefault(user_id, 0)
            user_xp_data[user_id] += 15
        

#Run the bot with token
bot.run('MTE3MTI3NTA5OTMxMjIzNDU3OQ.G2P7vA.xHlQ-DOF9KzWNQrZHZMKfiEwoZCtY50MG-70pE')