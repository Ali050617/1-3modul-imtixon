from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import WeatherData
from .serilazers import WeatherDataSerializer


class WeatherDatePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class WeatherDateListCreateView(generics.ListCreateAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
    pagination_class = WeatherDatePagination


class WeatherDateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
    lookup_field = 'id'


class WeatherDataByLocationView(generics.ListAPIView):
    serializer_class = WeatherDataSerializer
    pagination_class = WeatherDatePagination

    def get_queryset(self):
        location_id = self.kwargs.get('location_id')
        return WeatherData.objects.filter(location_id=location_id).select_related('location')
