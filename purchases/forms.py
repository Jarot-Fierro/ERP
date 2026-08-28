from django import forms
from django.forms import inlineformset_factory

from core.models import Unit, Currency
from inventory.models import LocationInventory
from organization.models import Department
from products.models import Product
from purchases.models import PurchasesOrder, LinesPurchasesOrder as LinesPurchasesOrderModel
from suppliers.models import Supplier


class PurchasesOrderForm(forms.ModelForm):
    supplier = forms.ModelChoiceField(
        label='Proveedor',
        queryset=Supplier.objects.all(),
        empty_label='Seleccione un proveedor',
        widget=forms.Select(
            attrs={
                'class': 'form-select form-select-sm',
                'id': 'id_supplier'
            }
        ),
        required=True,
    )
    department = forms.ModelChoiceField(
        label='Departamento',
        queryset=Department.objects.all(),
        empty_label='Seleccione un departamento: ',
        widget=forms.Select(
            attrs={
                'class': 'tom-select',
                'id': 'id_department'
            }
        ),
        required=True,
    )
    inventory = forms.ModelChoiceField(
        label='Bodega',
        queryset=LocationInventory.objects.all(),
        empty_label='Seleccione una Bodega',
        widget=forms.Select(
            attrs={
                'class': 'tom-select',
                'id': 'id_supplier'
            }
        ),
        required=True,
    )
    estimated_delivery_date = forms.DateField(
        label='Fecha de Entrega',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control form-control-sm flatpickr-input',
                'type': 'date',
                'placeholder': 'Ingrese la fecha de entrega'
            }
        ),
        required=True,
    )

    class Meta:
        model = PurchasesOrder
        fields = [
            'supplier',
            'estimated_delivery_date',
            'department',
            'inventory',
        ]


class LinesPurchasesOrderForm(forms.ModelForm):
    product = forms.ModelChoiceField(
        label='Producto',
        queryset=Product.objects.all(),
        empty_label='Seleccione un producto',
        widget=forms.Select(
            attrs={
                'class': 'tom-select',
            }
        ),
        required=True,
    )
    quantity = forms.IntegerField(
        label='Cantidad',
        min_value=1,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Ingrese cantidad'
            }
        ),
        required=True,
    )
    unit = forms.ModelChoiceField(
        label='Unidad de Medida',
        queryset=Unit.objects.all(),
        empty_label='Seleccione una medida',
        widget=forms.Select(
            attrs={
                'class': 'form-select form-select-sm',
            }
        ),
        required=True,
    )
    price = forms.IntegerField(
        label='Precio',
        min_value=0,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Ingrese precio'
            }
        ),
        required=True,
    )

    currency = forms.ModelChoiceField(
        label='Moneda',
        queryset=Currency.objects.all(),
        empty_label='Seleccione una moneda',
        widget=forms.Select(
            attrs={
                'class': 'form-select form-select-sm',
            }
        ),
        required=True,
    )

    class Meta:
        model = LinesPurchasesOrderModel
        fields = [
            'product',
            'quantity',
            'unit',
            'price',
            'currency',
        ]


LinesPurchasesOrder = LinesPurchasesOrderModel

LinesPurchasesOrderFormSet = inlineformset_factory(
    PurchasesOrder,
    LinesPurchasesOrderModel,
    form=LinesPurchasesOrderForm,
    extra=1,
    can_delete=True
)
