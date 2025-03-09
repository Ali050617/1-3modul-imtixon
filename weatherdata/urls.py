from django.urls import path
from . import views

urlpatterns = [
    path('weather-data/', views.WeatherDateListCreateView.as_view(), name='weather_data_list_create'),
    path('weather-data/<int:id>/', views.WeatherDateDetailView.as_view(), name='weather_data_detail'),
    path('weather-data/location/<int:location_id>/', views.WeatherDataByLocationView.as_view(), name='weather_location'),

]