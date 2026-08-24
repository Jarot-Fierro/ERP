from django.contrib import admin

from core.standard.admin import StandardAdmin
from customers.models import Customer


@admin.register(Customer)
class CustomerAdmin(StandardAdmin):
    list_display = (
        'id',
        'legal_name',
        'name',
        'tax_id',
        'country',
        'state_province',
        'city',
        'address',
        'zip_code',
        'phone',
        'email',
        'contact_name',
        'contact_role',
        'category',
        'payment_terms',
        'currency',
        'payment_method',
        'bank_account',
        'is_active',
        'created_at',
        'updated_at',
        'created_by',
    )

    search_fields = (
        'legal_name',
        'name',
        'tax_id',
        'country',
        'city',
        'email',
        'contact_name',
        'category',
    )

    list_filter = (
        'is_active',
        'country',
        'category',
        'currency',
        'payment_method',
        'created_at',
        'updated_at',
    )

    list_display_links = (
        'name',
    )

    ordering = (
        'name',
    )
