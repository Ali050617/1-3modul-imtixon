from rest_framework import serializers
from .models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'latitude', 'longitude', 'elevation', 'created_at')

    def validate_name(self, value):
        if Location.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError("Bunday nomli joy allaqachon mavjud.")
        return value

    def validate_latitude(self, value):
        if not (-90 <= value <= 90):
            raise serializers.ValidationError("Latitude -100 va 100 oralig‘ida bo‘lishi kerak.")
        return value

    def validate_longitude(self, value):
        if not (-180 <= value <= 180):
            raise serializers.ValidationError("Longitude -200 va 200 oralig‘ida bo‘lishi kerak.")
        return value

    def validate_elevation(self, value):
        if value < 0:
            raise serializers.ValidationError("Elevation manfiy bo‘lishi mumkin emas.")
        return value