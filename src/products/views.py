from django.shortcuts import render, redirect
from .models import Product, Order, Vendor, Source
from .forms import ProductForm, OrderForm, VendorForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import auth_users, allowed_users
from django.db.models import Q
from django.db.models import Sum

# Create your views here.


def product_detail_view(request, pk):
    obj = Product.objects.get(id=pk)
    context = {
        "title": obj.title,
        "price": obj.price,
        "color": obj.color,
        "shape": obj.shape,
        "material": obj.material,
        "size": obj.size,
    }
    return render(request, "product/detail.html", context)


@login_required(login_url="user-login")
def index(request):
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    customer = User.objects.filter(~Q(groups=1))
    customer_count = customer.count()
    source = Source.objects.all()
    sources_count = source.count()

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.customer = request.user
            obj.save()
            return redirect("dashboard-index")
    else:
        form = OrderForm()
    context = {
        "form": form,
        "order": order,
        "product": product,
        "product_count": product_count,
        "order_count": order_count,
        "customer_count": customer_count,
        "sources_count": sources_count,
    }
    return render(request, "dashboard/index.html", context)


@login_required(login_url="user-login")
def products(request):
    product = Product.objects.all()
    product_count = product.count()
    customer = User.objects.filter(~Q(groups=1))
    customer_count = customer.count()
    order = Order.objects.all()
    order_count = order.count()
    source = Source.objects.all()
    sources_count = source.count()
    product_quantity = Product.objects.filter(title="")
    order_quantity = Order.objects.aggregate(Sum('order_quantity'))
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_title = form.cleaned_data.get("title")
            messages.success(request, f"{product_title} has been added")
            return redirect("dashboard-products")
    else:
        form = ProductForm()
    context = {
        "product": product,
        "form": form,
        "customer_count": customer_count,
        "product_count": product_count,
        "order_count": order_count,
        "sources_count": sources_count,
        "product_quantity": product_quantity,
        "order_quantity": order_quantity,
    }
    return render(request, "dashboard/products.html", context)


@login_required(login_url="user-login")
@allowed_users(allowed_roles=["Staff"])
def source(request):
    customer = User.objects.filter(~Q(groups=1))
    customer_count = customer.count()
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    source = Source.objects.all()
    sources_count = source.count()

    context = {
        "source": source,
        "customer_count": customer_count,
        "product_count": product_count,
        "order_count": order_count,
        "sources_count": sources_count,
    }
    return render(request, "dashboard/source.html", context)

@login_required(login_url="user-login")
@allowed_users(allowed_roles=["Staff"])
def source_detail(request, pk):
    customer = User.objects.filter(~Q(groups=1))
    customer_count = customer.count()
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    source = Source.objects.all()
    sources_count = source.count()
    sources = Source.objects.get(id=pk)
    context = {
        "sources": sources,
        "customer_count": customer_count,
        "product_count": product_count,
        "order_count": order_count,
        "sources_count": sources_count,
    }
    return render(request, "dashboard/sources_detail.html", context)


@login_required(login_url="user-login")
def product_detail(request, pk):
    obj = Product.objects.get(id=pk)
    context = {
        "title": obj.title,
        "price": obj.price,
        "color": obj.color.capitalize(),
        "shape": obj.shape.capitalize(),
        "material": obj.material.capitalize(),
        "size": obj.size,
    }
    return render(request, "dashboard/products_detail.html", context)


@login_required(login_url="user-login")
@allowed_users(allowed_roles=["Staff"])
def customers(request):
    customer = User.objects.filter(~Q(groups=1))
    customer_count = customer.count()
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    source = Source.objects.all()
    sources_count = source.count()

    context = {
        "customer": customer,
        "customer_count": customer_count,
        "product_count": product_count,
        "order_count": order_count,
        "sources_count": sources_count,
    }
    return render(request, "dashboard/customers.html", context)


@login_required(login_url="user-login")
@allowed_users(allowed_roles=["Staff"])
def customer_detail(request, pk):
    customer = User.objects.filter(~Q(groups=1))
    customer_count = customer.count()
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    source = Source.objects.all()
    sources_count = source.count()
    
    customers = User.objects.get(id=pk)
    context = {
        "customers": customers,
        "customer_count": customer_count,
        "product_count": product_count,
        "order_count": order_count,
        "sources_count": sources_count,
    }
    return render(request, "dashboard/customers_detail.html", context)


@login_required(login_url="user-login")
@allowed_users(allowed_roles=["Staff"])
def product_edit(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("dashboard-products")
    else:
        form = ProductForm(instance=item)
    context = {
        "form": form,
    }
    return render(request, "dashboard/products_edit.html", context)


@login_required(login_url="user-login")
@allowed_users(allowed_roles=["Staff"])
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect("dashboard-products")
    context = {"item": item}
    return render(request, "dashboard/products_delete.html", context)


@login_required(login_url="user-login")
def order(request):
    order = Order.objects.all()
    order_count = order.count()
    customer = User.objects.filter(~Q(groups=1))
    customer_count = customer.count()
    product = Product.objects.all()
    product_count = product.count()
    source = Source.objects.all()
    sources_count = source.count()

    context = {
        "order": order,
        "customer_count": customer_count,
        "product_count": product_count,
        "order_count": order_count,
        "sources_count": sources_count,
    }
    return render(request, "dashboard/order.html", context)
