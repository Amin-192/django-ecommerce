from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'), # Redirect to home page upon visiting root URL
    path('room/', views.room, name='room'), # Room page URL
]