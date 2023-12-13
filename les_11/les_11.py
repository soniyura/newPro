"""
прочитать файл
превратить строчки в екземпляры класов
проверки
сохранить в json  файл
"""

class Reader:

    def __init__(self, name: str):
        self.name = name


    def read(self) -> str:
        with open(self.name, "r") as f:
            return f.read()









def main():
    reader = Reader("file.txt")
    print(reader.read())




if __name__ == '__main__':
    main()