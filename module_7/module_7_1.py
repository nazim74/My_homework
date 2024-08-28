from pprint import pprint


class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        # Создаем файл, если его не существует
        file = open(self.__file_name, 'a')
        file.close()

    def get_products(self):
        # Открываем файл для чтения
        file_info = open(self.__file_name, 'r', encoding='utf-8')
        content_file = file_info.read()  # читаем файл
        file_info.close()
        return content_file  # возвращаем содержимое

    def add(self, *products):
        # Получаем текущее содержимое файла products.txt
        existing_products = self.get_products().splitlines()
        existing_entries = []  # Список для продуктов которые уже есть

        for line in existing_products:  # смотрим пустые строки
            if line:
                existing_entries.append(line)

        # добавляем записи
        file = open(self.__file_name, 'a', encoding='utf-8')
        for product in products:
            product_for_add = str(product)  #
            if product_for_add not in existing_entries:  # смотрим нет ли такого продукта
                file.write(product_for_add + '\n')  # если нет, добавляем в конец с новой строки
            else:
                print(f'Продукт {product} уже есть в магазине')
        file.close()


if __name__ == "__main__":
    s1 = Shop()

    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)

    s1.add(p1, p2, p3)

    print(s1.get_products())
