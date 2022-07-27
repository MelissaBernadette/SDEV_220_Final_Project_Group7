from django import forms
from .models import Product, Order, Vendor


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['title', 'order_quantity']

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['title', 'vendor', 'vendor_quantity', 'vendor_price']
