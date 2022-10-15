

def check_if_word_has_4_or_more_letters(word):
    words = len(word) > 3

    return words


def check_what_number_is_greater(first_number, second_number):
    maxNumber = first_number

    if second_number > maxNumber:
        return second_number

    return maxNumber


def check_if_number_is_odd_or_even(number):
    div = number % 2

    if div == 0:
        return 'even'

    return 'odd'


def check_if_element_exists_in_list(element, input_list: list):
    return element in input_list
