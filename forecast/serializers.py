from rest_framework import serializers
from collections import OrderedDict
from .models import Forecast
from locations.models import Location


class LocationShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["id", "name"]


class ForecastByLocationSerializer(serializers.ModelSerializer):
    location = LocationShortSerializer(read_only=True)

    class Meta:
        model = Forecast
        fields = [
            "id", "location", "forecast_date", "temperature_min",
            "temperature_max", "humidity", "precipitation_probability",
            "wind_speed", "wind_direction", "created_at"
        ]


class ForecastSerializer(serializers.ModelSerializer):
    location = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(), write_only=True
    )
    location_details = LocationShortSerializer(source="location", read_only=True)

    class Meta:
        model = Forecast
        fields = [
            "id", "location", "location_details", "forecast_date",
            "temperature_min", "temperature_max", "humidity",
            "precipitation_probability", "wind_speed", "wind_direction",
            "created_at"
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        location_data = representation.pop("location_details")
        ordered_data = OrderedDict([
            ("id", representation.pop("id")),
            ("location", location_data),
            *representation.items()
        ])
        return ordered_data


class AnalyticsSerializer(serializers.Serializer):
    metric = serializers.FloatField()