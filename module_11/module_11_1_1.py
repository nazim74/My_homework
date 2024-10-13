def introspection_info(obj):
    # Получаем тип объекта
    obj_type = type(obj).__name__

    # Получаем все атрибуты и методы объекта
    attributes_methods = dir(obj)

    # Фильтруем только атрибуты (исключая методы)
    attributes = {attr: getattr(obj, attr) for attr in attributes_methods if not callable(getattr(obj, attr))}

    # Фильтруем только методы (исключая атрибуты)
    methods = {method: getattr(obj, method) for method in attributes_methods if callable(getattr(obj, method))}

    # Определяем модуль, к которому принадлежит объект
    obj_module = getattr(obj, '__module__')

    # Получаем количество атрибутов и методов
    num_attributes = len(attributes)
    num_methods = len(methods)

    # Получаем документацию объекта, если она есть
    obj_doc = getattr(obj, '__doc__')

    print(f"Модуль объекта: {obj_module}\n")
    print(f"Тип объекта: {obj_type}\n")
    print(f"Атрибуты объекта (всего {num_attributes}):")
    for attr_name, attr_value in attributes.items():  # Проходим по каждому атрибуту в словаре
        print(f"  - {attr_name}: {attr_value}")

    print(f"\nМетоды объекта (всего {num_methods}):")
    for method_name in methods:  # Проходим по каждому методу в словаре
        print(f"  - {method_name}")

    print(f"\nДругие интересные свойства объекта:")
    print(f"  - Документация объекта: {obj_doc if obj_doc.strip() else 'Документация отсутствует'}")
    print(f"  - Количество атрибутов: {num_attributes}")
    print(f"  - Количество методов: {num_methods}")


# Пример использования
class MyClass:
    """Это просто класс для демонстрации"""

    def __init__(self, name, age, status):
        self.name = name
        self.age = age
        self.status = status

    def my_method(self):
        return f"Hello, {self.name}!"


# Создаем объект класса
obj = MyClass("Nazim", 50, "вроде как справился с домашним заданием))")

introspection_info(obj)
print(f"\nМеня зовут {obj.name}, мне {obj.age} лет и я {obj.status}")
