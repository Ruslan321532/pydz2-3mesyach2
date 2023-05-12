from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from decouple import config
import logging

TOKEN = config("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    # if message.text == "/help":
    await message.answer(f"Салалекум {message.from_user.full_name}")


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_1")
    markup.add(button_1)

    question = "Что такое фронтенд‑разработка"
    answers = [
        "создание телеграм ботов",
        "создание ios приложении",
        "это создание пользовательского интерфейса на клиентской стороне веб‑сайта или приложения.",
    ]
    # await message.answer_poll()
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        open_period=10,
        reply_markup=markup
    )


@dp.callback_query_handler(text="button_1")
async def quiz_2(call: types.CallbackQuery):
    question = "Что такое бэкенд‑разработка"
    answers = [
        "Бэкенд — это разработка бизнес-логики продукта (сайта или веб-приложения).",
        "Разработчик Веб сайтов и SPA приложений",
        "Разработчик андроид приложении",
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        open_period=10,
    )


@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)
    # await message.answer("This is an answer method!")
    # await message.reply("This is a reply method")
@dp.message_handler(commands=['mem', ])
async def hendler(message: types.Message):
    # if message.text == "/help":
    await message.answer(f"Салалекум {message.from_user.full_name}")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)