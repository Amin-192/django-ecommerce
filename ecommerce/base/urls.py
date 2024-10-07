from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'), # Redirect to home page upon visiting root URL
    path('room/', views.room, name='room'), # Room page URL
    path('products/', views.products, name='products'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)