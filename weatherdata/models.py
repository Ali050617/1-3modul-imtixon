from django.db import models
from locations.models import Location


class WeatherData(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='weather_data')
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    wind_speed = models.FloatField()
    wind_direction = models.FloatField()
    precipitation = models.FloatField()
    recorded_at = models.DateTimeField()

    def __str__(self):
        return f"Weather at {self.location.name} on {self.recorded_at}"
