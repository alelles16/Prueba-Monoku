from django.db import models

class Producto (models.Model):
    nombre = models.CharField(max_length=45)
    marca = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre
