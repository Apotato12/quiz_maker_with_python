import os

# Defines the file name to store the quiz answers and questions
file_name = "quiz.txt"

# Defines the function to ask for the question and options
def ask_for_the_question_and_answer():

    
    # Loop to ask for the question and answers
    while True:
        # Asks for the question
        question = input("Enter a question: ")

        # Asks for the choices and the correct answer
        answers = {}
        answers['a'] = input("Please enter option a: ")
        answers['b'] = input("Please enter option b: ")
        answers['c'] = input("Please enter option c: ")
        answers['d'] = input("Please enter option d: ")
        
        #asks for the correct answer
        correct_answer = input("Please enter the correct answer (a, b, c, or d): ")
        
        # Inserts the question and answers into the file
        with open(file_name, "a") as file:
            file.write(f"Question: {question}\n")
            for option, answer in answers.items():
                file.write(f"Option {option}: {answer}\n")
            file.write(f"Correct Answer: {correct_answer}\n\n")

        # Asks if the user wants to add another question
        another_question = input("Do you want to add another question? (y to continue and any other letter to exit): ")
        
        # If the user presses any letter other than 'y', the program exits
        if another_question.lower() != "y":
            print("Exiting the program.")
            break

# Creates the file if it does not exist
def make_file():
    if not os.path.exists(file_name):
        open(file_name, "w").close()  # Close the file after creating it
    else:
        print("File already exists.")

# Calls the functions that are used for the code
def actual_program():
    make_file()
    ask_for_the_question_and_answer()

actual_program()