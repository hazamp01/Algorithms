# list comperhension
x = [i * i for i in (1, 2, 3, 4, 5, 6)]
print x

# Example to achieve more using list comperhension
v = [1, -3, 5]
a = (1, 2, 34, 5)
print "list-----"
print dir(v)
print "Tuple----"
print dir(a)
print 4 * v
# what actually do is it concatenate the lists
result = [1, -3, 5, 1, -3, 5, 1, -3, 5, 1, -3, 5]
# we can achieve this using list comperhension
re = [4 * i for i in v]
print re
