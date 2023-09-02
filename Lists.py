#dont have to be the same datatypes
#can make a list within the elements of the list

a = [4, True, "hi"]
y = a #y becomes a reference of list a
y = a[:] #y becomes a copy of a 
a[0] = "heyyy"
print (a)
print(len(a)) #print lenght of the list