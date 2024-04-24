from random import randint


NUMBER_FROM_WHICH_RANDINT_STARTS = 0
NUMBER_WITH_WHICH_RANDINT_ENDS = 1000


def generate_question():
    random_input = randint(NUMBER_FROM_WHICH_RANDINT_STARTS, NUMBER_WITH_WHICH_RANDINT_ENDS)
    correct_answer = 'yes' if random_input % 2 == 0 else 'no'
    return (random_input, correct_answer)