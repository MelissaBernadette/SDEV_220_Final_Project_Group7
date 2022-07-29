from django.contrib import admin

# Register your models here.
from .models import Product, Source

admin.site.register(Product)
admin.site.register(Source)