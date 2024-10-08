from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'), # Redirect to home page upon visiting root URL
    path('room/', views.room, name='room'), # Room page URL
    path('login/', views.login_view, name='login'), # Room page URL
    path('register/', views.register, name='register'), # Room page URL
    path('dashboard/', views.dashboard, name='dashboard'), # Room page URL
    path('products/', views.products, name='products'),
    path('logout/', views.user_logout, name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)