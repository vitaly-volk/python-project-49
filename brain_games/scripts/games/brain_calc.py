#!/usr/bin/env python3


from random import randint, choice
from ..brain_interface import run_the_game


ATTEMPTS_NUMBER = 3
QUESTION = "What is the result of the expression?"


def generate_question():
    random_sign = choice(["+","-","*"])
    random_number1 = randint(0,100)
    random_number2 = randint(0,100)
    random_input = f"{random_number1}{random_sign}{random_number2}"
    if random_sign == "+":
        correct_answer = str(random_number1+random_number2)
    elif random_sign == "-":
        correct_answer = str(random_number1-random_number2)
    else:
        correct_answer = str(random_number1*random_number2)
    return (random_input, correct_answer)

def main():
    run_the_game(ATTEMPTS_NUMBER, QUESTION, generate_question)


if __name__ == '__main__':
    main()
