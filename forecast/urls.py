from django.urls import path
from . import views

urlpatterns = [
    path('forecasts/', views.ForecastListCreateView.as_view(), name='forecast_list_create'),
    path('forecasts/<int:id>/', views.ForecastDetailView.as_view(), name='forecast_detail'),
    path('forecasts/location/<int:location_id>/', views.ForecastByLocationView.as_view(), name='forecast_by_location'),
    path('analytics/temperature-avg/', views.TemperatureAvgView.as_view(), name='temperature_avg'),
    path('analytics/precipitation-sum/', views.PrecipitationSumView.as_view(), name='precipitation_sum'),
    path('analytics/wind-speed-max/', views.MaxWindSpeedView.as_view(), name='wind+speed_max'),
]




