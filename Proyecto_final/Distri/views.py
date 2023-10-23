from django.shortcuts import render
from django.template import loader
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Leches
from .forms import LecheFormulario

@login_required
def catalo(request):
    return render (request, "Distri/catalogo.html")

def inicio(request):
    return render (request, "Distri/inicio.html")

@login_required
def aboutme(request):
    return render (request, "Distri/aboutme.html")

def log(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")

            clave = form.cleaned_data.get("password")

            nombre_usuario = authenticate(username = usuario, password = clave)

            if usuario is not None:

                login (request, nombre_usuario)

                return render(request, "Distri/inicio.html", {"mensaje":f"Has iniciado sesión. Bienvenido {usuario}"})
                

            else:

                return render(request, "Distri/inicio.html", {"mensaje":"Error, datos incorrectos", "form":form})

        else:

            return render(request, "Distri/inicio.html", {"mensaje":"Error, formulario inválido"})

    form = AuthenticationForm()

    return render(request, "Distri/login.html", {"form":form})


def signup(request):
     

     if request.method == "POST":
            
            #form = UserCreationForm(request.POST)

            form = UserCreationForm(request.POST)

            if form.is_valid():

                  username = form.cleaned_data["username"]

                  form.save()

                  return render(request,"Distri/signup.html" ,  {"mensaje":"Usuario creado corrrectamente:)"})
            
     else:

            #form = UserCreationForm()       

            form = UserCreationForm()     
            return render(request,"Distri/login.html" ,  {"form":form})
     

def leches(request):
     milk= Leches.objects.all()
     contexto={"milk":milk}
     return render(request, "Distri/cati.html", contexto)   


 
def catalogo(request):
 
      if request.method == "POST":
 
            miFormulario = LecheFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  leche = Leches(marca=informacion["marca"], precio =informacion["precio"],email=informacion["email"])
                  leche.save()
                  return render(request, "Distri/inicio.html")
      else:
            miFormulario = LecheFormulario()
 
      return render(request, "Distri/catalogo.html", {"miFormulario": miFormulario})