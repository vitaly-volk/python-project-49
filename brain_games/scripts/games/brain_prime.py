
from random import randint
from ..brain_interface import get_user_name, greet_user, ask_question, get_answer, inform_about_wrong_answer, inform_about_right_answer, inform_about_win

ATTEMPTS_NUMBER = 3

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def isPrime(number):
    if number == 0:
        return False
    if number == 1:
        return False
    i = 2
    while i*i < number:
        if number % i == 0:
            return False
        i += 1
    return True


def generate_question():
    random_input = randint(0,100)
    correct_answer = "yes" if isPrime(random_input) == True else "no"
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

