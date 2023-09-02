# curly brackets
""" data = {1:'Navin',2:'Kiran', 4:'Harsh'}

print(data)
print(data[4])
print(data.get(1))
print(data.get(3)) """

keys = ['Navin','Kiran','Harsh']

values = ['Python', 'Java','JS']

data = dict(zip(keys,values)) # combine the two lists and convert to a dict
data['Monika'] = 'CS'# adding values
del data['Harsh']# deleting 
print(data)