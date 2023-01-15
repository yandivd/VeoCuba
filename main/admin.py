from django.contrib import admin
from .models import *

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display = ('nombre','ig', 'categoria', 'email', 'foto',)
    list_filter = ('categoria','estado',)

class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('sub1es','texto1es','sub2es','texto2es','sub3es','texto3es',
    'sub4es','texto4es','sub1en','texto1esn','sub2en','texto2en',
    'sub3en','texto3en','sub4en','texto4en',)
    class Meta:
        verbose_name = 'Historia'
        verbose_plural_name = 'Historias'

admin.site.register(Imagen, ImageAdmin)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
