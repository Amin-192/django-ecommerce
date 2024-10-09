from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),  # Redirect to home page upon visiting root URL
    path('room/', views.room, name='room'),  # Room page URL
    path('login/', views.login_view, name='login'),  # Login page URL
    path('register/', views.register, name='register'),  # Register page URL
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard page URL
    path('products/', views.products, name='products'),  # Products page URL
    path('logout/', views.user_logout, name='logout'),  # Logout page URL
    path('cart/', views.cart_detail, name='cart_detail'),  # Cart detail page URL
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  # Add to cart URL
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),  # Remove from cart URL
    path('cart/update/<int:product_id>/', views.update_cart, name='update_cart'),  # Update cart URL
    path('checkout/', views.checkout, name='checkout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)