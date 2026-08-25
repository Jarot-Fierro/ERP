from django.urls import path

from purchases.views import (
    PurchaseOrderListView,
    PurchaseOrderCreateView,
    PurchaseOrderUpdateView,
    PurchaseOrderDetailView,
)

app_name = 'purchases'

urlpatterns = [
    path(
        'list/',
        PurchaseOrderListView.as_view(),
        name='purchase_list'
    ),
    path(
        'create/',
        PurchaseOrderCreateView.as_view(),
        name='purchase_create'
    ),
    path(
        'update/<int:pk>/',
        PurchaseOrderUpdateView.as_view(),
        name='purchase_update'
    ),
    path(
        'detail/<int:pk>/',
        PurchaseOrderDetailView.as_view(),
        name='purchase_detail'
    ),
]
