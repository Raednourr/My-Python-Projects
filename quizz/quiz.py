import quiz_auth
import time
import os
import json

questions_file = "projects/quizz/quiz_questions.json"


def quiz():
    score = 0   
    print("Welcome to the Quiz!")
    time.sleep(1)
    print("This is where the quiz questions would go.")
    time.sleep(1)
    if os.path.exists(questions_file) and os.path.getsize(questions_file) > 0:
        with open(questions_file, "r") as f:
            questions = json.load(f)
    else:
        questions = []

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        user_answer = input("Enter Answer: ").strip().lower()
        if user_answer == q["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    if score == 5:
        print(f"End of quiz!, Final Score: {score}, Full Mark!")
    else:
        print(f"End of quiz!, Final Score: {score}")


    # with open(questions_file, "w") as f:
    #     json.dump(questions, f, indent=4)

    
    


username, logged_in = quiz_auth.authenticate()
if logged_in:
    print(f"Welcome, {username}!")
    quiz()
else:
    print("Authentication failed. Please try again.")
    exit(1)