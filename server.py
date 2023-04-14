import logging
import sqlite3
from aiogram import Bot, Dispatcher, executor, types
import datetime
from db import add_expense, today_category, month, delete_expense, month_category
from middleware import AccessMiddleware

API_TOKEN = '5816921578:AAH4KNQE0e-et7sUAoHZEbUOVP-IAXVXHrk'
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
ACCESS_ID = 602404694
dp.middleware.setup(AccessMiddleware(ACCESS_ID))

@dp.message_handler(commands=['help', 'start'])
async def send_welcome(message: types.Message):
    await message.answer(
        "Бот для учета финансов\n\n"
        "Добавить рассход 100 такси\n"
        "Остаток денег для трат в текущем месяце /cash\n"
        "Статистика без базовых трат за месяц /month\n"
        "Статистика без базовых трат за день по категориям /today\n"
        "Удалить последнюю запись /delete\n"
    )


@dp.message_handler(commands=['month'])
async def echo_month(message: types.Message):
    answer_message1 = month()
    answer_message2 = month_category()
    await message.answer("Потрачено в текущем месяце: " + str(answer_message1))
    for i in answer_message2:
     await message.answer(i)


@dp.message_handler(commands=['cash'])
async def echo_cash(message: types.Message):
    answer_message = int(15000) - int(month())
    await message.answer("Остаток денег в текущем месяце для трат: " + str(answer_message))


@dp.message_handler(commands=['today'])
async def echo_today(message: types.Message):
    try:
        answer_message = today_category()
        for i in answer_message:
            await message.answer(i)
    except:
        answer_message = "Еще нет трат за сегодня"
        await message.answer(answer_message)


@dp.message_handler(lambda message: message.text.startswith('/del'))
async def del_expense(message: types.Message):
    delete_expense()
    await message.answer("Запись удалена")


@dp.message_handler()
async def add(message: types.Message):
    con = sqlite3.connect("db/db.db")
    cur = con.cursor()
    text = message.text
    vars = text.split(" ")
    aliases_name = vars[1]
    try:
        res = cur.execute("SELECT codename from category where aliases like ?", ('%' + aliases_name + '%',))
        base_result = res.fetchone()
        codename = base_result[0]
    except:
        codename = "other"
    add_expense(vars[0], datetime.datetime.now(), codename, message.text)
    await message.answer("Данные записаны в бд")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
