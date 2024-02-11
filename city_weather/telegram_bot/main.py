
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from city_weather.telegram_bot.weather_report import weather_report

TOKEN = "6416996182:AAG2vrq1GHC7eqC_4GbIOR49_dMn7oulfCM"
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    """ Обработка команды Старт """
    await message.answer(f"Привет, {hbold(message.from_user.full_name)}! "
                         f"Напиши название города, и я дам прогноз погоды на день 🔮✨")


@dp.message()
async def message_handler(message: types.Message):
    """ Обработка сообщений """
    try:
        resp = await weather_report(message.text)
    except ValueError:
        await message.answer(str('Ваш город не найден на карте :('))
    else:
        await message.answer(str(resp))


async def main():
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())










