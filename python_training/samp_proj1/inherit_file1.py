from oop_file import Student
from copy import deepcopy

class Cs_student(Student):

    def __init__(self,n,a,s):

        Student.__init__(self,n,a) # call __init__ for student
        self.age=Student.get_age(self)
        self.section_num = s
        print(self.age)

    def get_age(self):
        print("Age:" + str(self.age))


cs_stu1 = Cs_student('poornima',24,22)
cs_stu2 = Cs_student('rang',22,653)
cs_stu3 = deepcopy(cs_stu1)

print(cs_stu1.get_age())