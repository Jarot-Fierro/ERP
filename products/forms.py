from django import forms

from core.models import Unit
from products.models import Product, ProductType


class ProductForm(forms.ModelForm):
    name = forms.CharField(
        label='Nombre',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Ingrese el nombre del producto'
            }
        ),
        required=True,
    )
    description = forms.CharField(
        label='Descripción',
        max_length=255,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Ingrese una breve descripción del producto',
                'rows': 3
            }
        ),
        required=False,
    )
    unit = forms.ModelChoiceField(
        label='Unidad',
        queryset=Unit.objects.all(),
        empty_label='- Seleccione una unidad -',
        widget=forms.Select(
            attrs={
                'class': 'form-control form-select',
            }
        ),
        required=True,
    )
    product_type = forms.ModelChoiceField(
        label='Tipo de Product',
        queryset=ProductType.objects.all(),
        empty_label='- Seleccione un tipo de producto -',
        widget=forms.Select(
            attrs={
                'class': 'form-control form-select',
            }
        ),
        required=True,
    )
    is_active = forms.BooleanField(
        label='¿Activo?',
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'type': 'checkbox',
                'role': 'switch',
            }
        ),
        required=False,
    )

    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'unit',
            'product_type',
            'is_active',
        ]
