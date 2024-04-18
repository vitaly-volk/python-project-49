
from random import randint
from ..brain_interface import get_user_name, greet_user, ask_question, get_answer, inform_about_wrong_answer, inform_about_right_answer, inform_about_win

ATTEMPTS_NUMBER = 3

QUESTION = "Find the greatest common divisor of given numbers."

def computeGCD(x, y):
    while(y):
       x, y = y, x % y
    return abs(x)

def generate_question():
    random_number1 = randint(0,100)
    random_number2 = randint(0,100)
    random_input = f"{random_number1} {random_number2}"
    correct_answer = str(computeGCD(random_number1,random_number2))
    return (random_input, correct_answer)

def main():

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


if __name__ == '__main__':
    main()

