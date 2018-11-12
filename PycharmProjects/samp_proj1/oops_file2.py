
from copy import deepcopy # generally in stu3 = stu1, a shallow copy of stu3 is only created, that's y we use this <-
from oop_file import Student

stu1 = Student("Sathya",22)
stu2 = Student("Manasa",23)
stu3 = deepcopy(stu1)

print(stu1.get_name() + "'s age is", stu1.get_age()) # print(stu1.__name + "'s age is", stu1.__age)
print(stu1.get_name() + 's roll number is', stu1.get_roll())

print(stu2.get_name() + "'s age is", stu2.get_age())
print(stu2.get_name() + 's roll number is', stu2.get_roll())

stu1.inc_age(3)
print(stu1.get_name() + "'s age is", stu1.get_age())
print(stu2.get_name() + "'s age is", stu2.get_age())

print(stu3.get_name() + "'s age is", stu3.get_age())
print(stu3.get_name() + 's roll number is', stu3.get_roll())


print(stu1) # O/P from repr method
print(stu1 > stu2)
print(stu1 < stu2)

import pickle # pickling is similar to serialization in java
f = open('student.bin','wb')
pickle.dump(stu1,f)
f.close()

f = open('student.bin','rb')
stu5 = pickle.load(f)
print(stu5.get_name()+ "'s age is", stu5.get_age())
