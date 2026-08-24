from django import forms

from materials.models import Material, Unit, MaterialType


class MaterialForm(forms.ModelForm):
    name = forms.CharField(
        label='Nombre',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Ingrese el nombre del material'
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
                'placeholder': 'Ingrese una breve descripción del material',
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
    material_type = forms.ModelChoiceField(
        label='Tipo de Material',
        queryset=MaterialType.objects.all(),
        empty_label='- Seleccione un tipo de material -',
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
        model = Material
        fields = [
            'name',
            'description',
            'unit',
            'material_type',
            'is_active',
        ]
