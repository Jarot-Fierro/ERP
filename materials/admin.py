from django.contrib import admin

from core.standard.admin import StandardAdmin
from .models import Material, Unit, MaterialType


@admin.register(Material)
class MaterialAdmin(StandardAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'unit',
        'material_type',
        'is_active',
        'created_at',
        'updated_at',
        'created_by',
    )

    search_fields = (
        'name',
        'description',
        'unit',
        'material_type',
    )

    list_filter = (
        'material_type',
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


@admin.register(Unit)
class UnitAdmin(StandardAdmin):
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


@admin.register(MaterialType)
class MaterialTypeAdmin(StandardAdmin):
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
