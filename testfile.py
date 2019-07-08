# File read
# take out the words from that file
# find unique words
# find the words which are duplicated
# create a dic with sorted order key should be the word and value shoud be the list or tupe
# how many times key was repeated

import json

file = "/Users/mohanpraveenhazaru/Documents/alg/test.txt"
read = open(file, "r")
count = {}
i = 1
for s in read:
    s = s.strip()
    if s in count:
        count[s]['cnt'] = count[s]['cnt'] + 1
        count[s]['indexes'].append(i)
    else:
        dc = {"cnt": 1, "indexes": [i]}
        count[s] = dc
    i = i + 1

print (json.dumps(count, sort_keys=True))
