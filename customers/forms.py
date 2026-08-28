from django import forms

from core.models import Country
from customers.models import Customer


class CustomerForm(forms.ModelForm):
    legal_name = forms.CharField(
        label='Nombre legal',
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Ingrese el nombre legal del proveedor'
            }
        ),
        required=False,
    )
    name = forms.CharField(
        label='Nombre',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Ingrese el nombre del proveedor'
            }
        ),
        required=True,
    )
    tax_id = forms.CharField(
        label='RUC/CIF',
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Ingrese el RUC/CIF del proveedor'
            }
        ),
        required=True,
    )
    country = forms.ModelChoiceField(
        label='País',
        queryset=Country.objects.all(),
        empty_label='Seleccione un país',
        widget=forms.Select(
            attrs={
                'class': 'form-control form-control-sm form-select',
            }
        ),
        required=True,
    )
    state_province = forms.CharField(
        label='Estado/Provincia',
        max_length=60,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Ingrese el estado/provincia del proveedor'
            }
        ),
        required=True,
    )
    city = forms.CharField(
        label='Ciudad',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Ingrese la ciudad del proveedor'
            }
        ),
        required=True,
    )
    address = forms.CharField(
        label='Dirección',
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Ingrese la dirección del proveedor'
            }
        ),
        required=True,
    )
    zip_code = forms.IntegerField(
        label='Código postal',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Ingrese el código postal'
            }
        ),
        required=True,
    )
    phone = forms.IntegerField(
        label='Teléfono',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Ingrese el teléfono del proveedor'
            }
        ),
        required=True,
    )
    email = forms.EmailField(
        label='Correo electrónico',
        max_length=150,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Ingrese el correo electrónico del proveedor'
            }
        ),
        required=True,
    )
    contact_name = forms.CharField(
        label='Nombre de contacto',
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Ingrese el nombre de contacto'
            }
        ),
        required=True,
    )
    contact_role = forms.CharField(
        label='Rol de contacto',
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Ingrese el rol del contacto'
            }
        ),
        required=True,
    )
    category = forms.CharField(
        label='Categoría',
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Ingrese la categoría del proveedor'
            }
        ),
        required=True,
    )
    payment_terms = forms.CharField(
        label='Condiciones de pago',
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Ingrese las condiciones de pago'
            }
        ),
        required=True,
    )
    currency = forms.CharField(
        label='Moneda',
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Ingrese la moneda'
            }
        ),
        required=True,
    )
    payment_method = forms.CharField(
        label='Método de pago',
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Ingrese el método de pago'
            }
        ),
        required=True,
    )
    bank_account = forms.CharField(
        label='Cuenta bancaria',
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Ingrese la cuenta bancaria'
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
        model = Customer
        fields = [
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
            'is_active',
        ]
