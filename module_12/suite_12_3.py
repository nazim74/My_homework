import unittest
from tests_12_3 import RunnerTest, TournamentTest  # Импорт тестов

# Создаем TestSuite для объединения всех тестов
def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    # Добавляем тесты через TestLoader
    suite.addTests(loader.loadTestsFromTestCase(RunnerTest))
    suite.addTests(loader.loadTestsFromTestCase(TournamentTest))

    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())

