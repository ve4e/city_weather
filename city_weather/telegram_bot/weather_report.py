from typing import Dict

import aiohttp
from aiohttp import ContentTypeError

from city_weather.common.pydantic_models import WeatherReport
from city_weather.telegram_bot.config import WEATHER_SERVER_ADDRESS


def report_beautifier(report: WeatherReport) -> str:
    return f'Прогноз погоды на сегодня ! ✨\n' \
           f'🌡: {report.temp}\n' \
           f'🎈: {report.pressure_mm}\n' \
           f'🌪: {report.wind_speed}\n'


async def weather_report(city: str) -> str:
    """
    Функция формирует доклад по данным от веб сервера. В случае ошибки вызывает исключение ValueError
    """
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'http://{WEATHER_SERVER_ADDRESS}/forecast?city={city}') as response:
                report = WeatherReport.model_validate(await response.json())
    except ContentTypeError:
        raise ValueError
    else:
        return report_beautifier(report)


