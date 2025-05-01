import os
import random

file_name = "quiz.txt"

def check_if_file_exists():
    if os.path.exists(file_name):
        print("Quiz file exists")
    else:
        print("Quiz file does not exist. Please make one")

def question_reader():
    questions = []
    with open(file_name, "r") as file:
        lines = file.readlines()

    lines_iter = iter(lines)
    while True:
            line = next(lines_iter).strip()
            if line.startswith("Question"):
                question = line[len("question:")]


question_reader