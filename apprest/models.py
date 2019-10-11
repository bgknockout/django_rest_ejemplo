from django.db import models

class Cliente(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=50)
    edad = models.IntegerField()


