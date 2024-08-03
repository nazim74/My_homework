def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])

    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result = get_multiplied_digits(402030)
result_1 = get_multiplied_digits(222)
print(result)
print(result_1)

#endswith
# if str(number).endswith('0'):
#       str_number = str(number//10)
#     else:
#       str_number = str(number)