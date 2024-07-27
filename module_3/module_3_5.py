# def get_multiplied_digits(number):
#     str_number = str[number]
#     first = int(str_number)
#     if
#
def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])

    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result = get_multiplied_digits(40203)
result_1 = get_multiplied_digits(222)
print(result)
print(result_1)
