from django.urls import path
from . import views

urlpatterns = [
    path('location/', views.LocationListCreateView.as_view(), name='location_list_create'),
    path('location/<int:id>/', views.LocationDetailView.as_view(), name='location_detail'),
]