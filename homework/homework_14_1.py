# Створення власного виключення для задачі 13_1

class StudentException(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def get_exception_message(self):
        return self.message


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.gender}, {self.first_name} {self.last_name}, {self.age} y.o."


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __eq__(self, other):
        if isinstance(other, Student):
            return str(self) == str(other)
        return True

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        return f"{self.gender}, {self.first_name} {self.last_name}, {self.age} y.o. {self.record_book}"


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)
        if len(self.group) >= 10:
            raise StudentException('Too many students!')

    def delete_student(self, last_name):
        self.group.discard(last_name)

    def find_student(self, last_name):
        for student in self.group:
            if last_name == student.last_name:
                return student

        return None

    def __str__(self):
        all_students = f"Students: "
        for students in self.group:
            all_students += str(students)
        return f'Number: {self.number}\n{all_students}\n '


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
# print(st1)
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 31, 'Javier', 'Esquela', 'AN145')
st4 = Student('Male', 40, 'Dutch', 'Linde', 'AN145')
st5 = Student('Female', 26, 'Marry', 'Beth', 'AN145')
st6 = Student('Male', 29, 'Sean', 'ONeal', 'AN145')
st7 = Student('Male', 31, 'John', 'Marston', 'AN145')
st8 = Student('Female', 27, 'Abigail', 'Porter', 'AN145')
st9 = Student('Male', 33, 'Arthur', 'Morgan', 'AN145')
st10 = Student('Female', 28, 'Margareth', 'Tetch', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
# print(gr)
print(str(gr.find_student('Jobs')))
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
# print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!
