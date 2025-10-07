from django.db import models

# Create your models here.

class Productos(models.Model):
    Nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    


    def __str__(self):
        return f"{self.Nombre}  {self.precio}"