from django.contrib import messages
from django.urls import reverse_lazy

from core.standard.views import StandardListView, StandardCreateView, StandardUpdateView
from products.filters import ProductFilterForm
from products.forms import ProductForm
from products.models import Product


class ProductListView(StandardListView):
    model = Product
    template_name = 'products/list.html'
    title = 'Listado de Productos'
    module_name = 'productos'
    filter_form_class = ProductFilterForm
    export_fields_csv = ['id', 'name', 'unit', 'product_type', 'is_active']
    list_url_name = 'products:product_list'
    create_url_name = 'products:product_create'
    update_url_name = 'products:product_update'
    delete_url_name = None
    trash_url_name = 'products:product_trash_list'

    def get_queryset(self):
        queryset = Product.objects.all().order_by('id')
        if not self.request.user.is_superuser:
            queryset = queryset.filter(establishment=self.request.user.establishment).order_by('id')
        self.filter_form = self.get_filter_form()
        if self.filter_form and self.filter_form.is_valid():
            data = self.filter_form.cleaned_data
            if data.get("id"):
                queryset = queryset.filter(id__icontains=data["id"])

            if data.get("name"):
                queryset = queryset.filter(name__icontains=data["name"])

            if data.get("unit"):
                queryset = queryset.filter(unit=data["unit"])

            if data.get("is_active"):
                queryset = queryset.filter(is_active=data["is_active"])

            messages.info(self.request, "Se aplicaron los filtros")

        return queryset


class ProductCreateView(StandardCreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/form.html'
    success_url = reverse_lazy('products:product_create')
    title = 'Crear Producto'
    module_name = 'productos'
    list_url_name = 'products:product_list'


class ProductUpdateView(StandardUpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/form.html'
    title = 'Editar Producto'
    module_name = 'productos'
    list_url_name = 'products:product_list'

    def get_success_url(self):
        return reverse_lazy(
            'products:product_update',
            kwargs={'pk': self.object.pk}
        )
