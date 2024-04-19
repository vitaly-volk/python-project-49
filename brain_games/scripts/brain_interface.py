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

def run_the_game(ATTEMPTS_NUMBER, QUESTION, generate_question):

    user_is_correct = True

    attempts = ATTEMPTS_NUMBER

    user_name = get_user_name()

    greet_user(user_name)

    while user_is_correct != False and attempts>0:

        random_input, correct_answer = generate_question()

        ask_question(QUESTION, random_input)
        given_answer = get_answer()

        if given_answer != correct_answer:
                user_is_correct = False

        if user_is_correct == False:
            inform_about_wrong_answer(given_answer, correct_answer, user_name)
        else:
            inform_about_right_answer(given_answer, correct_answer, user_name)
            attempts-=1

        if attempts == 0:
            inform_about_win(user_name)

