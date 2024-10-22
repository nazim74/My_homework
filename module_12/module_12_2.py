import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    """
    исправление заключается в разделении процессов
    итерации списка участников и удаления участников из списка
    в исходном коде получалось, что мы удаляем участников пока итерируем список
    """

    def start(self):
        finishers = {}
        place = 1

        while self.participants:  # Цикл продолжается, пока есть участники
            to_remove = []  # Список участников, будем удалять после цикла
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:  # Если участник достиг финиша
                    finishers[place] = participant
                    place += 1  # Увеличиваем место для следующего бегуна
                    to_remove.append(participant)  # Добавляем участника в список для удаления

            # Удаляем участников, которые финишировали, чтоб они больше не участвовали в забеге
            for participant in to_remove:
                self.participants.remove(participant)

        return finishers  # Возвращаем словарь


class TournamentTest(unittest.TestCase):
    """
    Метод setUpClass - выполняется один раз перед запуском всех тестов
    используем его для хранения общего для всех тестов результата
    """

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):  # Метод - выполняем перед каждым тестом
        # Создаем три объекта класса Runner
        self.usain = Runner("Усэйн", speed=10)
        self.andrey = Runner("Андрей", speed=9)
        self.nick = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):  # Метод - выполняется один раз после всех тестов
        # Вывод результатов всех тестов в консоль
        for result in cls.all_results:  # Для каждого результата из списка all_results
            # Преобразуем результат в словарь
            formatted_result = {place: participant.name for place, participant in result.items()}
            print(formatted_result)

    """ Сами тесты """

    def test_race_usain_nick(self):  # Первый тест: Усэйн VS Ник
        # Создаем турнир
        tournament = Tournament(90, self.usain, self.nick)
        # Запускаем турнир и сохраняем результаты
        results = tournament.start()

        # Сохраняем результаты в общий список результатов - setUpClass
        self.__class__.all_results.append(results)

        # Проверяем, что Ник финишировал последним
        last_place = max(results.keys())  # Получаем номер последнего места
        self.assertTrue(results[last_place].name == "Ник")  # Проверяем, что имя на последнем месте

    def test_race_andrey_nick(self):  # Второй тест: Андрей VS Ник
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        self.__class__.all_results.append(results)

        # Проверяем, что Ник финишировал последним
        last_place = max(results.keys())  # Получаем номер последнего места
        self.assertTrue(results[last_place].name == "Ник")  # Проверяем, что Ник на последнем месте

    def test_race_usain_andrey_nick(self):  # Третий тест: Усэйн VS Андрей VS Ник
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        self.__class__.all_results.append(results)

        # Проверяем, что Ник финишировал последним
        last_place = max(results.keys())  # Получаем номер последнего места
        self.assertTrue(results[last_place].name == "Ник")  # Проверяем, что Ник на последнем месте

    def test_race_usain_andrey(self):  # Четвертый тест: Усэйн VS Андрей
        tournament = Tournament(90, self.usain, self.andrey)
        results = tournament.start()
        self.__class__.all_results.append(results)

        # Проверка, что Усэйн финишировал первым
        first_place = min(results.keys())  # Получаем номер первого места
        self.assertTrue(results[first_place].name == "Усэйн")  # Проверяем, что Усэйн на первом месте

        # Проверка, что Андрей финишировал вторым
        last_place = max(results.keys())  # Получаем номер последнего места
        self.assertTrue(results[last_place].name == "Андрей")  # Проверяем, что Андрей на последнем месте


# Запуск тестов
if __name__ == "__main__":
    unittest.main()  # Запускаем все тесты
