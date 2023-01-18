from django.shortcuts import render, redirect
from .models import *
from .forms import *
import smtplib
from email.mime.text import MIMEText
from django.conf import settings
from django.contrib import messages

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
    return render(request, 'main/submission.html')

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

#correo para cuando contacten
def send_email(asunto, usuario, link):
    try:
        mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        print(mailServer.ehlo())
        mailServer.starttls()
        print(mailServer.ehlo())
        mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        print('Conectado...')

        email_to='yandivd@gmail.com'

        #construir el mensaje
        mensaje= MIMEText(usuario+""" ha dejado un testimonio acerca de ti. Entre al siguiente
                            link para acceder: """+ link)
        mensaje['From'] = settings.EMAIL_HOST_USER
        mensaje['To'] = email_to
        mensaje['Subject'] = asunto

        mailServer.sendmail(settings.EMAIL_HOST_USER,email_to, mensaje.as_string())
        print("Correo enviado")

    except Exception as e:
        print(e)