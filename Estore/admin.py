from django.contrib import admin
from . models import Category, Products, Images

from tinymce.widgets import TinyMCE
from django.db import models



class ImagesAdmin(admin.StackedInline):
    model = Images


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'updated')
    fields = ('name', 'slug', 'category', 'price', 'description',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ImagesAdmin]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

