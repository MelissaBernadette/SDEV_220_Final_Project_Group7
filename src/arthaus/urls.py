"""arthaus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pages.views import home_view
import products.views as views
from django.contrib.auth import views as auth_views
from user import views as user_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("home/", home_view, name="home"),
    path("product/", views.product_detail_view),
    path("product/<int:pk>/", views.product_detail_view, name="product-detail-vew"),
    path("admin/", admin.site.urls),
    path("index/", views.index, name="dashboard-index"),
    path("products/", views.products, name="dashboard-products"),
    path("products/delete/<int:pk>/", views.product_delete, name="dashboard-products-delete",),
    path("products/detail/<int:pk>/",views.product_detail,name="dashboard-products-detail",),
    path("products/edit/<int:pk>/", views.product_edit, name="dashboard-products-edit"),
    path("customers/", views.customers, name="dashboard-customers"),
    path("customers/detail/<int:pk>/",views.customer_detail,name="dashboard-customer-detail",),
    path("order/", views.order, name="dashboard-order"),
    path("source/", views.source, name="dashboard-source"),
    path("source/detail/<int:pk>/",views.source_detail,name="dashboard-source-detail",),
    path("admin/", admin.site.urls),
    #path('', include('dashboard.urls')),
    path('register/', user_views.register, name='user-register'),
    path("",auth_views.LoginView.as_view(template_name="user/login.html"),name="user-login",),
    path('profile/', user_views.profile, name='user-profile'),
    path('profile/update/', user_views.profile_update,name='user-profile-update'),
    path("logout/",auth_views.LogoutView.as_view(template_name="user/logout.html"),name="user-logout",),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
