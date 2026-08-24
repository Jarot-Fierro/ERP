from django.urls import path

from customers.views import CustomerListView, CustomerCreateView, CustomerUpdateView

app_name = 'customers'

urlpatterns = [
    path(
        'list/',
        CustomerListView.as_view(),
        name='customer_list'
    ),
    path(
        'create/',
        CustomerCreateView.as_view(),
        name='customer_create'
    ),
    path(
        'update/<int:pk>/',
        CustomerUpdateView.as_view(),
        name='customer_update'
    ),
]
