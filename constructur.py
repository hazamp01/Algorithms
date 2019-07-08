class employee:
    def __init__(self, age, id, name):
        self.age = age
        self.id = id
        self.name = name


# Create the object of student class
s = employee('23', '124', 'Mohan')
print getattr(s, 'name')
setattr(s, 'age', '24')
print getattr(s, 'age')
print hasattr(s, 'age')
delattr(s, 'age')
print s.__doc__
print s.__dict__
print s.__module__


# Another example class instance to setting the other values using the default

class computer:
    def __init__(self):
        self.max_price = 1000

    def sell(self):
        print ("Selling price is {} ".format(self.max_price))

    def set_max_price(self, price):
        self.max_price = price


c = computer()
c.sell()
# Attached price variable to the max_price allows you to change the actual value
c.set_max_price(1009)
c.sell()


# Polymorphism

class Parrot:
    def fly(self):
        print "Parrot can fly"

    def swim(self):
        print "Parot can't swim"


class penguin:
    def fly(self):
        print "Penguin can't fly"

    def swim(self):
        print "Penguin can swim"


def flying_test(bird):
    bird.fly()


def flying_test_1(bird):
    bird.swim()


blue = Parrot()
piggy = penguin()

flying_test(blue)
flying_test_1(piggy)
