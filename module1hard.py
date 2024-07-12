grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#находим среднее арифметическое в каждом блоке списка
grades_block_1 = sum(grades[0]) / len(grades[0])
grades_block_2 = sum(grades[1]) / len(grades[1])
grades_block_3 = sum(grades[2]) / len(grades[2])
grades_block_4 = sum(grades[3]) / len(grades[3])
grades_block_5 = sum(grades[4]) / len(grades[4])
#создаем список средних значение
grades_midl = grades_block_1, grades_block_2, grades_block_3, grades_block_4, grades_block_5
#print(grades_midl)
#переводим множество в список
students_list = list(students)
#print(students_list)
#форматируем список по алфавиту
students_list_sort = sorted(students_list)
#print(students_list_sort)
#создаем новый словарь
new_student_list = dict(zip(students_list_sort, grades_midl))
print(new_student_list)
