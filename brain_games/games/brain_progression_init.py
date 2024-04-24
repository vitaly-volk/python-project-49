from random import randint


def generate_question():
    random_number = randint(0, 100)
    progression_length = randint(6, 10)
    progression_step = randint(0, 10)
    missing_point = randint(0, progression_length - 1)
    random_input = ''
    i = 0
    while i < progression_length:
        if i == missing_point:
            random_input += '.. '
        else:
            random_input += str(random_number + (i * progression_step)) + ' '
        i += 1
    correct_answer = str(random_number + (missing_point * progression_step))
    return (random_input, correct_answer)
