from django.contrib import admin

from users.models import User, Role


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_staff'
    )
    list_filter = (
        'is_staff',
        'is_superuser',
        'is_active'
    )
    search_fields = (
        'username',
        'email',
        'first_name',
        'last_name'
    )


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'customers',
        'suppliers',
        'materials',
        'purchases',
        'sales',
        'inventory',
        'accounting',
        'reporting'
    )
