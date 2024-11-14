from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, InputFile
import asyncio

# Импортируем функции работы с БД
from crud_functions import initiate_db, get_all_products, add_user, is_included
# Для проверки корректности введенного email
import re

# Инициализация базы данных
initiate_db()

# Инициализация бота
api_key = "6601810404:AAEIG6q3uX7akLbehWQ368D44AqNsgA2j64"
bot = Bot(token=api_key)
dp = Dispatcher(bot, storage=MemoryStorage())


# Определение группы состояний для регистрации
class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()


# Определение группы состояний для расчета калорий
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


# Создание обычной клавиатуры
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton("Рассчитать")
button_info = KeyboardButton("Информация")
button_buy = KeyboardButton("Купить")
button_register = KeyboardButton("Регистрация")
keyboard.row(button_calculate, button_info)
keyboard.add(button_buy, button_register)

# Inline клавиатура для расчета
calculate_keyboard = InlineKeyboardMarkup(row_width=1)
calculate_keyboard.add(
    InlineKeyboardButton("Рассчитать норму калорий", callback_data='calories'),
    InlineKeyboardButton("Формулы расчёта", callback_data='formulas')
)

# Inline клавиатура для продуктов
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
    await message.reply("Разработал Назим")


# Обработчик для кнопки "Рассчитать"
@dp.message_handler(Text(equals="Рассчитать", ignore_case=True))
async def main_menu(message: types.Message):
    await message.reply("Выберите опцию:", reply_markup=calculate_keyboard)


# Обработчик для Inline-кнопки "Формулы расчёта"
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


# Обработчик для Inline-кнопки "Рассчитать норму калорий"
@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_age(call: types.CallbackQuery):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()


# Запрашиваем рост после возраста
@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.reply("Введите свой рост (в см):")
    await UserState.growth.set()


# Запрашиваем вес после роста
@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.reply("Введите свой вес (в кг):")
    await UserState.weight.set()


# Вычисляем калории после ввода веса
@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    calories = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.reply(f"Ваша норма калорий: {calories} ккал в день.")
    await state.finish()


# Обработчик для кнопки "Регистрация"
@dp.message_handler(Text(equals="Регистрация", ignore_case=True))
async def sign_up(message: types.Message):
    await message.reply("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()


# Установка имени пользователя
@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text.lower()  # Приводим к нижнему регистру

    # Проверка, существует ли пользователь
    if is_included(username):
        await message.reply("Пользователь существует, введите другое имя.")
    else:
        await state.update_data(username=username)
        await message.reply("Введите свой email:")
        await RegistrationState.email.set()


# # Установка email
# @dp.message_handler(state=RegistrationState.email)
# async def set_email(message: types.Message, state: FSMContext):
#     email = message.text
#     await state.update_data(email=email)
#     await message.reply("Введите свой возраст:")
#     await RegistrationState.age.set()

# Установка email с проверкой корректности
@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    email = message.text

    # Регулярное выражение для проверки формата email
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(email_pattern, email):
        await message.reply("Некорректный формат email. Пожалуйста, введите корректный email:")
        return  # Возвращаемся, чтобы пользователь ввел email снова

    # Если email корректный, сохраняем его в состоянии и переходим к следующему шагу
    await state.update_data(email=email)
    await message.reply("Введите свой возраст:")
    await RegistrationState.age.set()


# Установка возраста и завершение регистрации
@dp.message_handler(state=RegistrationState.age)
async def set_age_for_registration(message: types.Message, state: FSMContext):
    try:
        age = int(message.text)
        if age < 18:
            await message.reply(
                "Регистрация доступна только для пользователей от 18 лет. К сожалению, вы не можете зарегистрироваться.")
            await state.finish()  # Завершаем состояние, чтобы прекратить регистрацию
            return
    except ValueError:
        await message.reply("Пожалуйста, введите числовое значение возраста.")
        return

    # Сохраняем возраст и баланс по умолчанию
    await state.update_data(age=age, balance=1000)
    user_data = await state.get_data()

    # Добавляем пользователя в базу данных
    add_user(user_data['username'], user_data['email'], user_data['age'])
    await message.reply("Регистрация завершена! Добро пожаловать!")
    await state.finish()


# Обработчик для кнопки "Купить"
@dp.message_handler(Text(equals="Купить", ignore_case=True))
async def get_buying_list(message: types.Message):
    products = get_all_products()  # Получаем список продуктов из БД
    for product in products:
        product_id, title, description, price = product
        product_text = f"Название: {title} | Описание: {description} | Цена: {price} рублей"
        try:
            photo = InputFile(f'pic_{product_id}.jpg')  # Загружаем файл изображения по ID продукта
            await message.reply_photo(photo=photo, caption=product_text)
        except Exception:
            await message.reply(product_text)  # Если фото нет, отправляем только текст
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
