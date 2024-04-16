def get_user_name():
    return input("May I have your name? ")
    
def greet_user(user_name):
    print(f"hello, {user_name}")

def ask_question(QUESTION, random_input):
    print(QUESTION)
    print(f"Question: {random_input}")

def get_answer():
    return input("Your answer: ")

def inform_about_wrong_answer(given_answer, correct_answer, user_name):
    print(f"{given_answer} is wrong answer ;(. Correct answer was {correct_answer}")
    print(f"Let's try again, {user_name}!")

def inform_about_right_answer(given_answer, correct_answer, user_name):
    print("Correct!")

def inform_about_win(user_name):
    print(f"Congratulations, {user_name}!")

