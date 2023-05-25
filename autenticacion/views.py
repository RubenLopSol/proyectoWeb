from django.shortcuts import render, redirect

from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.

class VRegistro(View):

    def get(self, request):
        
        form=UserCreationForm()
        return render(request,"registro/registro.html", {"form":form})

    def post(self,request):
        
        # Instanciar en una variable el formulario con request.POST data (creacion)
        form=UserCreationForm(request.POST) 
        
        if form.is_valid():
            form=UserCreationForm(request.POST)
            # Almacenar datos en la base de datos en auth:
            usuario=form.save()
            # Login automatico:
            login(request, usuario)

            return redirect('home')
        else:

            # Gestion de mensages de error para el UI:
            for msg in form.error_messages:
               
                messages.error(request, form.error_messages[msg])

            return render(request, "registro/registro.html", {"form":form})

def cerrar_session(request):
    
    logout(request)
    
    return redirect('home')


def VLogin(request):

    if request.method == "POST":
        form=AuthenticationForm(request, data= request.POST)
        
        if form.is_valid():
            # Guardamos en variables el contenido de los campos de login: 
            nombre_usuario=form.cleaned_data.get("username")
            passw= form.cleaned_data.get("password")
            # Authenticate, para identificar al usuario:
            usuario= authenticate(username=nombre_usuario, password=passw)
            if usuario is not None:
                login(request, usuario)
                return redirect('home')
            else:
                messages.error(request, "Usuario no válido")
        else:
            messages.error(request, "Informacion incorrecta")
    
    # creacion formulario login con la clase Autenticationform:
    form=AuthenticationForm()

    return render(request, "login/login.html", {"form":form})
