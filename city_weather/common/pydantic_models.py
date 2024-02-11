from pydantic import BaseModel


class WeatherReport(BaseModel):
    temp: int
    pressure_mm: int
    wind_speed: float
