from django.contrib import admin

from store.models import Category
from .models import Category, Product, ProductCategory, Order, OrderDetails, Customer

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Order)
admin.site.register(OrderDetails)
admin.site.register(Customer)