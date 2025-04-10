import os

file_name = "quiz.txt"

def ask_for_the_question():
    list_of_questions = []
    while True:
        question = input("enter a question:")
        if question in list_of_questions:
            print("question has already been added")
            continue

        list_of_questions.append(question)
        print ("question has been added")
        answers = {}
        answers['a'] = input("Please enter option a: ")
        answers['b'] = input("Please enter option b: ")
        answers['c'] = input("Please enter option c: ")
        answers['d'] = input("Please enter option d: ")
        correct_answer = input("Please enter the correct answer (a, b, c, or d): ")

        return answers, correct_answer

        with open(file_name, "a") as file:
            file.write(f"Question: {question}\n")
            for option, answer in answers.items():
                file.write(f"Option {option}: {answer}\n")
            file.write(f"Correct Answer: {correct_answer}\n")
            file.write("\n")


def make_file():
    if not os.path.exists(file_name):
        open (file_name, "w")
    else:
        print("file already exists")

def actual_program():
    make_file()
    ask_for_the_question()


actual_program()