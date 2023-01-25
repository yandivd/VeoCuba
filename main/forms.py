from django import forms
from .models import *

class ImagenForm(forms.ModelForm):
    
    class Meta:
        model = Imagen
        fields = 'nombre','ig','categoria','provincia','municipio','referencia','email','telf','direccion','foto'
    
    #metodo para validar imagenes not working yet
    def clean_image(self):
        image = self.cleaned_data['foto']
        if image:
            if image.__size < 4*1024*1024:
                raise ValidationError("Imagen demasiado grande")
            return image
        else:
            raise ValidationError("No se cargo la imagen")

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'
