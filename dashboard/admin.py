from django.contrib import admin
from .models import Product, Order
from django.contrib.auth.models import Group

# Register your models here.
admin.site.site_header = 'SPRAKASH Dashboard'
# admin.site.unregister(Group)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category','quantity']
    list_filter = ['category']

admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','product', 'staff', 'order_quantity', 'date']

admin.site.register(Order, OrderAdmin)






