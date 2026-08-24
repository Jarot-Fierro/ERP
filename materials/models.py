from django.db import models

from core.standard.models import StandardModel


class Unit(StandardModel):
    name = models.CharField(
        unique=True,
        max_length=200,
        verbose_name='Nombre'
    )
    symbol = models.CharField(
        unique=True,
        max_length=200,
        verbose_name='Simbolo'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Unidad'
        verbose_name_plural = 'Unidades'


class MaterialType(StandardModel):
    name = models.CharField(
        unique=True,
        max_length=200,
        verbose_name='Nombre'
    )
    symbol = models.CharField(
        unique=True,
        max_length=200,
        verbose_name='Simbolo'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo de Material'
        verbose_name_plural = 'Tipos de Materiales'


class Material(StandardModel):
    name = models.CharField(
        max_length=200,
        verbose_name='Nombre'
    )
    description = models.TextField(
        verbose_name='Descripción'
    )
    unit = models.ForeignKey(
        'materials.Unit',
        on_delete=models.CASCADE,
        verbose_name='Unidad',
        related_name='unit',
        null=True,
        blank=True,
    )
    material_type = models.ForeignKey(
        'materials.MaterialType',
        on_delete=models.CASCADE,
        verbose_name='Tipo de Material',
        related_name='unit',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materiales'

    def __str__(self):
        return self.name
