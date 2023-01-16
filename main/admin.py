from django.contrib import admin
from .models import *

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display = ('nombre','ig', 'categoria', 'email', 'foto',)
    list_filter = ('categoria','estado',)

class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('subtitulo', 'texto',)
    class Meta:
        verbose_name = 'Historia'
        verbose_plural_name = 'Historias'

admin.site.register(Imagen, ImageAdmin)
# admin.site.register(Estado, EstadoAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
