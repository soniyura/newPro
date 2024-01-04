from abc import ABC, abstractmethod

class Enemy(ABC):

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def do_bad_thongs(self):
        pass


class Skileton(Enemy):
    def attack(self):
        print("Skileton hit by sward !!! o_0")

    def move(self):
        print("move it")

    def do_bad_thongs(self):
        print("Python is bad lan")



class Dog:
    def __init__(self, name: str):
        self.name = name
        self.age = 4

    def voice(self):
        print("Гав гав")

    def __str__(self):
        return f"Dog with name = {self.name} and age = {self.age}"


class Puppy(Dog):
    def voice(self):
        print("Тяф тяф")

class Korgi(Dog):
    pass

def main():
    # my_dog = Dog(name="Шарик")
    # my_dog.voice()
    #
    # korgi = Korgi(name="korgi")
    # print(korgi)
    sk = Skileton()
    sk.attack()
    sk.move()
    sk.do_bad_thongs()

if __name__ == '__main__':
    main()