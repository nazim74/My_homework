import asyncio
import time


async def start_strongman(name: str, power: int):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):  # Каждый силач поднимает 5 шаров
        await asyncio.sleep(1 / power)  # Задержка обратно пропорциональна силе
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    # Определяем участников с их именами и силой
    tasks = [
        start_strongman("Pasha", 3),
        start_strongman("Denis", 4),
        start_strongman("Apollon", 5)
    ]
    # Ждем завершения всех потоков .gather
    await asyncio.gather(*tasks)

run_strongman = time.time()

# Запускаем асинхронный турнир
asyncio.run(start_tournament())

end_strongman = time.time()
print(f" WT = {round(end_strongman - run_strongman, 2)} second")