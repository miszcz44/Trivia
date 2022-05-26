import json
import random

points = 0
lifelines = {1: "fifty-fifty", 2: "reject one of two"}
used_lifelines = []



def Print_question_and_possibilities_and_get_the_answer(category, question_numb, list_of_possible_answers):
    print(category[question_numb]["pytanie"])
    Print_user_possibilities(category, question_numb, list_of_possible_answers)
    user_answer = input("Your answer:")
    return user_answer

def Print_user_possibilities(category, question_numb, list_of_possible_answers):
    for answer_letter in list_of_possible_answers:
        print(answer_letter + ": " + category[question_numb][answer_letter])
    if len(lifelines) > 0 and len(used_lifelines) == 0:
        if len(lifelines) > 1: print("Remaining lifelines:")
        else: print("Remaining lifeline:")
        for lifeline in lifelines:
            print(str(lifeline) + ". " + lifelines[lifeline])

def Fifty_fifty(category, question_numb, list_of_possible_answers):
 #   Update_lifelines("fifty-fifty")
    Remove_two_wrong_answers(category, question_numb, list_of_possible_answers)
    return Print_question_and_possibilities_and_get_the_answer(category, question_numb, list_of_possible_answers)

#def Update_lifelines(lifeline_type):
 #   for lifeline in lifelines:
  #      if lifelines[lifeline] == lifeline_type:
 #           temporary_lifeline_number = lifeline
 #           lifelines.pop(lifeline)
 #   for lifeline in lifelines:
 #       if(lifeline > temporary_lifeline_number):
#            lifeline -= 1

def Remove_two_wrong_answers(category, question_numb, list_of_possible_answers):
    list_of_possible_answers.remove(category[question_numb]["correct_answer"])
    wrong_answer = random.choice(list_of_possible_answers)
    #print(wrong_answer)
    list_of_possible_answers = [category[question_numb]["correct_answer"], wrong_answer]
    list_of_possible_answers.sort()

def Update_lifelines():
    for _ in range(len(used_lifelines)):
        for key, value in lifelines:
            if(value == used_lifelines[0]):
                lifelines.pop(key)


def Answering_mechanism(category):
    global points
    global questions_count
    global used_lifelines
    list_of_possible_answers = ['a','b','c','d']
    questions_count += 1
    question_number = random.randint(0,len(category)-1)
    user_answer = Print_question_and_possibilities_and_get_the_answer(category, question_number, list_of_possible_answers)
    print(user_answer)
    if(user_answer == "1"):
        print("abcd")
        used_lifelines.append("fifty-fifty")
        Fifty_fifty(category, question_number, list_of_possible_answers)
        print(list_of_possible_answers)
    while(user_answer not in list_of_possible_answers and user_answer not in lifelines.keys()):
        if(len(lifelines) > 0): print("Choose one of possible answers or take a lifeline. Try again")
        else: print("Choose one of possible answers. Try again")
        user_answer = Print_question_and_possibilities_and_get_the_answer(category, question_number, list_of_possible_answers)
    if(user_answer == category[question_number]["correct_answer"]):
        print("Correct answer")
        points += 1
    else:
        print("Wrong answer, the correct answer is " + category[question_number]["correct_answer"])
    print("Twoje punkty: " + str(points) + "/" + str(questions_count))
    category.remove(category[question_number])
    Update_lifelines()
    used_lifelines = []

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