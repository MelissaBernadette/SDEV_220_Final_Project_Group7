from django.contrib import admin

# Register your models here.
from .models import Product, Source, Order

admin.site.register(Product)
admin.site.register(Source)
admin.site.register(Order)