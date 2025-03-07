from rest_framework import serializers
from .models import Forecast
from locations.models import Location


class LocationShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["id", "name"]


class ForecastByLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forecast
        fields = [
            "id", "forecast_date", "temperature_min", "temperature_max",
            "humidity", "precipitation_probability", "wind_speed",
            "wind_direction", "created_at"
        ]


class ForecastSerializer(serializers.ModelSerializer):
    location = LocationShortSerializer(read_only=True)

    class Meta:
        model = Forecast
        fields = [
            "id", "location", "forecast_date", "temperature_min", "temperature_max",
            "humidity", "precipitation_probability", "wind_speed", "wind_direction", "created_at"
        ]


class AnalyticsSerializer(serializers.Serializer):
    metric = serializers.FloatField()