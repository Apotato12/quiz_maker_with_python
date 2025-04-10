import os

#defines the file name to store the quiz answers and questions
file_name = "quiz.txt"

#defines the function to ask for the question and options
def ask_for_the_question_and_answer():
    #list to store the questions
    list_of_questions = []
    #loop to ask for the question and answers
    while True:
        #asks for the question
        question = input("enter a question:")
        if question in list_of_questions:
            #check if the question is already added on the list
            print("question has already been added")
            continue
        #if the question is not already added add it to the list
        else:
            list_of_questions.append(question)
        #asks for the choices and the correct asnwer
        print ("question has been added")
        answers = {}
        answers['a'] = input("Please enter option a: ")
        answers['b'] = input("Please enter option b: ")
        answers['c'] = input("Please enter option c: ")
        answers['d'] = input("Please enter option d: ")
        correct_answer = input("Please enter the correct answer (a, b, c, or d): ")
        
        #inserts the question and answers into the file
        with open(file_name, "a") as file:
            file.write(f"Question: {question}\n")
            for option, answer in answers.items():
                file.write(f"Option {option}: {answer}\n")
            file.write(f"Correct Answer: {correct_answer}\n")
            file.write("\n")

        #asks if the user wants to add another question
        another_question = input("do you want to add another question? (y to continue and any other letter to exit): ")
        #if the user want presses n the program exits
        if another_question != "y":
            print("exiting the program")
            break
        elif another_question == "y":
            return ask_for_the_question_and_answer()

        return answers, correct_answer


def make_file():
    if not os.path.exists(file_name):
        open (file_name, "w")
    else:
        print("file already exists")

def actual_program():
    make_file()
    ask_for_the_question_and_answer()


actual_program()