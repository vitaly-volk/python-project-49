from random import randint


NUMBER_START_RAND_FROM = 0
NUMBER_END_RAND_WITH = 100
LENGTH_START_RAND_FROM = 6
LENGTH_END_RAND_WITH = 10
STEP_START_RAND_FROM = 1
STEP_END_RAND_WITH = 10
QUESTION = 'What number is missing in the progression?'


def generate_progression(begin, length, step):
    progression = []
    for i in range(0, length):
        progression.append(str(begin + i * step))
    return progression


def generate_question():
    begin = randint(NUMBER_START_RAND_FROM, NUMBER_END_RAND_WITH)
    length = randint(LENGTH_START_RAND_FROM, LENGTH_END_RAND_WITH)
    step = randint(STEP_START_RAND_FROM, STEP_END_RAND_WITH)
    missing_point = randint(0, length - 1)
    progression = generate_progression(begin, length, step)
    progression[missing_point] = '..'
    random_input = ' '.join(progression)
    correct_answer = str(begin + (missing_point * step))
    return (random_input, correct_answer)
