from django.contrib import admin

from core.standard.admin import StandardAdmin
from purchases.models import OrderStatus, PurchasesOrder, LinesPurchasesOrder


@admin.register(OrderStatus)
class OrderStatusAdmin(StandardAdmin):
    list_display = (
        'id',
        'name',
        'symbol',
        'is_active',
        'created_at',
        'updated_at',
        'created_by',
    )

    search_fields = (
        'name',
        'symbol',
    )

    list_filter = (
        'is_active',
        'created_at',
        'updated_at',
    )

    list_display_links = (
        'name',
    )

    ordering = (
        'name',
    )


@admin.register(PurchasesOrder)
class PurchasesOrderAdmin(StandardAdmin):
    list_display = (
        'id',
        'code',
        'supplier',
        'issue_date',
        'estimated_delivery_date',
        'created_at',
    )

    search_fields = (
        'supplier__name',
        'supplier__legal_name',
    )

    list_filter = (
        'supplier',
        'issue_date',
        'estimated_delivery_date',
        'is_active',
        'created_at',
        'updated_at',
    )

    list_display_links = (
        'id',
        'supplier',
        'code',
    )

    ordering = (
        '-id',
    )


@admin.register(LinesPurchasesOrder)
class LinesPurchasesOrderAdmin(StandardAdmin):
    list_display = (
        'id',
        'purchase_order',
        'position',
        'product',
        'quantity',
        'unit',
        'price',
        'currency',
        'received_quantity',
        'is_active',
        'created_at',
        'updated_at',
        'created_by',
    )

    search_fields = (
        'purchase_order__id',
        'product__name',
    )

    list_filter = (
        'purchase_order',
        'product',
        'unit',
        'currency',
        'is_active',
        'created_at',
        'updated_at',
    )

    list_display_links = (
        'id',
        'purchase_order',
    )

    ordering = (
        'purchase_order',
        'position',
    )
