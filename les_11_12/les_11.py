"""
прочитать файл
превратить строчки в екземпляры класов
проверки
сохранить в json  файл
"""
import json
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
        object_list = s.split(", ")
        return {tmp_list[0]: tmp_list[1] for el in object_list for tmp_list in [el.split(" = ")]}  # list comprehension

    def parse(self) -> List[dict]:
        data = self.reader.read()
        car_list = data.split("\n")
        return [self._parse_string(el) for el in car_list]   # list comprehension


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

    def to_json(self):
        return {"color": self.color,
                "weight": self.weight,
                "transmission": self.transmission,
                "engine": self.engine
                }


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


car_made = {
    "BMW": BMW,
    "Seat": Seat,
    "Audi": Audi,
    "Chevrolet": Chevrolet,
    "Jaguar": Jaguar,
    "Opel": Opel
}


def serealize(car_list: List[dict]) -> List[Union[BMW, Seat, Audi, Chevrolet, Jaguar, Opel]]:
    return [car_made[el["car"]](color=el["color"],
                                weight=el["weight"],
                                transmission=el["transmission"],
                                engine=el["engine"]) for el in car_list]   # list comprehension
# В выражении List Comprehension сначала указывается то, что должно произойти с каждым элементом,
# а затем идет цикл, который перебирает элементы из итерируемого объекта.



class Writer:
    def __init__(self, name: str):
        self.name = name

    def write(self, obj_list: List[Union[BMW, Seat, Audi, Chevrolet, Jaguar, Opel]]):
        with open(self.name, "w") as f:
            for el in obj_list:
                data = json.dumps(el.to_json())
                f.writelines(data)
                f.writelines("\n")


def main():
    reader = Reader("file.txt")
    parser = Parser(reader)
    car_list = parser.parse()
    obj_list = serealize(car_list)
    print(obj_list)
    writer = Writer("file.json")
    writer.write(obj_list)


if __name__ == "__main__":
    main()
