my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
initial_value = 0
print("my_list =", my_list)
while len(my_list) > initial_value:
    number_my_list = my_list[initial_value]
    if number_my_list < 0:
        break
    if number_my_list > 0:
        print(number_my_list)
        initial_value = initial_value + 1
        continue
