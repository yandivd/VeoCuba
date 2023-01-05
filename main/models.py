from django.db import models

# Create your models here.
class Estado(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    

class Imagen(models.Model):
    nombre = models.CharField(max_length=50, null=True, blank=True)
    ig = models.CharField(max_length=500, null=True, blank=True)
    sector = models.CharField(max_length=50)
    provincia = models.CharField(max_length=20)
    municipio = models.CharField(max_length=20)
    referencia = models.CharField(max_length=500)
    email = models.EmailField()
    telf = models.CharField(max_length=15)
    direccion = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos')
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    