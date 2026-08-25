from django import forms
from django.forms import inlineformset_factory

from materials.models import Material, Unit
from purchases.models import PurchasesOrder, LinesPurchasesOrder as LinesPurchasesOrderModel
from suppliers.models import Supplier, Currency


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
    estimated_delivery_date = forms.DateField(
        label='Fecha de Entrega',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control form-control-sm',
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
        ]


class LinesPurchasesOrderForm(forms.ModelForm):
    material = forms.ModelChoiceField(
        label='Material',
        queryset=Material.objects.all(),
        empty_label='Seleccione un material',
        widget=forms.Select(
            attrs={
                'class': 'form-select form-select-sm',
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
    unit_material = forms.ModelChoiceField(
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
            'material',
            'quantity',
            'unit_material',
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
