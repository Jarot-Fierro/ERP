from django.contrib import messages
from django.urls import reverse_lazy

from core.standard.views import StandardListView, StandardCreateView, StandardUpdateView
from suppliers.filters import SupplierFilterForm
from suppliers.forms import SupplierForm
from suppliers.models import Supplier


class SupplierListView(StandardListView):
    model = Supplier
    template_name = 'suppliers/list.html'
    title = 'Listado de Proovedores'
    module_name = 'proveedores'
    filter_form_class = SupplierFilterForm
    export_fields_csv = [
        'id',
        'id_supplier',
        'legal_name',
        'name',
        'tax_id',
        'country',
        'state_province',
        'city',
        'address',
        'zip_code',
        'phone',
        'email',
        'contact_name',
        'contact_role',
        'category',
        'payment_terms',
        'currency',
        'payment_method',
        'bank_account',
        'status',
        'created_at',
        'updated_at',
        'created_by',
    ]
    list_url_name = 'suppliers:supplier_list'
    create_url_name = 'suppliers:supplier_create'
    update_url_name = 'suppliers:supplier_update'
    delete_url_name = None
    trash_url_name = 'suppliers:supplier_trash_list'

    def get_queryset(self):
        queryset = Supplier.objects.all().order_by('id')
        if not self.request.user.is_superuser:
            queryset = queryset.filter(establecimiento=self.request.user.establecimiento).order_by('id')
        self.filter_form = self.get_filter_form()
        if self.filter_form and self.filter_form.is_valid():
            data = self.filter_form.cleaned_data
            if data.get("id"):
                queryset = queryset.filter(id__icontains=data["id"])

            if data.get("legal_name"):
                queryset = queryset.filter(legal_name__icontains=data["legal_name"])

            if data.get("name"):
                queryset = queryset.filter(name__icontains=data["name"])

            if data.get("tax_id"):
                queryset = queryset.filter(tax_id__icontains=data["tax_id"])

            if data.get("country"):
                queryset = queryset.filter(country__icontains=data["country"])

            if data.get("state_province"):
                queryset = queryset.filter(state_province__icontains=data["state_province"])

            if data.get("city"):
                queryset = queryset.filter(city__icontains=data["city"])

            if data.get("address"):
                queryset = queryset.filter(address__icontains=data["address"])

            if data.get("zip_code"):
                queryset = queryset.filter(zip_code=data["zip_code"])

            if data.get("phone"):
                queryset = queryset.filter(phone=data["phone"])

            if data.get("email"):
                queryset = queryset.filter(email__icontains=data["email"])

            if data.get("contact_name"):
                queryset = queryset.filter(contact_name__icontains=data["contact_name"])

            if data.get("contact_role"):
                queryset = queryset.filter(contact_role__icontains=data["contact_role"])

            if data.get("category"):
                queryset = queryset.filter(category__icontains=data["category"])

            if data.get("payment_terms"):
                queryset = queryset.filter(payment_terms__icontains=data["payment_terms"])

            if data.get("currency"):
                queryset = queryset.filter(currency__icontains=data["currency"])

            if data.get("payment_method"):
                queryset = queryset.filter(payment_method__icontains=data["payment_method"])

            if data.get("bank_account"):
                queryset = queryset.filter(bank_account__icontains=data["bank_account"])

            messages.info(self.request, "Se aplicaron los filtros")

        return queryset


class SupplierCreateView(StandardCreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'suppliers/form.html'
    success_url = reverse_lazy('suppliers:supplier_create')
    title = 'Crear Proovedores'
    module_name = 'proveedores'
    list_url_name = 'suppliers:supplier_list'


class SupplierUpdateView(StandardUpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'suppliers/form.html'
    title = 'Editar Proovedores'
    module_name = 'proveedores'
    list_url_name = 'suppliers:supplier_list'

    def get_success_url(self):
        return reverse_lazy(
            'suppliers:supplier_update',
            kwargs={'pk': self.object.pk}
        )
