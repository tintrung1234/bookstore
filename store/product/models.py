from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=255, default='')
    description = models.CharField(max_length=255, default='')
    active = models.BooleanField(default=True)
    slug = models.CharField(max_length=255, default='')
    # slug = models.SlugField(default="", null=False)


class Product(models.Model):
    name = models.CharField(max_length=255, default='')
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    image = models.CharField(max_length=255, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    provider = models.CharField(max_length=255)
    active = models.BooleanField(default=True)


class Variation(models.Model):
    name = models.CharField(max_length=255, default='')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    active = models.BooleanField(default=True)
    sale_price = models.FloatField(default=0)
    inventory = models.IntegerField(default=0)
