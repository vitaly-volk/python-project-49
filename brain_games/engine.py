#!/usr/bin/env python3


ATTEMPTS_NUMBER = 3


def run_game(module):

    user_is_correct = True

    attempts = ATTEMPTS_NUMBER

    user_name = input('May I have your name? ')

    print(f'Hello, {user_name}!')

    while user_is_correct and attempts > 0:

        random_input, correct_answer = module.generate_question()

        print(module.QUESTION)

        print(f'Question: {random_input}')

        answer = input('Your answer: ')

        if answer != correct_answer:
            user_is_correct = False

        if not user_is_correct:
            print(f'{answer} is wrong answer ;(. Correct answer was {correct_answer}')
            print(f'Let\'s try again, {user_name}!')
        else:
            print('Correct!')
            attempts -= 1

        if attempts == 0:
            print(f'Congratulations, {user_name}!')
