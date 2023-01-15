from django.db import models

# Create your models here.
#models del index
class Estado(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
    

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
    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'
    

    #models para el AboutUS

# class Datos_para_about(models.Model):
#     telf = models.CharField(max_length=15)
#     email = models.EmailField()
#     address = models.CharField(max_length=200)
#     website = models.CharField(max_length=500)

class AboutUs(models.Model):
    sub1es = models.CharField(max_length=10000, verbose_name='Subtitulo 1')
    texto1es = models.CharField(max_length=5000000)
    sub2es = models.CharField(max_length=10000)
    texto2es = models.CharField(max_length=5000000)
    sub3es = models.CharField(max_length=10000)
    texto3es = models.CharField(max_length=5000000)
    sub4es = models.CharField(max_length=10000)
    texto4es = models.CharField(max_length=5000000)
    #######Seccion en Ingles#############
    sub1en = models.CharField(max_length=10000)
    texto1esn= models.CharField(max_length=5000000)
    sub2en = models.CharField(max_length=10000)
    texto2en = models.CharField(max_length=5000000)
    sub3en = models.CharField(max_length=10000)
    texto3en = models.CharField(max_length=5000000)
    sub4en = models.CharField(max_length=10000)
    texto4en = models.CharField(max_length=5000000)
    # imagen = models.ImageField(upload_to='about')
    class Meta:
        verbose_name = 'Historia'
        verbose_name_plural = 'Historia'

class Miembros(models.Model):
    imagen = models.ImageField(upload_to='miembros')
    nombre = models.CharField(max_length=100)
    labor = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
    

    