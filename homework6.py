my_dict = {'Nazim': 1974, 'Maxim': 1980, 'Alex': 2001}
print('Dict:', my_dict)
print('Existing value: ', my_dict['Nazim'])
print('Not existing value: ', my_dict.get('Boris'))
my_dict['Rick'] = 1967
my_dict['Morty'] = 2011
deleted_value = my_dict['Nazim']
del my_dict['Nazim']
print('Deleted value: ', deleted_value)
print(my_dict)

my_set = {'one', 2, 3, False, 'one', 2, 3, True, False}
print('Set: ', my_set)
my_set.add('new')
my_set.add(777)
my_set.remove(False)
list_ = [2, 3, 2, 2]
print('Modified set: ', my_set)
#list_ = [2, 3, 2, 2] не разобрался
#print(my_set(list_))