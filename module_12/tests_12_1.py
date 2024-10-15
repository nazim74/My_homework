import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


# Тестовый класс
class RunnerTest(unittest.TestCase):

    # Тестируем метод walk
    def test_walk(self):
        runner = Runner("Walker")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)  # Проверяем, что пройденная дистанция равна 50

    # Тестируем метод run
    def test_run(self):
        runner = Runner("Runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)  # Проверяем, что пройденная дистанция равна 100

    # Тестируем оба объекта с разными методами
    def test_challenge(self):
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")

        for _ in range(10):
            runner1.run()  # У первого объекта вызывается метод run
            runner2.walk()  # У второго объекта вызывается метод walk

        self.assertNotEqual(runner1.distance, runner2.distance)  # Проверяем, что дистанции разные


# Запуск тестов
if __name__ == '__main__':
    unittest.main()
