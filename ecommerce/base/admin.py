from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'sold_out')
    list_editable = ('sold_out',)

admin.site.register(Product, ProductAdmin)  # Only register the model here