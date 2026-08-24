from django.contrib import admin

from core.standard.admin import StandardAdmin
from inventory.models import MovementType, LocationInventory, InventoryMovements


@admin.register(MovementType)
class MovementTypeAdmin(StandardAdmin):
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


@admin.register(LocationInventory)
class LocationInventoryAdmin(StandardAdmin):
    list_display = (
        'id',
        'name',
        'code',
        'main_location',
        'location',
        'is_active',
        'created_at',
        'updated_at',
        'created_by',
    )

    search_fields = (
        'name',
        'code',
        'location',
    )

    list_filter = (
        'main_location',
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


@admin.register(InventoryMovements)
class InventoryMovementsAdmin(StandardAdmin):
    list_display = (
        'id',
        'location',
        'material',
        'unit_type',
        'quantity',
        'movement_type',
        'is_active',
        'created_at',
        'updated_at',
        'created_by',
    )

    search_fields = (
        'location__name',
        'material__name',
        'unit_type__name',
        'movement_type__name',
    )

    list_filter = (
        'location',
        'material',
        'unit_type',
        'movement_type',
        'is_active',
        'created_at',
        'updated_at',
    )

    list_display_links = (
        'id',
        'location',
    )

    ordering = (
        '-created_at',
    )
