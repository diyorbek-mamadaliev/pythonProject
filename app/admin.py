from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class UserModel(UserAdmin):
    list_display = ['username', 'user_type']
admin.site.register(CustomUser, UserModel)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'quantity', 'image']
    search_fields = ['name', 'description']
    ordering = ['name']
    fields = ['name', 'description', 'price', 'quantity', 'image']

admin.site.register(Product, ProductAdmin)


class SoldItemAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'quantity_sold', 'payment_type', 'sold_at', 'comment']
    search_fields = ['product__name', 'payment_type', 'comment']
    list_filter = ['product__name', 'comment', 'payment_type', 'sold_at']
    ordering = ['-sold_at']  # Sort by the most recent sold items first

admin.site.register(SoldItem, SoldItemAdmin)
