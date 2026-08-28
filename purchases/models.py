from django.db import models
from django.utils import timezone

from core.standard.models import StandardModel, StandardModelEstablishment


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


class PurchasesOrder(StandardModelEstablishment):
    code = models.CharField(
        max_length=30,
        unique=True,
        editable=False,
        verbose_name='Código'
    )
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
        return self.code

    def save(self, *args, **kwargs):
        if not self.code:
            year = timezone.now().year
            last_order = (
                PurchasesOrder.objects
                .filter(code__startswith=f'OC-{year}-')
                .order_by('-id')
                .first()
            )
            if last_order:
                last_number = int(
                    last_order.code.split('-')[-1]
                ) + 1
            else:
                last_number = 1
            self.code = f'OC-{year}-{last_number:05d}'

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Orden de compra'
        verbose_name_plural = 'Ordenes de compra'
        ordering = ['id']


class LinesPurchasesOrder(StandardModelEstablishment):
    purchase_order = models.ForeignKey(
        PurchasesOrder,
        on_delete=models.CASCADE,
        verbose_name='Orden de compra',
        related_name='lines_purchases_order'
    )
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        verbose_name='Producto',
        related_name='lines_purchases_order_product'
    )
    position = models.PositiveIntegerField(
        default=1,
        verbose_name='Posición'
    )
    quantity = models.PositiveIntegerField(
        default=0,
        verbose_name='Cantidad'
    )
    unit = models.ForeignKey(
        'core.Unit',
        on_delete=models.CASCADE,
        verbose_name='Tipo de Unidad',
        related_name='lines_purchases_unit'
    )
    price = models.PositiveIntegerField(
        verbose_name='Precio'
    )
    currency = models.ForeignKey(
        'core.Currency',
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


class GoodsReceipStatus(StandardModelEstablishment):
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
