my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
initial_value = 0
print("my_list =", my_list)
while len(my_list) > initial_value: #проверяем что количество значений в списке больше чем 0,1,2 и до 13. Как только len(my_list) станет равен  initial_value цикл остановиться
    number_of_my_list = my_list[initial_value] #создаем переменную равную конкретному  значению в списке, первое значение (42)
    if number_of_my_list < 0: #проверяем что значение отрицательное
        break
    if number_of_my_list > 0: #проверяем что значение положительное
        print(number_of_my_list)
    initial_value = initial_value + 1 #берем сделующее значение из списка

