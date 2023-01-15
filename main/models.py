from django.db import models

# Create your models here.
#models del index
class Estado(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    

class Imagen(models.Model):
    nombre = models.CharField(max_length=50)
    ig = models.CharField(max_length=500)
    categoria = models.CharField(max_length=50)
    provincia = models.CharField(max_length=20)
    municipio = models.CharField(max_length=20)
    referencia = models.CharField(max_length=500)
    email = models.EmailField()
    telf = models.CharField(max_length=15)
    direccion = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos')
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    

    #models para el AboutUS

class Datos_para_about(models.Model):
    telf = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    website = models.CharField(max_length=500)

class AboutUs(models.Model):
    texto1 = models.CharField(max_length=500)
    texto2 = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to='about')

class Miembros(models.Model):
    imagen = models.ImageField(upload_to='miembros')
    nombre = models.CharField(max_length=100)
    labor = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
    

    