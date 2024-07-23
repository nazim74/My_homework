def print_params(a=1, b='One', c=True):
    print(a, b, c)

values_list = [2, 'Two', False]
values_list_2 = [3, 'Three']
values_dict = {'a': 4, 'b': 'Four', 'c': False}

print_params()
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
print_params(b=25)
print_params(c=[1,2,3])
