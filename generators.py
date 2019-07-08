# # without generator
# def square_num(nums):
#     result = []
#     for num in nums:
#         result.append(num * num)
#     return result
#
#
# mynums = square_num([1, 2, 3, 4, 5])
# print mynums
#
#
# # with yield generator
#
# def sqr_num(nums):
#     for num in nums:
#         yield num * num
#
#
# num = sqr_num([1, 2, 3, 4, 5, 6])
# for i in num:
#     print i
# def rev_str(my_str):
#     length = len(my_str)
#     for i in range(length-1,-1,-1):
#         yield my_str[i]
#
# # For loop to reverse the string
# # Output:
# # o
# # l
# # l
# # e
# # h
# for char in rev_str("hello"):
#      print(char)
#
# daily_balances = [107.92, 108.67, 109.86, 110.15]
# # print "slice starting"+str(i) + 'days ago : '+
# b = daily_balances[1:3]
# c=daily_balances[2:4]
# print "slice starting for 3 days: "+ str(b)
# print "slice starting for 2 days: "+ str(c)

def add(x,y):
    return x+y

a=add(1,2)

print a
