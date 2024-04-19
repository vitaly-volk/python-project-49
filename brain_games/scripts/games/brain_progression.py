
from random import randint
from ..brain_interface import get_user_name, greet_user, ask_question, get_answer, inform_about_wrong_answer, inform_about_right_answer, inform_about_win

ATTEMPTS_NUMBER = 3

QUESTION = "What number is missing in the progression?"

def generate_question():
    random_number = randint(0,100)
    progression_length= randint(6,10)
    progression_step = randint(0,10)
    missing_point = randint(0,progression_length-1)
    random_input = ""
    i = 0
    while i < progression_length:
        if i == missing_point:
            random_input += ".. "
        else:
            random_input += str(random_number+ i*progression_step)+" " 
        i += 1
    correct_answer = str(random_number + missing_point*progression_step)
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

