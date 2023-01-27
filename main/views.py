from django.shortcuts import render, redirect
from .models import *
from .forms import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    estado1 = Estado.objects.get(nombre='ok')
    fotos = Imagen.objects.all().filter(estado=estado1)
    menor = 9999999999999
    for i in fotos:
        if i.id<menor:
            menor=i.id
    data={
        'fotos': fotos,
        'menor': menor,
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

    provinciasArray=['','Pinar del Rio', 'Artemisa', 'La Habana', 'Mayabeque','Matanzas','Villa Clara', 'Cienfuegos','Sancti Spíritus','Ciego de Ávila','Camagüey','Las Tunas','Holguín','Granma','Santiago de Cuba','Guantánamo','Isla de la Juventud']
    data={
        'form': ImagenForm()
    }
    if(request.method == 'POST'):
        formulario = ImagenForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            print(type(formulario.cleaned_data['foto'].size))
            ### validar las imagenes actual: imagen > 2mb ###
            if formulario.cleaned_data['foto'].size < 2097152:
                data["form"] = formulario
                return render(request, 'main/submission.html',data)
            else:
                try:
                    estado1 = Estado.objects.get(nombre='revisar')
                except:
                    print("No existe estado con ese nombre")
                imagen1 = Imagen(nombre=formulario.cleaned_data['nombre'],
                ig=formulario.cleaned_data['ig'], 
                categoria=formulario.cleaned_data['categoria'],
                provincia=provinciasArray[int(formulario.cleaned_data['provincia'])], 
                municipio=formulario.cleaned_data['municipio'], 
                referencia=formulario.cleaned_data['referencia'],
                email=formulario.cleaned_data['email'], 
                telf=formulario.cleaned_data['telf'], 
                direccion=formulario.cleaned_data['direccion'],
                foto=formulario.cleaned_data['foto'],
                estado=estado1)
                imagen1.save()
                ###llamada al metodo de enviar el correo
                send_emailI(imagen1)
                messages.success(request, "Gracias por compartir su imagen con nosotros.")
                return redirect('index')
        else:
            data['form'] = formulario

    return render(request, 'main/submission.html',data)

def contact(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario= ContactoForm(data=request.POST)
        if formulario.is_valid():
            email=formulario.cleaned_data['email']
            texto=formulario.cleaned_data['message']
            formulario.save()
            ###llamada al metodo de enviar el correo
            # send_emailC(email, texto)
            messages.success(request, "Gracias por contactarme")
            print(messages)
            return redirect(to='index')
        else:
            data['form']=formulario

    return render(request, 'main/contact.html', data)

##### Funciones para el envio de correo ###
######funcion para enviar correos#######
def send_emailC(email,texto):
    try:
        mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        print(mailServer.ehlo())
        mailServer.starttls()
        print(mailServer.ehlo())
        mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        print('Conectado...')

        ####cambiar el correo para el del que lo recive
        email_to='yandivd@gmail.com'

        #construir el mensaje
        mensaje= MIMEText("""Alguien ha hecho contacto contigo a traves de tu sitio Web.  """+
                        "Correo: "+email+' '+"Mensaje: "+texto )
        mensaje['From'] = settings.EMAIL_HOST_USER
        mensaje['To'] = email_to
        mensaje['Subject'] = 'Te han dejado un mensaje'

        mailServer.sendmail(settings.EMAIL_HOST_USER,email_to, mensaje.as_string())
        print("Correo enviado")

    except Exception as e:
        print(e)

##### Funcion para el envio de correo con la imagen #########
def send_emailI(foto):
    try:
        mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        print(mailServer.ehlo())
        mailServer.starttls()
        print(mailServer.ehlo())
        mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        print('Conectado...')

        ####cambiar el correo para el del que lo recive
        email_to='yandivd@gmail.com'

        #construir el mensaje
        # mensaje= MIMEText("""Se ha publicado una imagen.  """+
        #                 "Nombre: "+foto.nombre+' '+"Instagram: "+
        #                 foto.ig+' '+"Categoria: "+foto.categoria+
        #                 ' '+"Provincia: "+foto.provincia+
        #                 ' '+"Municipio: "+foto.municipio+
        #                 ' '+"Escucho sobre nosotros mediante: "+foto.referencia+
        #                 ' '+"Correo: "+foto.email+
        #                 ' '+"Telefono: "+foto.telf+
        #                 ' '+"Direccion: "+foto.direccion+
        #                 ' '+"Imagen: "+"localhost:8000/"+foto.foto.url)
        mensaje= MIMEMultipart()
        mensaje['From'] = settings.EMAIL_HOST_USER
        mensaje['To'] = email_to
        mensaje['Subject'] = 'Te han dejado un mensaje'

        content = render_to_string('send_email.html',{'foto': foto })

        mensaje.attach(MIMEText(content,'html'))

        mailServer.sendmail(settings.EMAIL_HOST_USER,email_to, mensaje.as_string())
        print("Correo enviado")

    except Exception as e:
        print(e)

def test(request):
    return render(request, "send_email.html",{'foto':Imagen.objects.get(pk=1)})