from hw_14_Human import Human
from hw_14_Student import Student
from hw_14_Group import Group
from hw_14_StudentException import StudentException

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 33, 'John', 'Marston', 'AN888')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
# print(gr)
assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None

s
print(gr)  # Only one student
