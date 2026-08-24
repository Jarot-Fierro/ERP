from django.urls import path

from materials.views import MaterialListView, MaterialCreateView, MaterialUpdateView

app_name = 'materials'

urlpatterns = [
    path(
        'list/',
        MaterialListView.as_view(),
        name='material_list'
    ),
    path(
        'create/',
        MaterialCreateView.as_view(),
        name='material_create'
    ),
    path(
        'update/<int:pk>/',
        MaterialUpdateView.as_view(),
        name='material_update'
    ),
]
