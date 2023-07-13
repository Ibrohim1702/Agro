from django.contrib import admin

# Register your models here.
from .models import *


class ProductImgInline(admin.StackedInline):
    model = ProdImg


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImgInline]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
