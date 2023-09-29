import os
import logging
import random

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import config
from dotenv import load_dotenv
# from keyboards import *
from model import Model

load_dotenv(".env")

ROBOFLOW_TOKEN = os.getenv("ROBOFLOW_API_TOKEN")
BOT_TOKEN = os.getenv("BOT_API_TOKEN")

# Инициализация нейронной сети, бота и диспетчера
model = Model(api_key=ROBOFLOW_TOKEN, id_=config.ROBOFLOW_ID, version=config.ROBOFLOW_VERSION)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Включение логирования
logging.basicConfig(level=logging.INFO)


@dp.callback_query_handler(lambda c: c.data.startswith('mode'))
async def mode_choice_process(callback: types.CallbackQuery):
    photo_path = callback.data[callback.data.find('?') + 1:]  # получаем путь к фото из callback
    url = f'https://api.telegram.org/file/bot{BOT_TOKEN}/{photo_path}'  # создаем url
    if 'mode_image' in callback.data:
        await callback.message.edit_reply_markup()  # Блокировка кнопки
        prediction = model.get_predict(url, confidence=20, overlap=1, hosted=True, mode='image')
        await callback.message.answer_photo(photo=prediction, caption='_Фрутилупс 2.0_',
                                            parse_mode='Markdown')  # отправка фото

    if 'mode_list' in callback.data:
        await callback.message.edit_reply_markup()  # Блокировка кнопки
        prediction = model.get_predict(url, confidence=20, overlap=100, hosted=True, mode='list')
        await callback.message.answer(text=f'*Я думаю, что тут у нас*:\n{", ".join(prediction)}\n_Фрутилупс 2.0_',
                                      parse_mode='Markdown')


# Обработка команды start
@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    await message.reply(config.command_start_message, parse_mode='Markdown')


# Обработка команды help
@dp.message_handler(commands=['help'])
async def echo(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    author_button = KeyboardButton(text='Автор')
    model_button = KeyboardButton(text='Модель')
    keyboard.add(author_button, model_button)

    await message.reply(config.command_help_message, reply_markup=keyboard)


# Обработка присылаемого изображения
@dp.message_handler(content_types=[types.ContentType.PHOTO])
async def download_photo(message: types.Message):
    photo_file = await bot.get_file(message.photo[-1].file_id)
    photo_path = photo_file.file_path

    keyboard = InlineKeyboardMarkup()
    image_mode = InlineKeyboardButton(text="Изображение 🖼", callback_data=f'mode_image?{photo_path}')
    list_mode = InlineKeyboardButton(text="Список 📋", callback_data=f'mode_list?{photo_path}')
    keyboard.add(image_mode, list_mode)

    await message.answer_photo(photo=photo_file.file_id, caption='Выберите вариант 🤖', reply_markup=keyboard)


@dp.message_handler(content_types=[types.ContentType.TEXT, types.ContentType.ANY])
async def message_handler(message: types.Message):
    if message.text == 'Автор':
        await message.answer(config.author_info, parse_mode='Markdown')
    elif message.text == 'Модель':
        await message.answer(config.model_info, parse_mode='Markdown')
    else:
        await message.answer(random.choice(config.text_phrases))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
