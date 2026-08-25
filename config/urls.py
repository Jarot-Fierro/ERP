from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(
        'admin/',
        admin.site.urls
    ),
    path(
        '',
        include('core.urls')
    ),
    path(
        'users/',
        include('users.urls')
    ),
    path(
        'materials/',
        include('materials.urls')
    ),
    path(
        'suppliers/',
        include('suppliers.urls')
    ),
    path(
        'customers/',
        include('customers.urls')
    ),
    path(
        'purchases/',
        include('purchases.urls')
    ),
]
