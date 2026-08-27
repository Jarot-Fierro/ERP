from django.db import models

from core.standard.models import StandardModel


class Country(StandardModel):
    name = models.CharField(max_length=60, verbose_name="País")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"
        ordering = ['name']


class Currency(StandardModel):
    name = models.CharField(max_length=60, verbose_name="País")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Moneda"
        verbose_name_plural = "Monedas"
        ordering = ['name']


# Create your models here.
class Supplier(StandardModel):
    legal_name = models.CharField(
        max_length=150, blank=True,
        verbose_name="Nombre legal"
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Nombre"
    )
    tax_id = models.CharField(
        max_length=30,
        verbose_name="RUC/CIF"
    )
    country = models.ForeignKey(
        'suppliers.Country',
        on_delete=models.CASCADE,
        related_name='supplier_country',
        verbose_name="País"
    )
    state_province = models.CharField(
        max_length=60,
        verbose_name="Estado/Provincia"
    )
    city = models.CharField(
        max_length=100,
        verbose_name="Ciudad"
    )
    address = models.CharField(
        max_length=150,
        verbose_name="Dirección"
    )
    zip_code = models.IntegerField(
        verbose_name="Código postal"
    )
    phone = models.IntegerField(
        verbose_name="Teléfono"
    )
    email = models.EmailField(
        max_length=150,
        verbose_name="Correo electrónico"
    )
    contact_name = models.CharField(
        max_length=150,
        verbose_name="Nombre de contacto"
    )
    contact_role = models.CharField(
        max_length=150,
        verbose_name="Rol de contacto"
    )
    category = models.CharField(
        max_length=150,
        verbose_name="Categoría"
    )
    payment_terms = models.CharField(
        max_length=150,
        verbose_name="Condiciones de pago"
    )
    currency = models.ForeignKey(
        'suppliers.Currency',
        on_delete=models.CASCADE,
        verbose_name="Moneda",
        related_name='supplier_currency'
    )
    payment_method = models.CharField(
        max_length=150,
        verbose_name="Método de pago"
    )
    bank_account = models.CharField(
        max_length=150,
        verbose_name="Cuenta bancaria"
    )

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ['name']

    def __str__(self):
        return self.name
