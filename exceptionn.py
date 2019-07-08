result =None
a=float(input("Enter first number you want to calculate :"))
b=float(input("Enter second number you want to calculate: "))

try:
    c=a/b
    print "result is ",c
except ZeroDivisionError as e:
    print "ZeroDivisionError is : ",type(e)
except TypeError as e:
    print "Type Error is :",type(e)
else:
    print "__omg else__"
finally:
    print "__Thank god it was printed"
print ("END")

class cofee_cup():
    def __init__(self,temparature):
        self.__temparature=temparature
    def drink_cofee(self):
        if self.__temparature>85:
            raise Exception ("Some random message")
        elif self.__temparature<100:
            raise ValueError ("Some random message")
        else:
            print "cofee ok to drink"


Creating own exception class using the Exception instead of using value error or Exception as errors
class cofee_hot(Exception):
    def __init__(self,msg):
        super().__init__(msg)
class cofee_cold(Exception):
    def __init_(self,msg):
        super().__init__(msg)

class cofee_cup():
    def __init__(self,temparature):
        self.__temparature=temparature
    def drink_cofee(self):
        if self.__temparature>85:
            raise cofee_cold ("Some random message")
        elif self.__temparature<100:
            raise cofee_hot ("Some random message")
        else:
            print "cofee ok to drink"