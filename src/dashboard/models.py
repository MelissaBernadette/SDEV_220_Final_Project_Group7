from django.db import models
from django.contrib.auth.models import User
from distutils.command.upload import upload

# Create your models here.

COLOR_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
    ('yellow', 'YELLOW'),
    ('purple', 'PURPLE'),
    ('light green','LIGHT GREEN'),
    ('light blue', 'LIGHT BLUE'),
    ('pink','PINK'),
    ('light orange','LIGHT ORANGE'),
    ('gray','GRAY'),
    ('light yellow', 'LIGHT YELLOW'),
    ('light purple', 'LIGHT PURPLE'),
    ('white', 'WHITE'),
    ('rainbow', 'RAINBOW')
)

SIZE_CHOICES = (
    ('small', 'SMALL'),
    ('standard', 'STANDARD'),
    ('large', 'LARGE'),
    ('x-large', 'X-LARGE')
)

MATERIAL_CHOICES = (
    ('mylar', 'MYLAR'),
    ('latex', 'LATEX')
)

class Product(models.Model):
    title = models.CharField(max_length=120, null=True)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    shape = models.CharField(max_length=120, null=True)
    material = models.CharField(max_length=8, choices=MATERIAL_CHOICES, default='latex')
    color = models.CharField(max_length=12, choices=COLOR_CHOICES, default='green')
    size = models.CharField(max_length=8, choices=SIZE_CHOICES, default='small')
    quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'${self.price} - {self.title}'

class Order(models.Model):
    title = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.customer}-{self.title}'

class Source(models.Model):
    source = models.CharField(max_length=120, null=True)
    source_email = models.CharField(max_length=120, null=True)

    def __str__(self):
        return f'{self.source}'