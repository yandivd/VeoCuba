from django import forms
from .models import *

class ImagenForm(forms.ModelForm):
    
    class Meta:
        model = Imagen
        fields = '__all__'

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'