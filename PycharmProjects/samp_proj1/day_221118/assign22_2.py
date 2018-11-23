#To define a class, and convert the object into a dictionary.

class Student:
    def __init__(self,n,a,r):
        self.__name = n
        self.__age =a
        self.__roll = r


    def get_age(self):
        return self.__age

    def get_roll(self):
        return self.__roll

    def get_name(self):
        return self.__name

stu1 = Student('reena',23,334423)
print(dir(stu1))
#print(stu1.name)
print(stu1.get_age())
print(stu1.get_roll())
new_d = {}
keys = []
values = []

print(stu1.__dict__) # will give variables in init
a = stu1.__dict__
print(a.keys())
print(a.values())
for k,v in a.items():
    print(k)
    print(v)
    if '_Student' in k:
        b = k.split('_Student__')
        #lprint("This is n:",n)
        new_d[b[1]] = v

print(new_d)






