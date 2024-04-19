#!/usr/bin/env python3


from random import randint
from ..brain_interface import run_the_game


ATTEMPTS_NUMBER = 3
QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def isPrime(number):
    if number == 0:
        return False
    if number == 1:
        return False
    i = 2
    while i*i <= number:
        if number % i == 0:
            return False
        i += 1
    return True


def generate_question():
    random_input = randint(0,100)
    correct_answer = "yes" if isPrime(random_input) == True else "no"
    return (random_input, correct_answer)


def main():
    run_the_game(ATTEMPTS_NUMBER, QUESTION, generate_question)


if __name__ == '__main__':
    main()

