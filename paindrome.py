tried = ['mohan','chintan','sanjana','aditi']
print tried
for idx, item in enumerate(tried):
    if 'chintan' in item:
        tried[idx] = 'gokani'
        break

tried.append('praveen')
print tried

for idx, item in enumerate(tried):
    if 'gokani' in item:
        tried[idx] = 'praveen'
        break

print tried