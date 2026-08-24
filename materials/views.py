from django.contrib import messages
from django.urls import reverse_lazy

from core.standard.views import StandardListView, StandardCreateView, StandardUpdateView
from materials.filters import MaterialFilterForm
from materials.forms import MaterialForm
from materials.models import Material


class MaterialListView(StandardListView):
    model = Material
    template_name = 'materials/list.html'
    title = 'Listado de Materiales'
    module_name = 'materiales'
    filter_form_class = MaterialFilterForm
    export_fields_csv = ['id', 'name', 'unit', 'material_type', 'is_active']
    list_url_name = 'materials:material_list'
    create_url_name = 'materials:material_create'
    update_url_name = 'materials:material_update'
    delete_url_name = None
    trash_url_name = 'materials:material_trash_list'

    def get_queryset(self):
        queryset = Material.objects.all().order_by('id')
        if not self.request.user.is_superuser:
            queryset = queryset.filter(establecimiento=self.request.user.establecimiento).order_by('id')
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


class MaterialCreateView(StandardCreateView):
    model = Material
    form_class = MaterialForm
    template_name = 'materials/form.html'
    success_url = reverse_lazy('materials:material_create')
    title = 'Crear Material'
    module_name = 'materiales'
    list_url_name = 'materials:material_list'


class MaterialUpdateView(StandardUpdateView):
    model = Material
    form_class = MaterialForm
    template_name = 'materials/form.html'
    title = 'Editar Material'
    module_name = 'materiales'
    list_url_name = 'materials:material_list'

    def get_success_url(self):
        return reverse_lazy(
            'materials:material_update',
            kwargs={'pk': self.object.pk}
        )
