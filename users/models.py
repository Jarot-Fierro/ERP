from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Nombre de Usuario')
    password = models.CharField(
        max_length=128,
        verbose_name='Contraseña'
    )
    role = models.ForeignKey(
        'users.Role',
        on_delete=models.CASCADE,
        verbose_name='Rol',
        related_name='role',
        null=True,
        blank=True,
    )
    establecimiento = models.ForeignKey(
        'core.Establishment',
        on_delete=models.CASCADE,
        verbose_name='Establecimiento',
        related_name='establishment',
        null=True,
        blank=True,
    )

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['username']


class Role(models.Model):
    PERMISION_CHOICES = [
        (0, 'Sin Acceso'),
        (1, 'Solo Ver'),
        (2, 'Crear y Modificar'),
        (3, 'Administrador')
    ]

    name = models.CharField(
        max_length=200,
        verbose_name='Nombre del Rol')
    customers = models.IntegerField(
        choices=PERMISION_CHOICES,
        default=0,
        verbose_name='Clientes'
    )
    suppliers = models.IntegerField(
        choices=PERMISION_CHOICES,
        default=0,
        verbose_name='Proveedores'
    )
    materials = models.IntegerField(
        choices=PERMISION_CHOICES,
        default=0,
        verbose_name='Materiales'
    )
    purchases = models.IntegerField(
        choices=PERMISION_CHOICES,
        default=0,
        verbose_name='Compras'
    )
    sales = models.IntegerField(
        choices=PERMISION_CHOICES,
        default=0,
        verbose_name='Ventas'
    )
    inventory = models.IntegerField(
        choices=PERMISION_CHOICES,
        default=0,
        verbose_name='Inventario'
    )
    accounting = models.IntegerField(
        choices=PERMISION_CHOICES,
        default=0,
        verbose_name='Contabilidad'
    )
    reporting = models.IntegerField(
        choices=PERMISION_CHOICES,
        default=0,
        verbose_name='Reportes'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        ordering = ['name']
