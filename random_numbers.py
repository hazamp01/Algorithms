import random

# print all the directories of random
# print(dir(random))
# for i in range(20):
#     print random.random()
# for i in range(10):
#     print random.normalvariate(1, 10)
# outcomes = ['rock', 'paper', 'sissors']
#
# for i in range(20):
#     print random.choice(outcomes)
#
#
#
#
def rand_int(x, min, max ):
    for i in range(1, x):
        print random.randint(min, max)

rand_int(10, 1, 100)