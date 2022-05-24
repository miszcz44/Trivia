import json
import random

points = 0
abcd = ['a','b','c','d']

def Print_question_get_answer(category, question_numb):
    print(category[question_numb]["pytanie"])
    print("a: " + category[question_numb]["a"])
    print("b: " + category[question_numb]["b"])
    print("c: " + category[question_numb]["c"])
    print("d: " + category[question_numb]["d"])
    user_answer = input("Your_answer:")
    return user_answer


def Answer_mechanism(category):
    global points
    global questions_count
    questions_count += 1
    question_number = random.randint(0,len(category)-1)
    user_answer = Print_question_get_answer(category, question_number)
    while(user_answer not in abcd):
        print("Enter either a, b, c or d. Try again")
        user_answer = Print_question_get_answer(category, question_number)
    if(user_answer == category[question_number]["correct_answer"]):
        print("Correct answer")
        points += 1
    else:
        print("Wrong answer, the correct answer is " + category[question_number]["correct_answer"])
with open("TriviaSport.json") as json_file:
    sport_questions = json.load(json_file)
with open("TriviaGeography.json") as json_file:
    geography_questions = json.load(json_file)
with open("TriviaHistory.json") as json_file:
   history_questions = json.load(json_file)
with open("TriviaBiology.json") as json_file:
    biology_questions = json.load(json_file)
with open("TriviaChemistry.json") as json_file:
   chemistry_questions = json.load(json_file)

category = ''
questions_count = 0
while(questions_count != 10):
    print("Choose Category:\n1.Sport\n2.Geography\n3.History\n4.Biology\n5.Chemistry")
    user_category_choice = int(input())
    if(user_category_choice == 1): category = sport_questions
    elif(user_category_choice == 2): category = geography_questions
    elif(user_category_choice == 3): category = history_questions
    elif(user_category_choice == 4): category = biology_questions
    elif(user_category_choice == 5): category = chemistry_questions
    Answer_mechanism(category)