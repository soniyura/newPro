from typing import Union, List
import csv



class LengthError(Exception):
    pass



class Student:
    def __init__(self):
        self.header = ["id", "login", "password", "email", "avd_mark", "course"]
        self.data = []
        self.file_name = "student.csv"

    def append(self, value: List[str]):
        if len(value) != len(self.header):
            raise LengthError
        self.data.append(value)




class Teacher:
    def __init__(self):
        self.header = ["id", "login", "password", "email", "subject", "category"]
        self.data = []
        self.file_name = "teacher.csv"

    def append(self, value: List[str]):
        if len(value) != len(self.header):
            raise LengthError
        self.data.append(value)



class CswWriter:
    def __init__(self, data_object: Union[Student, Teacher]):
        self.data_object = data_object

    def write(self):
        with open(self.data_object.file_name, 'w', encoding='UTF8') as f:
            writer = csv.writer(f)

            # write the header
            writer.writerow(self.data_object.header)

            # write the data
            writer.writerow(self.data_object.data)


def main():
    student = Student()
    teacher = Teacher()

    #"id", "login", "password", "email", "subject", "category"
    student_data = [[],
                    []]

    teacher_data = [["0", "Ivan", "qwerty", "qwe@gg.com", "3", "python"],
                    ["1", "Alex", "qwerty1", "qwe@gg.com", "40", "python"],
                    ["2", "Anna", "qwerty2", "qwe1@gg.com", "40", "python"],
                    ["3", "Victoria", "qwerty3", "qwe2@gg.com", "40", "python"],
                    ["4", "Denis", "qwerty4", "qwe3@gg.com", "40", "python"],
                    ["5", "Pavel", "qwerty5", "qwe4@gg.com", "40", "python"]
                    ]

   # "id", "login", "password", "email", "avd_mark", "course"
    for el in teacher_data:
        teacher.append(el)

    for el in student_data:
        student.append(el)


if __name__ == "__main__":
    main()
