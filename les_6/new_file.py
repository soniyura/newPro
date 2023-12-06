from typing import List, Tuple, Union


def input_data() -> List[List[int]]:
    list_a_str = input("Enter list  of int type: ").split()
    list_a_int = [int(item) for item in list_a_str]
    list_b_str = input("Enter list  of int type: ").split()
    list_b_int = [int(item) for item in list_b_str]
    list_c_str = input("Enter list  of int type: ").split()
    list_c_int = [int(item) for item in list_c_str]
    List_a_b_c_int = [list_a_int, list_b_int, list_c_int]
    return List_a_b_c_int


def validate_input(raw_data: List[List[int]]) -> bool:
    """
    case 1: empty list
    case 2: same length of all lists
    case 3: a != 0
    :param raw_data:
    :return:
    """
    for l in raw_data:
        if not l:
            return False       # case 1

    if len(raw_data[0]) != len(raw_data[1]) != len(raw_data[2]):
        return False           # case 2

    for el in raw_data[0]:
        if el == 0:
            return False       # case 3

    return True

"""
valid_dta = [
    [1, 2, 3], a
    [2, 3, 4], b
    [-1, -1, -1] c
    ]
    
result = [
    (x1, x2) zero
    (x1, x2) first
    (x1, x2) second
    ]
"""

def calc_quadr_eq(valid_data: List[List[int]]) -> List[Tuple[Union[float, str]]]:
    result_list = []
    for ind, el in enumerate(valid_data[0]):
        a = el
        b = valid_data[1][ind]
        c = valid_data[2][ind]

        dis = b**2 - 4*a*c
        print(dis)

        if dis > 0:
            x1 = (-b + dis**0.5) / (2*a)
            x2 = (-b + dis**0.5) / (2*a)
            result_list.append((x1, x2))
        elif dis == 0:
            x = -b / (a *2)
            result_list.append((x))
        else:
            result_list.append(("No roots"))
    return result_list



def print_roots(list_roots: List[Tuple[Union[float, str]]], input_list: List[List[int]]) -> None:

    for ind, el in enumerate(input_list[0]):
        a = el
        b = input_list[1][ind]
        c = input_list[2][ind]
        result_str = f'For equation {a}x^2 + {b}x + {c} = 0 '  \
                    f'result: {list_roots[ind]}'
        print(result_str)




def main():
    input_list = input_data()
    print(input_list)
    if validate_input(input_list):
        result_list = calc_quadr_eq(input_list)
        print_roots(list_roots=result_list, input_list=input_list)




if __name__ == '__main__':
    main()