import os

file_name = "quiz.txt"

def options_for_question():
    answers = []
    def answers():
        answers['a'] = input("Please enter option a: ")
        answers['b'] = input("Please enter option b: ")
        answers['c'] = input("Please enter option c: ")
        answers['d'] = input("Please enter option d: ")
        correct_answer = input("Please enter the correct answer (a, b, c, or d): ")


def ask_for_the_question():
    list_of_questions = []
    while True:
        question = input("enter a question:")
        if question in list_of_questions:
            print("question has already been added")
            continue
        list_of_questions.append(question)
        print ("question has been added")
        
        answers = options_for_question()


def make_file():
    if not os.path.exists(file_name):
        open (file_name, "w")
    else:
        print("file already exists")

make_file()
ask_for_the_question()