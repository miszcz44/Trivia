import json
import random

points = 0
lifelines = {"1": "fifty-fifty", "2": "reject-one-of-two"}
used_lifelines = []
category_numbers = ["1", "2", "3", "4", "5"]



def Print_question_and_possibilities_and_get_the_answer(question_numb, list_of_possible_answers):
    print(category[question_numb]["pytanie"])
    Print_user_possibilities(question_numb, list_of_possible_answers)
    user_answer = input("Your answer:")
    return user_answer

def Print_user_possibilities(question_numb, list_of_possible_answers):
    for answer_letter in list_of_possible_answers:
        print(answer_letter + ": " + category[question_numb][answer_letter])
    if len(lifelines) > 0 and len(used_lifelines) == 0:
        if len(lifelines) > 1: print("Remaining lifelines:")
        else: print("Remaining lifeline:")
        for lifeline in lifelines:
            print(str(lifeline) + ". " + lifelines[lifeline])

def Fifty_fifty(question_numb, list_of_possible_answers):
    Remove_two_wrong_answers(question_numb, list_of_possible_answers)
    return Print_question_and_possibilities_and_get_the_answer(question_numb, list_of_possible_answers)

def Remove_two_wrong_answers(question_numb, list_of_possible_answers_after_fifty_fifty):
    list_of_possible_answers_after_fifty_fifty.remove(category[question_numb]["correct_answer"])
    wrong_answer = random.choice(list_of_possible_answers_after_fifty_fifty)
    list_of_possible_answers_after_fifty_fifty = [category[question_numb]["correct_answer"], wrong_answer]
    list_of_possible_answers_after_fifty_fifty.sort()
    return list_of_possible_answers_after_fifty_fifty

def Update_lifelines():
    flag = 0
    for _ in range(len(lifelines)):
        for key, value in lifelines.items():
            if(value in used_lifelines):
                temp_key = key
                flag = 1
                break
    if(flag == 1):
        lifelines.pop(temp_key)

def Reject_one_of_two_answers(list_of_possible_answers, question_numb):
    lifeline_user_answers = Ask_for_two_answers(list_of_possible_answers)
    lifeline_user_answers = Remove_one_of_two_answers(lifeline_user_answers, question_numb)
    return lifeline_user_answers

def Ask_for_two_answers(list_of_possible_answers):
    print("Enter the answers you are curious about, one after another")
    lifeline_user_answers = []
    lifeline_user_answers.append(input())
    while(lifeline_user_answers[0] not in list_of_possible_answers):
        print("Enter one of the possible answers. Try again")
        lifeline_user_answers[0] = input()
    list_of_possible_answers.remove(lifeline_user_answers[0])
    lifeline_user_answers.append(input())
    while (lifeline_user_answers[1] not in list_of_possible_answers):
        print("Enter one of the possible answers. Try again")
        lifeline_user_answers[1] = input()
    return lifeline_user_answers

def Remove_one_of_two_answers(list_of_possible_answers, question_numb):
    list_of_possible_answers_after_rejection = ["a", "b", "c", "d"]
    if category[question_numb]["correct_answer"] in list_of_possible_answers:
        for i in range(len(list_of_possible_answers)):
            if(list_of_possible_answers[i] != category[question_numb]["correct_answer"]):
                list_of_possible_answers_after_rejection.remove(list_of_possible_answers[i])
    else:
        random_answer_of_two = random.choice(list_of_possible_answers)
        list_of_possible_answers_after_rejection.remove(random_answer_of_two)
    list_of_possible_answers_after_rejection.sort()
    return list_of_possible_answers_after_rejection



def Answering_mechanism():
    global points
    global questions_count
    global used_lifelines
    list_of_possible_answers = ['a', 'b', 'c', 'd']
    questions_count += 1
    question_number = random.randint(0, len(category)-1)
    user_answer = Print_question_and_possibilities_and_get_the_answer(question_number, list_of_possible_answers)
    if(user_answer == "1"):
        used_lifelines.append("fifty-fifty")
        list_of_possible_answers = Remove_two_wrong_answers(question_number, list_of_possible_answers)
        user_answer = Print_question_and_possibilities_and_get_the_answer(question_number, list_of_possible_answers)
    elif(user_answer == "2"):
        used_lifelines.append("reject-one-of-two")
        list_of_possible_answers = Reject_one_of_two_answers(list_of_possible_answers, question_number)
        user_answer = Print_question_and_possibilities_and_get_the_answer(question_number, list_of_possible_answers)
    while(user_answer not in list_of_possible_answers and (user_answer not in lifelines.keys() or len(used_lifelines) > 0)):
        if(len(lifelines) > 0 and len(used_lifelines) == 0): print("Choose one of possible answers or take a lifeline. Try again")
        else: print("Choose one of possible answers. Try again")
        user_answer = Print_question_and_possibilities_and_get_the_answer(question_number, list_of_possible_answers)
    if(user_answer == category[question_number]["correct_answer"]):
        print("Correct answer")
        points += 1
    else:
        print("Wrong answer, the correct answer is " + category[question_number]["correct_answer"])
    if(questions_count < 10):
        print("Your score: " + str(points) + "/" + str(questions_count))
    category.remove(category[question_number])
    Update_lifelines()
    used_lifelines = []

def Load_best_results_from_file():
    print("Best results:")
    place = 1
    with open("BestResults") as best_results_file:
        for line in best_results_file:
            line = line.strip()
            print(str(place) + "." + line + "/10")
            place += 1
    print()
    best_results_file.close()

def Save_best_results():
    best_results = Get_best_results()
    best_results = Update_best_results(best_results)
    with open("BestResults", "w") as best_results_file:
        for el in best_results:
            best_results_file.write(str(el) + "\n")
    best_results_file.close()

def Get_best_results():
    best_results = []
    with open("BestResults") as best_results_file:
        for line in best_results_file:
            best_results.append(int(line))
    best_results_file.close()
    return best_results

def Update_best_results(best_results):
    flag = 0
    for i in range(len(best_results)):
        if (points >= best_results[i]):
            position_for_result = i
            flag = 1
            break
    if(flag == 1):
        best_results.insert(position_for_result, points)
    elif(flag == 0 and len(best_results) < 5):
        best_results.append(points)
    if(len(best_results) > 5):
        best_results.remove(best_results[-1])
    return best_results


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
    print("1.Start\n2.Best results\n3.Quit")
    user_choice = int(input())
    while(user_choice != 1 and user_choice != 2 and user_choice != 3):
        print("Choose one of possible options. Try again")
        user_choice = int(input())
    if(user_choice == 3): break
    elif(user_choice == 2):
        Load_best_results_from_file()
        continue
    else:
        while(questions_count != 10):
            print("Choose Category:\n1.Sport\n2.Geography\n3.History\n4.Biology\n5.Chemistry")
            user_category_choice = input()
            while(user_category_choice not in category_numbers):
                print("Choose one of possible options. Try again")
                user_category_choice = input()
            if(int(user_category_choice) == 1): category = sport_questions
            elif(int(user_category_choice) == 2): category = geography_questions
            elif(int(user_category_choice) == 3): category = history_questions
            elif(int(user_category_choice) == 4): category = biology_questions
            elif(int(user_category_choice) == 5): category = chemistry_questions
            Answering_mechanism()
    Save_best_results()
    print("The game is over, your score: " + str(points) + "/" + str(questions_count))