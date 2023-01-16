from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    estado1 = Estado.objects.get(nombre='ok')
    fotos = Imagen.objects.all().filter(estado=estado1)
    data={
        'fotos': fotos,
    }
    return render(request, 'main/index.html', data)

def about(request):
    historia = AboutUs.objects.all()
    data = {
        'historias':historia,
    }
    return render(request, 'main/about.html', data)

#este metodo es el encargado de renderizar los formularios para subir una foto
def submission(request):
    return render(request, 'main/submission.html')

def contact(request):
    return render(request, 'main/contact.html')