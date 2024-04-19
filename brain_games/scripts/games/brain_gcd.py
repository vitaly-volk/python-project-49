#!/usr/bin/env python3


from random import randint
from ..brain_interface import run_the_game


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
    run_the_game(ATTEMPTS_NUMBER, QUESTION, generate_question)


if __name__ == '__main__':
    main()
