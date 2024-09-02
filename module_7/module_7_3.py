import string
from pprint import pprint


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read()
                text = text.lower()  # Приведение текста к нижнему регистру
                # Удаляем пунктуацию
                deleted_punctuation = str.maketrans('', '', string.punctuation.replace("'", ''))

                # string.punctuation: строка, содержащая все символы пунктуации в Python:
                # !"#$%&'()*+,-./:;<=>?@[\]^_{|}~`.
                # Метод str.maketrans создает таблицу перевода символов,
                # где первый аргумент указывает на заменяемые символы,
                # второй аргумент указывает на заменяющие символы,
                # третий аргумент указывает на символы для удаления.

                cleaned_text = text.translate(deleted_punctuation)
                words = cleaned_text.split()  # Разбиваем текст на слова
                all_words[file_name] = words
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        result = {}
        word = word.lower()

        for file_name, words in all_words.items():  # перебираем сразу пару ключ - значение
            position = words.index(word) + 1  # Позиция не с нуля
            result[file_name] = position
            continue
        return result

    def count(self, word):
        all_words = self.get_all_words()
        result = {}
        word = word.lower()

        for file_name, words in all_words.items():  # перебираем сразу пару ключ - значение
            count = words.count(word)
            if count > 0:
                result[file_name] = count

        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
