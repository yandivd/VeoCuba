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
    

    #####models para el AboutUS####

# class Datos_para_about(models.Model):
#     telf = models.CharField(max_length=15)
#     email = models.EmailField()
#     address = models.CharField(max_length=200)
#     website = models.CharField(max_length=500)

class AboutUs(models.Model):
    subtitulo = models.CharField(max_length=100, verbose_name='subtitulo')
    texto = models.TextField(verbose_name= 'texto')
    class Meta:
        verbose_name = 'Historia'
        verbose_name_plural = 'Historias'

class Miembros(models.Model):
    imagen = models.ImageField(upload_to='miembros')
    nombre = models.CharField(max_length=100)
    labor = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
    
###### Models para el Contacto ######## 

class Contacto(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Tamanno(models.Model):
    name = models.CharField(max_length=10)
    capacidad = models.IntegerField()

    def __str__(self):
        return self.name

class Calidad_Permitida(models.Model):
    capacidad = models.ForeignKey(to=Tamanno, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.capacidad.name
    
    
