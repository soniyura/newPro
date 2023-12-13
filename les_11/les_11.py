"""
прочитать файл
превратить строчки в екземпляры класов
проверки
сохранить в json  файл
"""
from pprint import pprint
from typing import List, Union


class Reader:
    def __init__(self, name: str):
        self.name = name

    def read(self) -> str:
        with open(self.name, "r") as f:
            return f.read()


class Parser:
    def __init__(self, reader: Reader):
        self.reader = reader

    def _parse_string(self, s: str) -> dict:
        dict = {}
        object_list = s.split(", ")
        for el in object_list:
            tmp_list = el.split(" = ")
            dict[tmp_list[0]] = tmp_list[1]
        return dict

    def parse(self) -> List[dict]:
        # cer = BMW, color = Red, weight = 155, transmission = Manual, Engine = 2.0
        result_list = []
        data = self.reader.read()
        car_list = data.split("\n")
        for el in car_list:
            result_list.append(self._parse_string(el))
        return result_list


class Car:
    def __init__(self, color: str, weight: str, transmission: str, engine: str):
        self.color = color
        self.weight = weight
        self.transmission = transmission
        self.engine = engine

    def __repr__(self):
        return (f"color = {self.color} " \
                f"weight = {self.weight} " \
                f"transmission = {self.transmission} " \
                f"engine = {self.engine} ")



class BMW(Car):
    pass


class Seat(Car):
    pass


class Audi(Car):
    pass


class Chevrolet(Car):
    pass


class Jaguar(Car):
    pass


class Opel(Car):
    pass


def serealize(
    car_list: List[dict],
) -> List[Union[BMW, Seat, Audi, Chevrolet, Jaguar, Opel]]:
    obj_list = []
    for el in car_list:
        if el["car"] == "BMW":
            tmp_object = BMW(
                color=el["color"],
                weight=el["weight"],
                transmission=el["transmission"],
                engine=el["engine"],
            )
        elif el["car"] == "Seat":
            tmp_object = Seat(
                color=el["color"],
                weight=el["weight"],
                transmission=el["transmission"],
                engine=el["engine"],
            )
        elif el["car"] == "Audi":
            tmp_object = Audi(
                color=el["color"],
                weight=el["weight"],
                transmission=el["transmission"],
                engine=el["engine"],
            )
        elif el["car"] == "Chevrolet":
            tmp_object = Chevrolet(
                color=el["color"],
                weight=el["weight"],
                transmission=el["transmission"],
                engine=el["engine"],
            )
        elif el["car"] == "Jaguar":
            tmp_object = Jaguar(
                color=el["color"],
                weight=el["weight"],
                transmission=el["transmission"],
                engine=el["engine"],
            )
        elif el["car"] == "Opel":
            tmp_object = Opel(
                color=el["color"],
                weight=el["weight"],
                transmission=el["transmission"],
                engine=el["engine"],
            )
        obj_list.append(tmp_object)
    return obj_list


def main():
    reader = Reader("file.txt")
    parser = Parser(reader)
    car_list = parser.parse()
    obj_list = serealize(car_list)
    print(obj_list)



if __name__ == "__main__":
    main()
