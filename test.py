#
# age_ = input()
# age = int(age_)
# if age < 4:
#     print("Your admission cost is $0.")
# elif age < 18:
#     print("Your admission cost is $25.")
# else:
#     print("Your admission cost is $40.")

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# active = True
# while active:
#     message = input(prompt)
#     if message == 'stop':
#         break #active = False
#     else: print(message)
#
# current_number = 0
# while current_number < 100:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     if current_number == 33:
#         print('ops')
#         #globals()
#     #         break #active = False
#     print(current_number)

responses = {}
  # Установка флага продолжения опроса.
polling_active = True
while polling_active:
      # Запрос имени и ответа пользователя.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
# Ответ сохраняется в словаре: ❷ responses[name] = response
# Проверка продолжения опроса.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
  # Опрос завершен, вывести результаты.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")


print(repeat)
#test