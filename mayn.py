
#
# def greet_user(usrename = input('твое имя? ')):  # функция где username - переменная
#     print(f"Hello!, {usrename.title()}!")
# greet_user() # вызов функцииб можно записать так, greet_user(input('name')), но тогда убрать это из def

# def favorite_book(title = 'One of my favorite books is Alice in Wonderland'):
#     print(title)
# favorite_book()
# def describe_pet(animal_type, pet_name): # (animal_type = input('tape: '), pet_name = input('pets name: ' )):
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet('hamster', 'harry')
# describe_pet('ham', 'har')

# def make_shirt(size_, print_):
#     print(f"\nразмер футболки {size_}.")
#     print(f"\nкартинка на футболке {print_}.")
# make_shirt('XL', 'Python')

# def get_formatted_name(first_name = input('name: '), last_name = input('last name: ')):
#     full_name = (f"{first_name} 777 {last_name}")
#     return full_name.title()
# musician = get_formatted_name()#('jimi', 'hendrix')
# print(f"Hello!, {musician.title()}!")#('Привет, ' + musician)
def get_formatted_name(first_name = input('name: '), middle_name = input('middle name:'), last_name = input('last name: ')):
    if middle_name:
        full_name = (f"{first_name} {middle_name} {last_name}")
    else:
        full_name = (f"{first_name} {last_name}")#return full_name.title()
    return full_name.title()
print(get_formatted_name())#('jimi', 'hendrix')
#print(f"Hello!, {musician.title()}!")#('Привет, ' + musician)
