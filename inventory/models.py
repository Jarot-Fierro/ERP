from django.db import models

from core.standard.models import StandardModel, StandardModelEstablishment


class MovementType(StandardModel):
    name = models.CharField(
        max_length=200,
        verbose_name='Nombre'
    )
    symbol = models.CharField(
        max_length=50,
        verbose_name='Simbolo'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo de Movimiento'
        verbose_name_plural = 'Tipos de Movimientos'


class LocationInventory(StandardModelEstablishment):
    name = models.CharField(
        max_length=200,
        verbose_name='Nombre'
    )
    code = models.CharField(
        max_length=200,
        verbose_name='Código'
    )
    main_location = models.BooleanField(
        default=True,
        verbose_name='Es la ubicación principal'
    )
    location = models.TextField(
        blank=True,
        verbose_name='Ubicación'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ubicación de Inventario'
        verbose_name_plural = 'Ubicaciones de Inventario'


class InventoryMovements(StandardModelEstablishment):
    location = models.ForeignKey(
        'inventory.LocationInventory',
        on_delete=models.CASCADE,
        verbose_name='Ubicación',
        related_name='inventory_location'
    )
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        verbose_name='Producto',
        related_name='inventory_product'
    )
    unit_type = models.ForeignKey(
        'core.Unit',
        on_delete=models.CASCADE,
        verbose_name='Tipo de Unidad',
        related_name='inventory_unit_type'
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Cantidad'
    )
    price = models.PositiveIntegerField(
        verbose_name='Precio'
    )
    currency = models.ForeignKey(
        'core.Currency',
        on_delete=models.CASCADE,
        verbose_name='Moneda',
        null=True,
        blank=True,
        related_name='inventory_currency'
    )
    movement_type = models.ForeignKey(
        'inventory.MovementType',
        on_delete=models.CASCADE,
        verbose_name='Tipo de Movimiento',
        related_name='inventory_movement_type'
    )

    def __str__(self):
        return f"{self.product} - {self.location} - {self.unit_type}"

    class Meta:
        verbose_name = 'Movimiento de Inventario'
        verbose_name_plural = 'Movimientos de Inventario'
