#!/usr/bin/env python3


def get_user_name():
    return input("May I have your name? ")


def greet_user(user_name):
    print(f"Hello, {user_name}!")


def ask_question(QUESTION, random_input):
    print(QUESTION)
    print(f"Question: {random_input}")


def get_answer():
    return input("Your answer: ")


def inform_wrong_answer(answer, correct_answer, user_name):
    print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}")
    print(f"Let's try again, {user_name}!")


def inform_right_answer(answer, correct_answer, user_name):
    print("Correct!")


def inform_about_win(user_name):
    print(f"Congratulations, {user_name}!")


def run_the_game(ATTEMPTS_NUMBER, QUESTION, generate_question):
    user_is_correct = True

    attempts = ATTEMPTS_NUMBER

    user_name = get_user_name()

    greet_user(user_name)

    while user_is_correct and attempts > 0:

        random_input, correct_answer = generate_question()

        ask_question(QUESTION, random_input)
        answer = get_answer()

        if answer != correct_answer:
            user_is_correct = False

        if not user_is_correct:
            inform_wrong_answer(answer, correct_answer, user_name)
        else:
            inform_right_answer(answer, correct_answer, user_name)
            attempts -= 1

        if attempts == 0:
            inform_about_win(user_name)