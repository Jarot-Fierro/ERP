from django.contrib import messages
from django.db import transaction
from django.shortcuts import redirect
from django.urls import reverse_lazy

from core.standard.views import (
    StandardListView,
    StandardCreateView,
    StandardUpdateView,
    StandardDetailView,
)
from purchases.forms import PurchasesOrderForm, LinesPurchasesOrderFormSet
from purchases.models import PurchasesOrder


class PurchaseOrderListView(StandardListView):
    model = PurchasesOrder
    template_name = 'purchases/list.html'
    title = 'Listado de Ordenes de Compra'
    module_name = 'ordenes de compra'
    filter_form_class = None
    export_fields_csv = None
    list_url_name = 'purchases:purchase_list'
    create_url_name = 'purchases:purchase_create'
    update_url_name = 'purchases:purchase_update'
    detail_url_name = 'purchases:purchase_detail'


class PurchaseOrderCreateView(StandardCreateView):
    model = PurchasesOrder
    form_class = PurchasesOrderForm
    template_name = 'purchases/form.html'
    success_url = reverse_lazy('purchases:purchase_list')
    title = 'Crear Orden de Compra'
    module_name = 'orden de compra'
    list_url_name = 'purchases:purchase_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'formset' not in context:
            if self.request.POST:
                context['formset'] = LinesPurchasesOrderFormSet(self.request.POST, self.request.FILES)
            else:
                context['formset'] = LinesPurchasesOrderFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            with transaction.atomic():
                if hasattr(form.instance, 'establishment') and not form.instance.establishment:
                    form.instance.establishment = getattr(self.request.user, 'establishment', None)
                if hasattr(form.instance, 'created_by') and not form.instance.created_by:
                    form.instance.created_by = self.request.user

                self.object = form.save()
                formset.instance = self.object
                lines = formset.save(commit=False)
                for i, line in enumerate(lines, start=1):
                    if hasattr(line, 'created_by') and not line.created_by:
                        line.created_by = self.request.user
                    if hasattr(line, 'establishment') and not line.establishment:
                        line.establishment = getattr(self.request.user, 'establishment', None)
                    if getattr(line, 'received_quantity', None) is None:
                        line.received_quantity = 0
                    if not getattr(line, 'position', None):
                        line.position = i
                    line.save()
                for obj in formset.deleted_objects:
                    obj.delete()
                formset.save_m2m()

            messages.success(self.request, f'{self.model._meta.verbose_name} creado correctamente.')
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class PurchaseOrderUpdateView(StandardUpdateView):
    model = PurchasesOrder
    form_class = PurchasesOrderForm
    template_name = 'purchases/form.html'
    success_url = reverse_lazy('purchases:purchase_list')
    title = 'Editar Orden de Compra'
    module_name = 'orden de compra'
    list_url_name = 'purchases:purchase_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'formset' not in context:
            if self.request.POST:
                context['formset'] = LinesPurchasesOrderFormSet(
                    self.request.POST, self.request.FILES, instance=self.object
                )
            else:
                context['formset'] = LinesPurchasesOrderFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            with transaction.atomic():
                if hasattr(form.instance, 'updated_by'):
                    form.instance.updated_by = self.request.user

                self.object = form.save()
                formset.instance = self.object
                lines = formset.save(commit=False)
                for i, line in enumerate(lines, start=1):
                    if hasattr(line, 'created_by') and not line.created_by:
                        line.created_by = self.request.user
                    if hasattr(line, 'updated_by'):
                        line.updated_by = self.request.user
                    if hasattr(line, 'establishment') and not line.establishment:
                        line.establishment = getattr(self.request.user, 'establishment', None)
                    if getattr(line, 'received_quantity', None) is None:
                        line.received_quantity = 0
                    if not getattr(line, 'position', None):
                        line.position = i
                    line.save()
                for obj in formset.deleted_objects:
                    obj.delete()
                formset.save_m2m()

            messages.success(self.request, f'{self.model._meta.verbose_name} actualizado correctamente.')
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class PurchaseOrderDetailView(StandardDetailView):
    model = PurchasesOrder
    template_name = 'purchases/detail.html'
    title = 'Detalle de Orden de Compra'
    module_name = 'orden de compra'
    list_url_name = 'purchases:purchase_list'
    update_url_name = 'purchases:purchase_update'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lines = self.object.lines_purchases_order.select_related(
            'material', 'unit_material', 'currency'
        ).order_by('position', 'id')

        # Calculamos subtotal para cada línea y el total general
        total_amount = 0
        total_quantity = 0
        total_received = 0
        lines_with_subtotal = []
        for line in lines:
            subtotal = (line.quantity or 0) * (line.price or 0)
            total_amount += subtotal
            total_quantity += line.quantity or 0
            total_received += line.received_quantity or 0
            lines_with_subtotal.append({
                'line': line,
                'subtotal': subtotal
            })

        context['lines_data'] = lines_with_subtotal
        context['total_amount'] = total_amount
        context['total_quantity'] = total_quantity
        context['total_received'] = total_received
        context['update_url_name'] = self.update_url_name
        context['list_url_name'] = self.list_url_name
        return context
