#Сюда добавляем логику работы бота фнукции по добавлению удалению рассхода
import logging
import sqlite3
from aiogram import Bot, Dispatcher, executor, types
import datetime
from db import add_expense,get_today,month

API_TOKEN = '5816921578:AAH4KNQE0e-et7sUAoHZEbUOVP-IAXVXHrk'
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

@dp.message_handler(commands=['month'])
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    answer_message = month()
    await message.answer(answer_message)

@dp.message_handler(commands=['today'])
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    answer_message = get_today()
    await message.answer(answer_message)


@dp.message_handler()
async def add(message: types.Message):
    con = sqlite3.connect("db.db")
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