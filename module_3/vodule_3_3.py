def print_params(a=1, b='Строка', c=True):
    print(a, b, c)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
print_params(3, 2, 3)
print_params(1, values_list_2)
print_params(1, *values_list_2)
print_params(b=25)
