import pickle

items = ['apple','banana','mango']
shoplist_file ='items.data'
f = open(shoplist_file,'rb')
pickle.dump(shoplist_file,f)
f.close()
del shoplist_file
f =open(shoplist_file,'rb')
stored_list = pickle.load(f)
print stored_list
f.close()