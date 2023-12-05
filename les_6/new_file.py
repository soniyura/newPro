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
    pass

def calc_quadr_eq(valid_data: List[List[int]]) -> List[Tuple[Union[str, int]]]:
    pass

def main():
    input_list = input_data()
    print(input_list)


if __name__ == '__main__':
    main()