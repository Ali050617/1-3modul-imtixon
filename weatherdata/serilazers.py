from rest_framework import serializers
from .models import WeatherData
from locations.models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["id", "name"]


class WeatherDataSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)
    location_id = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(), source='location', write_only=True, required=False
    )

    class Meta:
        model = WeatherData
        fields = ('id', 'location', 'location_id', 'temperature', 'humidity', 'pressure',
                  'wind_speed', 'wind_direction', 'precipitation', 'recorded_at')

    def update(self, instance, validated_data):
        location = validated_data.pop('location', None)
        if location:
            instance.location = location
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
