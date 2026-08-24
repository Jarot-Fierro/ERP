from django import forms


class SupplierFilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():

            value = self.data.get(field_name)

            if value:
                field.widget.attrs["class"] += " border-primary bg-light"

    id = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control form-control-sm",
                "placeholder": "ID",
            }
        ),
    )
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
        required=False,
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
        required=False,
    )
    country = forms.CharField(
        label='País',
        max_length=60,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Ingrese el país del proveedor'
            }
        ),
        required=False,
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
        required=False,
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
        required=False,
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
        required=False,
    )
    zip_code = forms.IntegerField(
        label='Código postal',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Ingrese el código postal'
            }
        ),
        required=False,
    )
    phone = forms.IntegerField(
        label='Teléfono',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Ingrese el teléfono del proveedor'
            }
        ),
        required=False,
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
        required=False,
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
        required=False,
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
        required=False,
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
        required=False,
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
        required=False,
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
        required=False,
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
        required=False,
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
        required=False,
    )
    is_active = forms.ChoiceField(
        choices=[
            ('True', 'Activo'),
            ('False', 'Inactivo')
        ],
        widget=forms.Select(
            attrs={
                'class': 'form-control form-control-sm form-select',
            }
        ),
        required=False,
    )
