from hw_14_Human import Human


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
        return f"{self.gender}, {self.first_name} {self.last_name}, {self.age} y.o. {self.record_book} \n"
