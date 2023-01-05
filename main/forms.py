from django import forms
from .models import *

class ImagenForm(forms.ModelForm):
    
    class Meta:
        model = Imagen
        fields = '__all__'