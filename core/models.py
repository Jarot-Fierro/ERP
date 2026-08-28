from django.db import models

from core.standard.models import StandardModel


class Establishment(StandardModel):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    run = models.CharField(max_length=20, unique=True, verbose_name='RUN')
    alias = models.CharField(max_length=20, unique=True, null=True, blank=True, verbose_name='Alias')
    area = models.CharField(max_length=100, blank=True, null=True, verbose_name='Área')
    address = models.TextField(blank=True, null=True, verbose_name='Dirección')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Teléfono')
    anexo = models.CharField(max_length=20, blank=True, null=True, verbose_name='Anexo')
    email = models.EmailField(blank=True, null=True, verbose_name='Correo')
    logo = models.ImageField(upload_to='establecimientos/logos/%Y', blank=True, null=True, verbose_name='Logo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Establecimiento'
        verbose_name_plural = 'Establecimientos'


class Unit(StandardModel):
    name = models.CharField(
        unique=True,
        max_length=200,
        verbose_name='Nombre'
    )
    symbol = models.CharField(
        unique=True,
        max_length=200,
        verbose_name='Simbolo'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Unidad'
        verbose_name_plural = 'Unidades'
        ordering = ['name']


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
    symbol = models.CharField(max_length=20, verbose_name="Simbolo")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Moneda"
        verbose_name_plural = "Monedas"
        ordering = ['name']
