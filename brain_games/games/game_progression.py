from random import randint


PROGRESSION_LENGTH = 9


def rules():
    return 'What number is missing in the progression?'


def get_progression():
    INITIAL_ITEM_RANGE_BOTTOM = 0
    INITIAL_ITEM_RANGE_TOP = 10
    COMMON_DIFFERENCE_RANGE_BOTTOM = 2
    COMMON_DIFFERENCE_RANGE_TOP = 10

    progression = [randint(INITIAL_ITEM_RANGE_BOTTOM, INITIAL_ITEM_RANGE_TOP)]
    common_difference = randint(COMMON_DIFFERENCE_RANGE_BOTTOM,
                                COMMON_DIFFERENCE_RANGE_TOP)

    for element in range(0, PROGRESSION_LENGTH):
        progression.append(progression[element] + common_difference)

    return progression


def progression_to_string(progression):
    str_progression = ' '.join(str(item) for item in progression)
    return str_progression


def game():
    progression = get_progression()
    hidden_index = randint(0, PROGRESSION_LENGTH)
    hidden_number = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = progression_to_string(progression)
    return (question, hidden_number)
