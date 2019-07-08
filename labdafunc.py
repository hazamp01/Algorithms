# Lambda fucntions is like list comperhensions can be used only for writig the codes in single lines
# We can use it as a run time function instead of creating new right away we can use anonymus fucntions
# print square os some values in list
def add_num(a, b):
    return a+b

def greater_num(x,y):
    if x>y:
        return x
    else:
        return y

# If you use lamda functions
# Must have parameters left to the colun and the rigt to colun is return values
print lambda x:2*x

print lambda x,y:x+y

print lambda x,y:x if x>y else y


# Print squares of numbers in the list withput using any map or labda functions
lis=[]
def square_num(a):
    for i in a:
        lis.append(i*i)
    return lis

print square_num([12,3,4,5])

# if you use lambda fucntions
# two fucntions calling here lamda and n map fucntions iterate through the loop of list and assigned to labda to do the functionality
n = [1, 2,3, 45]
print list(map(lambda x:x**2, n))

# Or we can use the function name without using the lambda
print list(map(square_num, n))

# Filter and reduce
#################
# {"a":54,"b":32}
# {"b":32,"a":54"}
# Sorting based on values using lambda based on value
from collections import OrderedDict
a={'a':45,'c':20, 'b':60}
sorted_a = OrderedDict(sorted(a.items() , key=lambda a: a[1]))
print sorted_a

# Sorting based on values using lambda based on key
for key in sorted(a.keys()):
    print key,":", a[key]

# # sorting the dictionary based on values
a={'a':45,'b':20, 'c':60}
res = sorted(a.items(), key=lambda kv:kv[1])
print res
