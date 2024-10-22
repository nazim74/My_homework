import unittest
from tests_12_2 import Runner, Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False  # Атрибут для замораживания тестов

    def setUp(self):
        self.runner = Runner("Test Runner")

    def freeze_test(func):  # Декоратор для пропуска тестов
        def wrapper(self, *args, **kwargs):
            if self.is_frozen:
                self.skipTest("Тесты в этом кейсе заморожены")
            else:
                return func(self, *args, **kwargs)

        return wrapper

    @freeze_test
    def test_walk(self):
        for _ in range(10):
            self.runner.walk()
        self.assertEqual(self.runner.distance, 50)

    @freeze_test
    def test_run(self):
        for _ in range(10):
            self.runner.run()
        self.assertEqual(self.runner.distance, 100)

    @freeze_test
    def test_challenge(self):
        runner1 = Runner("Runner 1")
        runner2 = Runner("Runner 2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True  # Атрибут для замораживания тестов

    def setUp(self):
        self.usain = Runner("Усэйн", speed=10)
        self.andrey = Runner("Андрей", speed=9)
        self.nick = Runner("Ник", speed=3)

    def freeze_test(func):  # Декоратор для пропуска тестов
        def wrapper(self, *args, **kwargs):
            if self.is_frozen:
                self.skipTest("Тесты в этом кейсе заморожены")
            else:
                return func(self, *args, **kwargs)

        return wrapper

    @freeze_test
    def test_first_tournament(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        last_place = max(results.keys())
        self.assertTrue(results[last_place].name == "Ник")

    @freeze_test
    def test_second_tournament(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        last_place = max(results.keys())
        self.assertTrue(results[last_place].name == "Ник")

    @freeze_test
    def test_third_tournament(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        last_place = max(results.keys())
        self.assertTrue(results[last_place].name == "Ник")
