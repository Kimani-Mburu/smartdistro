from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.http import request
from django.utils import timezone
from django.utils.text import slugify
from django.shortcuts import reverse
from datetime import date, datetime

from UserInformation.models import Farmer


# products categories

class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='title')
    category_desc = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=150, unique=True, allow_unicode=True, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        unique_together = (('category_name', 'slug'),)
        
    def get_absolute_url(self):
        return reverse("category", args=[self.slug])
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.category_name
    
    
# Products units

class Unit(models.Model):
    unit_name = models.CharField(max_length=20)
    unit_desc = models.CharField(max_length=50)
    
    def __str__(self):
        return self.unit_name
    
    
    
# product information

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_category = models.ForeignKey(Category, on_delete=CASCADE, verbose_name='Category')
    product_images = models.ImageField(upload_to='images/%Y/%m/%d',default=None, verbose_name='Thumbnail')
    product_other_image = models.ImageField(upload_to='images/%Y/%m/%d',blank=True, null=True)
    product_other_image1 = models.ImageField(upload_to='images/%Y/%m/%d',blank=True, null=True)
    product_unit = models.ForeignKey(Unit, on_delete=CASCADE)
    product_unit_price = models.FloatField()
    product_availability_wef_date = models.DateTimeField(default=datetime.now, verbose_name='Available from')
    product_availability_wet_date = models.DateTimeField(blank=True, null=True, verbose_name='Available until')
    product_location = models.CharField(max_length=30, blank=True, null=True)
    product_created_on = models.DateTimeField(default=datetime.now)
    product_is_featured = models.BooleanField(default=False)
    product_farmer_login_id = models.ForeignKey(Farmer, on_delete=CASCADE)
    
    
    def __str__(self):
        return self.product_name
    
    def get_absolute_url(self):
        return reverse("supply:product", args=[self.pk])
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
