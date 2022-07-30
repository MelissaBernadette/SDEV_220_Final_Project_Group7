from django import forms
from .models import Product, Order, Source


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['title', 'order_quantity']

class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = ['source', 'source_email']
