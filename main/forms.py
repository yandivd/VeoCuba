from django import forms
from .models import *

class ImagenForm(forms.ModelForm):
    
    class Meta:
        model = Imagen
        fields = 'nombre','ig','categoria','provincia','municipio','referencia','email','telf','direccion','foto'


class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'
