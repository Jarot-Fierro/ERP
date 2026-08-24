from django.db import models

from core.standard.models import StandardModel


class AccountNature(StandardModel):
    name = models.CharField(
        max_length=100,
        verbose_name='Nombre'
    )
    symbol = models.CharField(
        max_length=50,
        verbose_name='Simbolo'
    )
    effect_on_balance = models.CharField(
        max_length=100,
        verbose_name='Efecto en el Balance'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Naturaleza de Cuenta'
        verbose_name_plural = 'Naturalezas de Cuenta'
        ordering = ['name']


class AccountGroup(StandardModel):
    name = models.CharField(
        max_length=100,
        verbose_name='Nombre'
    )
    code_prefix = models.CharField(
        max_length=10,
        verbose_name='Prefijo de Código'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Descripción'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Grupo de Cuentas'
        verbose_name_plural = 'Grupos de Cuentas'
        ordering = ['name']


class AccountType(StandardModel):
    name = models.CharField(
        max_length=100,
        verbose_name='Nombre'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Descripción'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo de Cuenta'
        verbose_name_plural = 'Tipos de Cuenta'
        ordering = ['name']


class AccountAccount(StandardModel):
    name = models.CharField(
        max_length=100,
        verbose_name='Nombre'
    )
    code = models.CharField(
        max_length=20,
        verbose_name='Código'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Descripción'
    )
    account_type = models.ForeignKey(
        'accounting.AccountType',
        on_delete=models.CASCADE,
        verbose_name='Tipo de Cuenta',
        related_name='account_type',
        null=True,
    )
    account_group = models.ForeignKey(
        'accounting.AccountGroup',
        on_delete=models.CASCADE,
        verbose_name='Grupo de Cuenta',
        related_name='account_group',
    )
    account_nature = models.ForeignKey(
        'accounting.AccountNature',
        on_delete=models.CASCADE,
        verbose_name='Naturaleza de Cuenta',
        related_name='account_nature',
    )
    currency = models.ForeignKey(
        'suppliers.Currency',
        on_delete=models.CASCADE,
        verbose_name='Moneda',
        related_name='account_currency',
    )
    country = models.ForeignKey(
        'suppliers.Country',
        on_delete=models.CASCADE,
        verbose_name='País',
        related_name='account_country',
    )
    is_control = models.BooleanField(
        default=False,
        verbose_name='Es una Cuenta de Control',
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        verbose_name='Cuenta Padre',
        related_name='account_parent',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cuenta'
        verbose_name_plural = 'Cuentas'
        ordering = ['name']
