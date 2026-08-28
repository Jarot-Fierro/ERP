from django import forms


class ProductFilterForm(forms.Form):
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
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Ingrese el nombre del material'
            }
        ),
        required=False,
    )
    unit = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Ingrese la unidad del material'
            }
        ),
        required=False,
    )
    material_type = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Ingrese el tipo de material'
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
