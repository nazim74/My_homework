from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

api_key = ""
bot = Bot(token=api_key)
dp = Dispatcher(bot, storage=MemoryStorage())

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

# Обработчик для всех остальных сообщений
@dp.message_handler()
async def all_message(message: types.Message):
    # Сообщение, если команда /start не была введена
    await message.answer("Введите команду /start, чтобы начать общение.")

if __name__ == "__main__":
    print("Bot is starting...")
    executor.start_polling(dp, skip_updates=True)
