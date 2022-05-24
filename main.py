import json
import random

points = 0
lifelines = {1: "fifty-fifty", 2: "reject one of two"}


def Print_question_and_possibilities_and_get_the_answer(category, question_numb, abcd):
    print(category[question_numb]["pytanie"])
    for answer_letter in abcd:
        print(answer_letter + ": " + category[question_numb][answer_letter])
    if len(lifelines) > 0:
        if len(lifelines) > 1: print("Remaining lifelines:")
        else: print("Remaining lifeline:")
    for lifeline in lifelines:
        print(lifeline)
    user_answer = input("Your answer:")
    return user_answer

def Fifty_fifty(category, question_numb):
    abcd_list = ['a','b','c','d']
    abcd_list.remove(category[question_numb]["correct_answer"])
    wrong_answer = random.random(abcd_list)
    abcd_list_after_fifty_fifty = [category[question_numb]["correct_answer"],wrong_answer]
    abcd_list_after_fifty_fifty.sort()
    return Print_question_and_possibilities_and_get_the_answer(category, question_numb, abcd_list_after_fifty_fifty)

def Answering_mechanism(category):
    global points
    global questions_count
    abcd = ['a','b','c','d']
    questions_count += 1
    question_number = random.randint(0,len(category)-1)
    user_answer = Print_question_and_possibilities_and_get_the_answer(category, question_number, abcd)
    if(user_answer == 1): Fifty_fifty(category, question_number)
    while(user_answer not in abcd or user_answer not in lifelines.keys()):
        if(len(lifelines) >0): print("Enter either a, b, c or d or choose a lifeline. Try again")
        else: print("Enter either a, b, c or d. Try again")
        user_answer = Print_question_and_possibilities_and_get_the_answer(category, question_number)
    if(user_answer == category[question_number]["correct_answer"]):
        print("Correct answer")
        points += 1
    else:
        print("Wrong answer, the correct answer is " + category[question_number]["correct_answer"])
    print("Twoje punkty: " + str(points) + "/" + str(questions_count))
    category.remove(category[question_number])
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
    Answering_mechanism(category)
print("Rozgrywka zakończona, twoje punkty: " + str(points) + "/" + str(questions_count))