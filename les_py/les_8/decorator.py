from typing import List

def looger(func):
    return func

def summator(num_list: List) -> int:
    return sum(num_list)

summator = looger(summator)

@looger
def main():
    my_list = [1, 2, 3, 4, 5]
    print(summator.__name__)
    result = summator(my_list)
    print(result)



if __name__ == '__main__':
    main()