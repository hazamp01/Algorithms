import collections

array = [2, 3, 5, 3, 7, 9, 5, 3, 7]
Out = [3, 3, 3, 5, 5, 7, 7, 2, 9]

output = {i: array.count(i) for i in array}
for key, value in sorted(output.iteritems(), key=lambda (k, v): (-v, -k)):
    print "%s: %s" % (key, value)

a = []
# Remove duplicates in array
for element in array:
    if element not in a :
        a.append(element)
    else:
        pass
print a
# You are given an array with duplicates. You have to sort the array with decreasing frequency of elements.
# If two elements have the same frequency, sort them by their actual value in increasing order.

# To count the frequeny of repeating elements in list
output={i:array.count(i) for i in array}
cat=output.values()
max=max(cat)
# for element in range(0,len(cat)):
#     if element is max:
print output
# print cat
