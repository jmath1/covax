
from django.urls import path
from core import views
urlpatterns = [
    path('', views.home),
    path('location/<int:location_id>', views.location),
]
