#!/usr/bin/env python3


from brain_games.engine import run_game
from brain_games.games.brain_even import generate_question


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    run_game(QUESTION, generate_question)


if __name__ == '__main__':
    main()
