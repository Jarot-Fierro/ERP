from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config import settings

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
        'products/',
        include('products.urls')
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

handler404 = 'core.errors.handler404'
handler403 = 'core.errors.handler403'
handler500 = 'core.errors.handler500'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
