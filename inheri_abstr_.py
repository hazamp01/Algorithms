# Implementing basic abstract calsses

import random
from abc import abstractmethod


class calculator():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        super(calculator, self).__init__()

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def sub(self):
        pass

    @abstractmethod
    def mult(self):
        pass

    @abstractmethod
    def div(self):
        pass

    @staticmethod
    def random_number(a):
        return random.randint(a)


class usage(calculator):

    @abstractmethod
    def add(self):
        return self.a + self.b

    @abstractmethod
    def sub(self):
        return self.a - self.b

    @abstractmethod
    def mul(self):
        return self.a * self.b

    @abstractmethod
    def div(self):
        return self.a / self.b


u = usage(1, 2)
print u.add()
print u.mult()
print u.div()
print u.sub()


##########################################
# Basic inheritance classes by printing employee details

class Person():
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def full_name(self):
        return self.first + " , " + self.last


class Employee(Person):
    def __init__(self, first, last, staffid):
        Person.__init__(self, first, last)
        self.staffid = staffid

    def employye_details(self):
        return self.first + " , " + self.last + " , " + self.staffid

# Class initialisation
p = Person('Mohanpraveen', 'Hazaru')
e = Employee('Gopaluni', 'sukhesh', '2002')

print p.full_name()
print e.employye_details()
