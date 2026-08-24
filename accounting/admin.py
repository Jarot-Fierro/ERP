from django.contrib import admin

from accounting.models import AccountNature, AccountGroup, AccountType, AccountAccount
from core.standard.admin import StandardAdmin


@admin.register(AccountNature)
class AccountNatureAdmin(StandardAdmin):
    list_display = (
        'id',
        'name',
        'symbol',
        'effect_on_balance',
        'is_active',
        'created_at',
        'updated_at',
        'created_by',
    )

    search_fields = (
        'name',
        'symbol',
        'effect_on_balance',
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


@admin.register(AccountGroup)
class AccountGroupAdmin(StandardAdmin):
    list_display = (
        'id',
        'name',
        'code_prefix',
        'description',
        'is_active',
        'created_at',
        'updated_at',
        'created_by',
    )

    search_fields = (
        'name',
        'code_prefix',
        'description',
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


@admin.register(AccountType)
class AccountTypeAdmin(StandardAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'is_active',
        'created_at',
        'updated_at',
        'created_by',
    )

    search_fields = (
        'name',
        'description',
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


@admin.register(AccountAccount)
class AccountAccountAdmin(StandardAdmin):
    list_display = (
        'id',
        'name',
        'code',
        'account_type',
        'account_group',
        'account_nature',
        'currency',
        'country',
        'is_control',
        'parent',
        'is_active',
        'created_at',
        'updated_at',
        'created_by',
    )

    search_fields = (
        'name',
        'code',
        'description',
        'account_type__name',
        'account_group__name',
        'account_nature__name',
    )

    list_filter = (
        'account_type',
        'account_group',
        'account_nature',
        'currency',
        'country',
        'is_control',
        'is_active',
        'created_at',
        'updated_at',
    )

    list_display_links = (
        'name',
    )

    ordering = (
        'code',
        'name',
    )
