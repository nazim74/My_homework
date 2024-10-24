import logging
import unittest

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(asctime)s | %(levelname)s | %(message)s | Строка: %(lineno)d | Как по фиксить: %(fix)s',
)


class Runner:
    def __init__(self, name, speed=5):
        try:
            if isinstance(name, str):
                self.name = name
            else:
                raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')

            self.distance = 0

            if speed > 0:
                self.speed = speed
            else:
                raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')
        except Exception as e:
            logging.error(f'Ошибка при создании Runner: {e}', extra={
            'fix': 'юзаем только буквы'
        })
            raise

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
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

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers


# Тесты
class RunnerTest(unittest.TestCase):

    def test_walk(self):
        # отрицательная скорость
        try:
            runner = Runner("Вася", speed=-10)
            for _ in range(10):
                runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f"Ошибка в тесте test_walk: {e}", extra={
            'fix': 'скорость только положительная'
        })

    def test_run(self):
        # ошибка имени int  вместо  str
        try:
            runner = Runner(12345, speed=5)
            for _ in range(10):
                runner.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f"Ошибка в тесте test_run: {e}", extra={
            'fix': 'предложения по исправлению'
        })

    def test_name_correction(self):
        # ошибка в имени Вося
        try:
            runner = Runner("Вося", speed=5)
            correct_name = "Вася"  # Ожидаемое имя
            self.assertEqual(runner.name, correct_name, f"Имя должно быть '{correct_name}', а не '{runner.name}'")
            logging.info('"test_name_correction" выполнен успешно')
        except AssertionError as e:
            logging.warning(f"Ошибка в test_name_correction: {e}", extra={
            'fix': 'учить русский язык...)'
        })
            raise

    def test_challenge(self):
        # корректный тест
        try:
            runner1 = Runner("Илья")
            runner2 = Runner("Арсен")
            for _ in range(10):
                runner1.run()
                runner2.walk()
            self.assertNotEqual(runner1.distance, runner2.distance)
            logging.info('"test_challenge" выполнен успешно')
        except Exception as e:
            logging.warning(f"Ошибка в тесте test_challenge: {e}")

if __name__ == "__main__":

    unittest.main()




