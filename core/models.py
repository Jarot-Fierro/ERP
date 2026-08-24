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
    logo = models.ImageField(upload_to='establecimientos/logos/&Y', blank=True, null=True, verbose_name='Logo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Establecimiento'
        verbose_name_plural = 'Establecimientos'
