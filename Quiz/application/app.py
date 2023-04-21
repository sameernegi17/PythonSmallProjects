from view.view import *

quiz = {
    "Is sun is star" : ["yes", "no"],
    "which keyword is used to create a function in Python" : ["create","def","func"],
    "what is 2 *  2 + 3 ?" : [10,0,7]
}

correct_answers = [0,1,2]

def start_quiz():
    score = 0
    question_counter = 0
    for question, answer in quiz.items():
        output = create_quiz_window(question,answer)
        if output:
            for key,value in output.items():
                if value and int(key) == correct_answers[question_counter]:
                    score+=1
        else:
            break
        question_counter+=1


    show_score(score)

if __name__ == "__main__":
    start_quiz()



