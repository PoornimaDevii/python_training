# Object oriented programming in python

# Self becomes the placeholder
# To make the data private, write name as __name
class Student:

    total = 0
    def __init__(self,n,a):
        self.__name = n
        self.__age = a

        self.__class__.total += 1
        self.__roll = self.__class__.total
        try:
            if a < 0:
                raise Exception(a,n)
            else:
                self.__age = a
        except Exception as inst:
            print("Negative age", inst.args)
            self.__age = 0


    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def get_roll(self):
        return self.__roll

    def inc_age(self,n):
        self.__age += n

    def __repr__(self):
        return "An object of class student"

    def __gt__(self,other): # example of operator overloading (>)
        if type(other) is Student:
            return self.__age > other.get_age()



