


class A:
    def __init__(self, a: str):
        self.a = a


class B(A):
    def __init__(self, a: int):
        super().__init__(a) #пусть выполнится функ инициализации у класа родителя а потом продолжу
        if self.a < 1000:
            raise ValueError



def main():
    a = A(a = 123)
    print(a)

    b = B(a = 234)
    print(b)


if __name__ == '__main__':
    main()