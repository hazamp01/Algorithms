
#
# # name,qty
# apple,10
# bat,1
# cat,20
# cat,20
# apple,5
#
# #name,ctn,sum,indexes
# apple,2,15,1,5


import pandas
file = '/Users/mohanpraveenhazaru/Desktop/test.csv'
df = pandas.read_csv('test.csv',
            index_col='Employee',
            parse_dates=['Hired'],
            header=0,
            names=['Employee', 'Hired', 'Salary', 'Sick Days'])
df.to_csv('hrdata_modified.csv')