from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage
from django.conf import settings
import traceback
from dotenv import load_dotenv
import os

load_dotenv()
# Create your views here.
def contacto(request):
    formulario_contacto = FormularioContacto()

    if request.method == "POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = formulario_contacto.cleaned_data["nombre"]
            email = formulario_contacto.cleaned_data["email"]
            contenido = formulario_contacto.cleaned_data["contenido"]
            
            email = EmailMessage("Mensaje desde App Django", 
                                 "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(nombre, email, contenido),
                                 "", [os.environ.get("EMAIL_HOST_USER")], reply_to=[email])
            try:
                email.send()
                return redirect("/contacto/?valido")
            except Exception as e:
                traceback.print_exc()
                return redirect("/contacto/?novalido")

    return render(request, "contacto/contacto.html", {'miFormulario': formulario_contacto})