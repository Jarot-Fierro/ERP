from django.db import models

from core.standard.models import StandardModel


class ProductType(StandardModel):
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
        verbose_name = 'Tipo de Producto'
        verbose_name_plural = 'Tipos de Productos'


class Product(StandardModel):
    name = models.CharField(
        max_length=200,
        verbose_name='Nombre'
    )
    description = models.TextField(
        verbose_name='Descripción'
    )
    unit = models.ForeignKey(
        'core.Unit',
        on_delete=models.CASCADE,
        verbose_name='Unidad',
        related_name='product_unit',
        null=True,
        blank=True,
    )
    product_type = models.ForeignKey(
        'products.ProductType',
        on_delete=models.CASCADE,
        verbose_name='Tipo de Product',
        related_name='product_product_type',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name
