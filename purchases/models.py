from django.db import models

from core.standard.models import StandardModel


class OrderStatus(StandardModel):
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
        verbose_name = 'Estado de Orden'
        verbose_name_plural = 'Estados de Ordenes'
        ordering = ['name']


class PurchasesOrder(StandardModel):
    supplier = models.ForeignKey(
        'suppliers.Supplier',
        on_delete=models.CASCADE,
        verbose_name='Proveedor',
        related_name='supplier_order'
    )
    issue_date = models.DateField(
        auto_now_add=True,
        verbose_name='Fecha de Emisión'
    )
    estimated_delivery_date = models.DateField(
        verbose_name='Fecha Estimada de Entrega'
    )

    def __str__(self):
        return f"{str(self.id)}"

    class Meta:
        verbose_name = 'Orden de compra'
        verbose_name_plural = 'Ordenes de compra'
        ordering = ['id']


class LinesPurchasesOrder(StandardModel):
    purchase_order = models.ForeignKey(
        PurchasesOrder,
        on_delete=models.CASCADE,
        verbose_name='Orden de compra',
        related_name='lines_purchases_order'
    )
    material = models.ForeignKey(
        'materials.Material',
        on_delete=models.CASCADE,
        verbose_name='Material',
        related_name='lines_purchases_order_material'
    )
    position = models.PositiveIntegerField(
        default=1,
        verbose_name='Posición'
    )
    quantity = models.PositiveIntegerField(
        default=0,
        verbose_name='Cantidad'
    )
    unit_material = models.ForeignKey(
        'materials.Unit',
        on_delete=models.CASCADE,
        verbose_name='Unidad de Material',
        related_name='lines_purchases_unit_material'
    )
    price = models.PositiveIntegerField(
        verbose_name='Precio'
    )
    currency = models.ForeignKey(
        'suppliers.Currency',
        on_delete=models.CASCADE,
        verbose_name='Moneda',
        related_name='lines_purchases_currency'
    )
    received_quantity = models.PositiveIntegerField(
        default=0,
        verbose_name='Cantidad Recibida',
    )

    def __str__(self):
        return f"{str(self.id)}"

    class Meta:
        verbose_name = 'Liena de orden de compra'
        verbose_name_plural = 'Líneas de ordenes de compra'
        ordering = ['id']


class GoodsReceipStatus(StandardModel):
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
        verbose_name = 'Estado de recepción de Mercancía'
        verbose_name_plural = 'Estados de recepción de Mercancías'
        ordering = ['name']
