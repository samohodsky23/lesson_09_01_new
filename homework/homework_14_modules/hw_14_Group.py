from hw_14_StudentException import StudentException


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)
        if len(self.group) > 10:
            raise StudentException('Too many students!')

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student in self.group:
            self.group.discard(student)

    def find_student(self, last_name):
        for student in self.group:
            if last_name == student.last_name:
                return student

        return None

    def __str__(self):
        all_students = f"Students: \n"
        for students in self.group:
            all_students += str(students)
        return f'Number: {self.number} \n {all_students}\n '
