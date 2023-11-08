'''
Authors: Autumn Harrison & Jayden Davis
Date: 2023-11-07
Course: CSCI 2910 
Document Name: Trivia.py

Trivia questions based on different categories..multiple choice

'''

import requests 

#Request the API link
API_URL = "https://opentdb.com/api.php?amount=50"


def get_trivia_questions(category="any")
    params = {
        "amount": 50, #how many questions to get
        "category": category, #selected category
        "type": "multiple", #multiple choice questions
    }

    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        questions = data.get("results")
        return questions
    else: 
        return None