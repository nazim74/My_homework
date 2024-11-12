from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, InputFile
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
button_buy = KeyboardButton("Купить")
keyboard.row(button_calculate, button_info)
keyboard.add(button_buy)

# Создание Inline клавиатуры для функции "Рассчитать"
inline_keyboard = InlineKeyboardMarkup(row_width=1)
button_calories = InlineKeyboardButton("Рассчитать норму калорий", callback_data='calories')
button_formulas = InlineKeyboardButton("Формулы расчёта", callback_data='formulas')
inline_keyboard.add(button_calories, button_formulas)

# Меню для продуктов с картинками
product_keyboard = InlineKeyboardMarkup(row_width=2)
product_buttons = [
    InlineKeyboardButton(f"Продукт {i}", callback_data="product_buying") for i in range(1, 5)
]
product_keyboard.add(*product_buttons)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.reply("Привет! Я бот, помогающий твоему здоровью.", reply_markup=keyboard)

# Обработчик для кнопки "Информация"
@dp.message_handler(Text(equals="Информация", ignore_case=True))
async def send_info(message: types.Message):
    await message.reply("Хорошая пластинка поможет вашему здоровью лучше чем любой БАД...))")

# Обработчик для кнопки "Рассчитать"
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

# Обработчик для кнопки "Рассчитать норму калорий"
@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_age(call: types.CallbackQuery):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()

# Обработка состояния UserState.age
@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.reply("Введите свой рост (в см):")
    await UserState.growth.set()

# Обработка состояния UserState.growth
@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.reply("Введите свой вес (в кг):")
    await UserState.weight.set()

# Обработка состояния UserState.weight и вычисление калорий
@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)

    # Получаем данные из состояния
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    # Формула Миффлина-Сан Жеора для мужчин
    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.reply(f"Ваша норма калорий: {calories} ккал в день.")
    await state.finish()

# Обработчик для кнопки "Купить"
@dp.message_handler(Text(equals="Купить", ignore_case=True))
async def get_buying_list(message: types.Message):
    # Отправка изображений продуктов с описанием
    for i in range(1, 5):
        product_text = f"Название: Product{i} | Описание: описание {i} | Цена: {i * 100} рублей"
        photo = InputFile(f'pic_{i}.jpg')  # Загружаем файл изображения (например, pic_1.jpg, pic_2.jpg и т.д.)
        await message.reply_photo(photo=photo, caption=product_text)
    await message.reply("Выберите продукт для покупки:", reply_markup=product_keyboard)

# Обработчик для покупки продукта
@dp.callback_query_handler(lambda call: call.data == "product_buying")
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

# Запуск бота
if __name__ == "__main__":
    print("Bot is starting...")
    executor.start_polling(dp, skip_updates=True)
