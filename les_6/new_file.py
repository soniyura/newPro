from typing import List, Tuple, Union


def _input_list(massage: str) -> List[int]:
    list_str = input(massage).split()
    list_int = [int(item) for item in list_str]
    return list_int

def input_data() -> List[List[int]]:
    return  [_input_list("Enter list  of int type: "),
             _input_list("Enter list  of int type: "),
             _input_list("Enter list  of int type: ")]


def _case1(raw_data: List[List[int]]) -> bool:
    for l in raw_data:
        if not l:
            return False
    return True

def _case2(raw_data: List[List[int]]) -> bool:
    if len(raw_data[0]) != len(raw_data[1]) != len(raw_data[2]):
        return False
    return True

def _case3(raw_data: List[List[int]]) -> bool:
    for el in raw_data[0]:
        if el == 0:
            return False
    return True

def validate_input(raw_data: List[List[int]]) -> bool:
    """
    case 1: empty list
    case 2: same length of all lists
    case 3: a != 0
    :param raw_data:
    :return:
    """
    return _case1(raw_data) and _case2(raw_data) and _case3(raw_data)


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