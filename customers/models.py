from django.db import models

from core.standard.models import StandardModel


# Create your models here.
class Customer(StandardModel):
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
        related_name='customer_country',
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
    currency = models.CharField(
        max_length=150, verbose_name="Moneda"
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
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['name']
