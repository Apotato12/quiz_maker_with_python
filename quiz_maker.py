import os

file_name = "quiz.txt"

def ask_for_the_question():
    list_of_questions = []
    answers = {}
    while True:
        question = input("enter a question:")
        if question in list_of_questions:
            print("question has already been added")
            continue

        list_of_questions.append(question)
        print ("question has been added")

        answers['a'] = input("Please enter option a: ")
        answers['b'] = input("Please enter option b: ")
        answers['c'] = input("Please enter option c: ")
        answers['d'] = input("Please enter option d: ")
        correct_answer = input("Please enter the correct answer (a, b, c, or d): ")

        return answers, correct_answer

        new_question = input("Do you want to add another question? (y or n): ")
        if new_question == "y":
            continue
        elif new_question == "n":
            break


def make_file():
    if not os.path.exists(file_name):
        open (file_name, "w")
    else:
        print("file already exists")

def actual_program():
    make_file()
    ask_for_the_question()


actual_program()