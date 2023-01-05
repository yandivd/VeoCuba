from django.contrib import admin
from .models import *

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display = ('nombre','ig', 'categoria', 'email', 'foto',)

class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(Imagen, ImageAdmin)
admin.site.register(Estado, EstadoAdmin)
