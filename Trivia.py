'''
Authors: Autumn Harrison & Jayden Davis
Date: 2023-11-07
Course: CSCI 2910 
Document Name: Trivia.py

Trivia questions based on different categories..multiple choice

'''


#from discord.ext import commands
import requests


def fetch_trivia_data():

    response = requests.get('https://opentdb.com/api.php?amount=50')
    
    if response.status_code == 200:
        # Assuming the API response is in JSON format
        trivia_data = response.json()
        return trivia_data
    else:
        return None

def get_trivia_questions(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad requests
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching trivia questions: {e}")
        return None

async def display_trivia_questions(trivia_data, ctx):
    if trivia_data:
        # Process and display trivia questions (customize based on the API response structure)
        for question in trivia_data['results']:
            message = f"Category: {question['category']}\nQuestion: {question['question']}\nOptions:\n"
            options = [f"{i + 1}. {option}" for i, option in enumerate(question['incorrect_answers'])]
            options.append(f"{len(question['incorrect_answers']) + 1}. {question['correct_answer']}")
            message += "\n".join(options)
            await ctx.send(message)



'''

#Request the API link
#API_URL = "https://opentdb.com/api.php?amount=50"

response = requests.get('https://opentdb.com/api.php?amount=50')
print(response.status_code)
#print(response.json())

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


def get_trivia_questions(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad requests
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching trivia questions: {e}")
        return None

async def display_trivia_questions(trivia_data, ctx):
    if trivia_data:
        # Process and display trivia questions (customize based on the API response structure)
        for question in trivia_data['results']:
            message = f"Category: {question['category']}\nQuestion: {question['question']}\nOptions:\n"
            options = [f"{i + 1}. {option}" for i, option in enumerate(question['incorrect_answers'])]
            options.append(f"{len(question['incorrect_answers']) + 1}. {question['correct_answer']}")
            message += "\n".join(options)
            await ctx.send(message)

@bot.command()
async def trivia(ctx, num_questions: int = 1):
    # Request the API link with the specified number of questions
    api_url = f"https://opentdb.com/api.php?amount={num_questions}"

    # Get trivia questions
    trivia_data = get_trivia_questions(api_url)

    # Display trivia questions
    display_trivia_questions(trivia_data, ctx)
    await ctx.send()
   '''


