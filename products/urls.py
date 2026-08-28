from django.urls import path

from products.views import ProductListView, ProductCreateView, ProductUpdateView

app_name = 'products'

urlpatterns = [
    path(
        'list/',
        ProductListView.as_view(),
        name='product_list'
    ),
    path(
        'create/',
        ProductCreateView.as_view(),
        name='product_create'
    ),
    path(
        'update/<int:pk>/',
        ProductUpdateView.as_view(),
        name='product_update'
    ),
]
