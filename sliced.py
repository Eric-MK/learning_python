x = [0,1,2,3,4,5,6,7,8]
y = ['hi','hello', 'goodbye','cya','sure']
s = "hello"

""" sliced = x[start:stop:step]
 """
""" sliced = x[:stop] start at the beginning stop at stop
 """
""" sliced = x[start:] start at start stop at the end
 """
""" sliced = x[::-1] reverse the list
 """
sliced = x[0:6:2]
sliced_s = s[::2]
print(sliced)
print(sliced_s)# can be used on strings also