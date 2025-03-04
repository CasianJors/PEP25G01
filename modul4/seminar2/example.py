# dict

leguma_pret ={                      # dict(key:value, key2:value2)
    'cartof' : '5 lei',
    'morcov' : '10 lei',
    'ceapa': "3 lei"
}


for key, value in leguma_pret.items():
    print(f' pretul legumei {key} este {value}')


my_dict1 = {'example': True}

my_dict2 = dict(test=123)
# update
print(my_dict1)
my_dict1.update({'example2': False})
print(my_dict1)
my_dict1.update(example=None)
print(my_dict1)
my_dict1['example2'] = (False, False)
print(my_dict1)



# get

print(my_dict1.get('example2'))

print(my_dict1)
print(my_dict1.get('example3', "No Value found"))

print(my_dict1['example2'])
# print(my_dict1['example3']) # KeyError: 'example3'

# pop

print(my_dict1)
print(my_dict1.pop('example2'))
print(my_dict1)
# del

del my_dict1['example']
print(my_dict1)

# iter

my_dict2.update({1: 1, 2: 2, 3: 3})
print(my_dict2)

for element in my_dict2:
    print('Element is key: ', element)

for element in my_dict2.keys():
    print('Element is key: ', element)

for element in my_dict2.values():
    print('Element is value: ', element)

for element in my_dict2.items():
    print('Element is item: ', element)

for key, value in my_dict2.items():
    print('Element key is: ', key, 'Element value is: ', value)

# set

my_set1 = set()  # empty set
my_set2 = {1, 3, 5, 5}
print(my_set1)
print(my_set2)
print(type(my_set1))

# operations with sets

my_set1.update([4, 5])
print(my_set1)
my_set1.update((9,))
print(my_set1)

print(my_set1.intersection(my_set2))
print(my_set1.difference(my_set2))
print(my_set1.symmetric_difference(my_set2))
print(my_set1.intersection_update(my_set2))
print(my_set1)
