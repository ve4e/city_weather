from enum import Enum
from typing import Dict

import aiohttp
from city_weather.common.pydantic_models import WeatherReport


async def make_async_request(url: str, headers: Dict[str, str]) -> Dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            return await response.json()


class WeatherDataType(Enum):
    fact = 'fact'
    forecast = 'forecast'


async def yandex_weather_report(data_type: WeatherDataType, latitude: float, longitude: float) -> WeatherReport:
    """ Функция запрашивает и возвращает данные от сервиса 'Яндекс Погода' """

    YANDEX_API_KEY = '7eca6aaf-09a1-4f16-ad5f-5669a9f3be91'  # да, ключи лучше не хранить в коде )
    URL = 'https://api.weather.yandex.ru/v2/forecast?lat={}&lon={}'
    HEADER = {'X-Yandex-API-Key': YANDEX_API_KEY}

    report = await make_async_request(URL.format(latitude, longitude), HEADER)

    if data_type == WeatherDataType.fact:
        return WeatherReport.model_validate(report['fact'])
    elif data_type == WeatherDataType.forecast:
        return WeatherReport.model_validate(report['forecasts'][0]['parts']['day_short'])



