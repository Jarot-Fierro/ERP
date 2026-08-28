from django.contrib import admin

from core.standard.admin import StandardAdmin
from .models import Product, ProductType


@admin.register(Product)
class ProductAdmin(StandardAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'unit',
        'product_type',
        'is_active',
        'created_at',
        'updated_at',
        'created_by',
    )

    search_fields = (
        'name',
        'description',
        'unit',
        'product_type',
    )

    list_filter = (
        'product_type',
        'unit',
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


@admin.register(ProductType)
class ProductTypeAdmin(StandardAdmin):
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
