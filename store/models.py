from typing import ChainMap
from django.db import models
from django.db.models.fields import CharField
import datetime
import os


# Create your models here.
def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('uploads/', filename)




class Category(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(max_length=250, null=False, blank=False)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=250, null=False, blank=False)
    product_image = models.ImageField(upload_to=get_file_path, null=True, blank=True)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    product_id = models.CharField(null=True, max_length=100)
    customer_id = models.CharField(null=True, max_length=100)
    def __str__(self):
        return self.product_id + ' ' +self.customer_id

class Customer(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=200)
    billing_address = models.CharField(max_length=250, null=False)
    

    def __str__(self):
        return self.first_name + ' ' +self.last_name


class Order(models.Model):
    customer_id = models.CharField(null=True, max_length=100)
    shipping_address = models.CharField(max_length=200)
    order_address = models.CharField(max_length=150)
    order_email = models.CharField(max_length=100)
    order_date = models.DateField()
    order_status = models.BooleanField(default=False, help_text="0-default, 1=Hidden")
    
    def __str__(self):
        return self.customer_id

class OrderDetails(models.Model):
	product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order_id = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
original_price = models.FloatField(null=False, blank=False)
quantity = models.IntegerField(null=False, blank=False)
def __str__(self):
    return self.product_id + ' ' + self.order_id