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
    historia = AboutUs.objects.all()[0]
    print(historia)
    data = {
        'historia':historia,
    }
    return render(request, 'main/about.html', data)