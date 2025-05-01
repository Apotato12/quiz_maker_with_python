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