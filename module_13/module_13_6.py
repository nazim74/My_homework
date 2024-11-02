from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

# Инициализация бота
api_key = ""
bot = Bot(token=api_key)
dp = Dispatcher(bot, storage=MemoryStorage())

# Определение группы состояний
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

# Создание обычной клавиатуры
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton("Рассчитать")
button_info = KeyboardButton("Информация")
keyboard.add(button_calculate, button_info)

# Создание Inline клавиатуры
inline_keyboard = InlineKeyboardMarkup(row_width=1)
button_calories = InlineKeyboardButton("Рассчитать норму калорий", callback_data='calories')
button_formulas = InlineKeyboardButton("Формулы расчёта", callback_data='formulas')
inline_keyboard.add(button_calories, button_formulas)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.reply("Привет! Я бот, помогающий твоему здоровью.", reply_markup=keyboard)

# Обработчик для кнопки "Информация"
@dp.message_handler(Text(equals="Информация", ignore_case=True))
async def send_info(message: types.Message):
    await message.reply("Разработал Назим")

# Функция вывода Inline меню
@dp.message_handler(Text(equals="Рассчитать", ignore_case=True))
async def main_menu(message: types.Message):
    await message.reply("Выберите опцию:", reply_markup=inline_keyboard)

# Обработчик для кнопки "Формулы расчёта"
@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    formula_text = (
        "Формула Миффлина-Сан Жеора для мужчин:\n"
        "BMR = 10 * вес + 6.25 * рост - 5 * возраст + 5\n\n"
        "Формула Миффлина-Сан Жеора для женщин:\n"
        "BMR = 10 * вес + 6.25 * рост - 5 * возраст - 161"
    )
    await call.message.answer(formula_text)
    await call.answer("Формулы отправлены!", show_alert=True)
# Функция начала опроса для расчета калорий
@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_age(call: types.CallbackQuery):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()  # Устанавливаем состояние для возраста

# Обработка состояния UserState.age
@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)  # Сохраняем возраст
    await message.reply("Введите свой рост (в см):")
    await UserState.growth.set()  # Устанавливаем следующее состояние для роста

# Обработка состояния UserState.growth
@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)  # Сохраняем рост
    await message.reply("Введите свой вес (в кг):")
    await UserState.weight.set()  # Устанавливаем следующее состояние для веса

# Обработка состояния UserState.weight и вычисление калорий
@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)  # Сохраняем вес

    # Получаем данные из состояния
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    # Формула Миффлина-Сан Жеора для мужчин:
    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.reply(f"Ваша норма калорий: {calories} ккал в день.")
    await state.finish()  # Завершаем машину состояний

# Запуск бота
if __name__ == "__main__":
    print("Bot is starting...")
    executor.start_polling(dp, skip_updates=True)
