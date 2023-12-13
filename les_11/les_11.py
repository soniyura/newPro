"""
прочитать файл
превратить строчки в екземпляры класов
проверки
сохранить в json  файл
"""
from typing import List


class Reader:
    def __init__(self, name: str):
        self.name = name


    def read(self) -> str:
        with open(self.name, "r") as f:
            return f.read()


class Parser:
    def __init__(self, reader: Reader):
        self.reader = reader

    def _parse_string(self, s: str) ->dict:
        dict = {}
        object_list = s.split(", ")
        print(object_list)
        for el in object_list:
            tmp_list = el.split(' = ')
            dict[tmp_list[0]] = tmp_list[1]
        return dict

    def parse(self) -> List[dict]:
        # cer = BMW, color = Red, weight = 155, transmission = Manual, Engine = 2.0
        result_list = []
        data = self.reader.read()
        car_list = data.split("\n")
        print(car_list)
        for el in car_list:
            result_list.append(self._parse_string(el))
        return result_list


def main():
    reader = Reader("file.txt")
    parser = Parser(reader)
    print(parser.parse())



if __name__ == '__main__':
    main()