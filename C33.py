import requests
import json
import random
import html

quit_app=""
correct_answers_count = 0
incorrect_answers_count = 0
while(quit_app!="quit"):
    request_api = requests.get("https://opentdb.com/api.php?amount=1&category=12&difficulty=easy&type=multiple")
    requests_text = request_api.text
    quiz_json = json.loads(requests_text)

    print("-----=====Welcome to the quizzing game!=====-----")
    print("Your question is: "+html.unescape(quiz_json['results'][0]['question']))
    answers = quiz_json['results'][0]['incorrect_answers']
    cor_ans = quiz_json['results'][0]['correct_answer']
    #print("---CORRECT IS:"+cor_ans)
    answers.append(cor_ans)
    shuffled_answers = answers
    random.shuffle(shuffled_answers)
    answer_number = 1
    for answer in shuffled_answers:
        print(str(answer_number) + ". "+ html.unescape(answer))
        answer_number+=1


    user_answer = input("Input your answer: ")
    answer_string = str(user_answer)
    
    try:
        answer_string_validate = shuffled_answers[int(answer_string)-1]
        if(answer_string_validate == cor_ans):
            print("Your answer is CORRECT!!!")
            correct_answers_count+=1
        else:
            print("Incorrect answer! Try again!")
            print("The CORRECT answer was: "+str(cor_ans))
            incorrect_answers_count+=1
    except:
        print("You entered a wrong number! Try again")

    quit_app=input("\nPress enter to continue or type 'quit' to quit the game").lower()

print("You had: "+str(correct_answers_count)+" correct answers and "+str(incorrect_answers_count)+" incorrect answers")