"""
Sum of list
input 1 2 3 4
output 10
"""

from typing import List

def get_user_input() -> List[str]:
    """
    :return: list of string from terminal
    """
    # input_string = input("Input list of number divided by spase: ")
    # result_list = input_string.split(" ")
    # return result_list
    input_string = input("Input list of number divided by spase: ")
    return input_string.split(" ")
#    or  return input("Input list of number divided by spase: ").split(" ")

def validate_list(raw_list: List[str]) -> List[int]:
    """
    Case 1 - letter instead number
    :param raw_list: list of string from terminal
    :return: valid list of int
    """
    try:
        result_list = [int(el) for el in raw_list]
        # result_list = []
        # for el in raw_list:
        #     result_list.append(int(el))
        return result_list
    except ValueError as err:
        print(err)
        raise TypeError("=======Letters instead numbers=======")

def get_sum_list(my_list: List[int]) -> int:
    """
    :param my_list: valid list of int
    :return: sum of list
    """
    result = 0
    for el in my_list:
        result += el
    return result


def main():
    user_input = get_user_input()
    valid_list = validate_list(user_input)
    result = get_sum_list(valid_list)
    print(result)


if __name__ == '__main__':
    main()