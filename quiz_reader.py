import os
import random

file_name = "quiz.txt"

def check_if_file_exists():
    if os.path.exists(file_name):
        print("Quiz file exists")
    else:
        print("Quiz file does not exist. Please make one")

def quiz_reader():
    questions = []
    with open(file_name, "r") as file:
        lines = file.readlines()
        
        i = 0

    while i < len(lines):
        line = lines[i]
        if line.startswith("Question: "):
            question = line[len("Question: "):]
            options = options_reader(lines, i)
            correct_answer = correct_answer_reader(lines, i + len(options)+ 1)
            questions.append((question, options, correct_answer))
            i += len(options) + 1
        else:
            i += 1
        return questions

def options_reader(lines, start_index):
    options = {}
    for option_letter in ['a', 'b', 'c', 'd']:
        start_index += 1
        option_line = lines[start_index]
        start = f"Option {option_letter}: "
        if option_line.startswith(start):
            options[option_letter] = option_line[len(start):]
        else:
            options[option_letter] = ""
    return options

def correct_answer_reader(lines, index):
    correct_line = lines[index]
    if correct_line.startswith("Correct Answer:"):
        return correct_line[len("Correct Answer:"):].strip().lower()

def question_displayer(questions):
    for question, options, correct_answer in questions:
        print(question)
        for option_letter, option_text in options.items():
            print(f"{option_letter}: {option_text}")
        user_answer = input("please enter your answer:").strip().lower()
        if user_answer == correct_answer:
            print("correct")
        else:
            print(f"wrong the answer was {correct_answer}")

quiz = quiz_reader()
if quiz:
    question_displayer(quiz)
else:
    print("No questions to display.")