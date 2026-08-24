from django.urls import path

from suppliers.views import SupplierListView, SupplierCreateView, SupplierUpdateView

app_name = 'suppliers'

urlpatterns = [
    path(
        'list/',
        SupplierListView.as_view(),
        name='supplier_list'
    ),
    path(
        'create/',
        SupplierCreateView.as_view(),
        name='supplier_create'
    ),
    path(
        'update/<int:pk>/',
        SupplierUpdateView.as_view(),
        name='supplier_update'
    ),
]
