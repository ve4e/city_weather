
from asgiref.sync import sync_to_async
from django.http import JsonResponse, Http404

from .models import City
from .utils.yandex_api import WeatherDataType, yandex_weather_report


async def weather(request):
    """View в зависимости от request.path возвращает либо текущие погодные данные, либо прогноз на день"""

    WEATHER_DATA_TYPE = {
        '/weather': WeatherDataType.fact,
        '/forecast': WeatherDataType.forecast,
    }

    try:
        city = await sync_to_async(City.objects.get)(name=request.GET.get('city'))
    except City.DoesNotExist:
        raise Http404("Object not found")

    report = await yandex_weather_report(WEATHER_DATA_TYPE[request.path], city.latitude, city.longitude)

    return JsonResponse(report.model_dump())















