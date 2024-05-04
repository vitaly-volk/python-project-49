#!/usr/bin/env python3


ATTEMPTS_NUMBER = 3


def run_game(module):

    user_name = input('May I have your name? ')

    print(f'Hello, {user_name}!')

    for attempts in range(0, ATTEMPTS_NUMBER):

        random_input, correct = module.generate_question()

        print(module.QUESTION)

        print(f'Question: {random_input}')

        answer = input('Your answer: ')

        if answer != correct:
            print(f'{answer} is wrong answer ;(. Correct answer was {correct}')
            print(f'Let\'s try again, {user_name}!')
            return
        else:
            print('Correct!')

    print(f'Congratulations, {user_name}!')
