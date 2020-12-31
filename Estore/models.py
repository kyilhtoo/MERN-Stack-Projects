from django.db import models
from django.urls import reverse



class Category(models.Model):
    name = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "products"

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('Estore:product_details', args=[self.id])


class Images(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='product-images', blank=True)

    class Meta:
        verbose_name_plural = 'images'








