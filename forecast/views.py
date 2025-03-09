from django.db.models import F, Avg, Sum, Max
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Forecast
from .serializers import ForecastSerializer, AnalyticsSerializer, ForecastByLocationSerializer


class ForecastPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class ForecastListCreateView(generics.ListCreateAPIView):
    queryset = Forecast.objects.all().order_by("-created_at")
    serializer_class = ForecastSerializer
    pagination_class = ForecastPagination


class ForecastDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer
    lookup_field = 'id'


class ForecastByLocationView(generics.ListAPIView):
    serializer_class = ForecastByLocationSerializer
    pagination_class = ForecastPagination

    def get_queryset(self):
        location_id = self.kwargs["location_id"]
        return Forecast.objects.filter(location_id=location_id).order_by("forecast_date")


class TemperatureAvgView(generics.ListAPIView):
    serializer_class = AnalyticsSerializer

    def get_queryset(self):
        avg_temp = Forecast.objects.aggregate(avg_temperature=Avg((F('temperature_min') + F('temperature_max')) / 2))
        return [{'metric': avg_temp['avg_temperature'] if avg_temp['avg_temperature'] is not None else 0}]


class PrecipitationSumView(generics.ListAPIView):
    serializer_class = AnalyticsSerializer

    def get_queryset(self):
        total_precipitation = Forecast.objects.aggregate(total_precipitation=Sum('precipitation_probability'))
        return [{'metric': total_precipitation['total_precipitation'] if total_precipitation['total_precipitation'] is not None else 0}]


class MaxWindSpeedView(generics.ListAPIView):
    serializer_class = AnalyticsSerializer

    def get_queryset(self):
        max_wind_speed = Forecast.objects.aggregate(max_wind_speed=Max('wind_speed'))
        return [{'metric': max_wind_speed['max_wind_speed'] if max_wind_speed['max_wind_speed'] is not None else 0}]
