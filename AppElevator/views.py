from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Avatar
from django.contrib import messages

from .forms import (
    ProyectoForm, AutorForm, ProductorForm, ProductoraForm,
    UserEditForm, AvatarFormulario
)
from .models import Proyecto, productora_audiovisual, autor, productor, Avatar
from django.contrib import messages


# Base de datos
def proyecto_view(request, nombre, logline, plot, genero):
    proyecto = Proyecto(nombre=nombre, logline=logline, plot=plot, genero=genero)
    proyecto.save()

    return HttpResponse(f"""
<p> Proyecto: {proyecto.nombre}, logline {proyecto.logline}, plot {proyecto.plot}, genero {proyecto.genero} Agregado con Exito!</p>""")

def productora_view(request, nombre, pag_web, email, pais):
    productora = productora_audiovisual (nombre=nombre, pag_web=pag_web, email=email, pais=pais)
    productora.save()

    return HttpResponse(f"""
<p> Productora: {productora.nombre}, pag_web {productora.pag_web}, email {productora.email}, pais {productora.pais} Agregado con Exito!</p>""")

def autor_view(request, nombre, apellido, edad, email, pais):
    Autor = autor(nombre=nombre, apellido=apellido, edad=edad, email=email, pais=pais)
    Autor.save()

    return HttpResponse(f"""
<p> Autor: {autor.nombre} {autor.apellido}, edad {autor.edad}, email {autor.email}, pais {autor.pais} Agregado con Exito!</p>""")

def productor_view(request, nombre, apellido, edad, email, pais):
    Productor = productor(nombre=nombre, apellido=apellido, edad=edad, email=email, pais=pais)
    Productor.save()

    return HttpResponse(f"""
<p> Productor: {productor.nombre} {productor.apellido}, edad {productor.edad}, email {productor.email}, pais {productor.pais} Agregado con Exito!</p>""")

# Listas

def lista_proyecto(request):
    listas_proyecto = Proyecto.objects.all().order_by('nombre')

    paginator = Paginator(listas_proyecto, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'listas_proyecto.html', {"listas_proyecto": page_obj})

def lista_productor(request):
    listas_productor = productor.objects.all().order_by('nombre')

    paginator = Paginator(listas_productor, 3) # Muestra 3 productores por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'listas_productor.html', {"listas_productor": page_obj})



def lista_productora(request):
    listas_productora = productora_audiovisual.objects.all().order_by('nombre')

    paginator = Paginator(listas_productora, 3) # Muestra 3 productoras por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'listas_productora.html', {"listas_productora": page_obj})

def lista_autor(request):
    listas_autor = autor.objects.all().order_by('nombre')

    paginator = Paginator(listas_autor, 3) # Muestra 3 autores por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'listas_autor.html', {"listas_autor": page_obj})


#Vistas

def inicio (request):
    return render (request,'inicio.html')

def vista_autor (request):
    return render (request,'listas_autor.html')

def vista_productor (request):
    return render (request,'listas_productor.html')

def vista_productora (request):
    return render (request, 'listas_productora.html')

def vista_proyecto (request):
    return render (request,'listas_proyecto.html')

#Formularios

def formulario_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AppElevator:lista_proyecto')
    else:
        form = ProyectoForm()

    return render(request, 'formulario_proyecto.html', {'form': form})

def formulario_autores(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AppElevator:lista_autor')
    else:
        form = AutorForm()

    return render(request, 'formulario_autores.html', {'form': form})

def formulario_productores(request):
    if request.method == 'POST':
        form = ProductorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AppElevator:lista_productor')
    else:
        form = ProductorForm()

    return render(request, 'formularioProductores.html', {'form': form})

def formulario_productoras(request):
    if request.method == 'POST':
        form = ProductoraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AppElevator:lista_productora')
    else:
        form = ProductoraForm()

    return render(request, 'formularioProductoras.html', {'form': form})

# Editar Eliminar Proyecto y Html details
def proyecto_detalles(request, nombre):
    encontrarProyectoPorNombre = Proyecto(nombre=nombre)

    proyecto = get_object_or_404(Proyecto, nombre=encontrarProyectoPorNombre.nombre)
    return render(request, 'proyecto_detalles.html', {'proyecto': proyecto})

def editar_proyecto(request, nombre):
    proyecto = get_object_or_404(Proyecto, nombre=nombre)

    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return render(request, 'formulario_proyecto.html', {"mensaje": "Proyecto editado con éxito"})
    else:
        form = ProyectoForm(instance=proyecto)

    return render(request, 'formulario_proyecto.html', {'form': form})

def eliminar_proyecto(request, nombre):
    proyecto = get_object_or_404(Proyecto, nombre=nombre)

    if request.method == 'POST':
        proyecto.delete()
        return redirect('AppElevator:lista_proyecto')
    
    return render(request, 'confirmar_eliminacion.html', {'proyecto': proyecto})

# Editar Eliminar Autor y Html details

def autor_detalles(request, nombre):
    autores = autor.objects.filter(nombre=nombre)
    print(autores)
    # if not autores.exists():
    #     return render(request, 'autor_no_encontrado.html', {'nombre': nombre})
    
    autorFound = autores.first()

    return render(request, 'autor_detalles.html', {'Autor': autorFound})

def editar_autor(request, nombre):
    Autor = get_object_or_404(autor, nombre=nombre)

    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return render(request, 'formulario_autor.html', {"mensaje": "Autor editado con éxito"})
    else:
        form = AutorForm(instance=autor)

    return render(request, 'formulario_autor.html', {'form': form})

def eliminar_autor(request, nombre):
    Autor = get_object_or_404( autor, nombre=nombre)

    if request.method == 'POST':
        Autor.delete()
        return redirect('AppElevator:lista_autor')
    
    return render(request, 'confirmar_eliminacion.html', {'autor': Autor})



#login


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user:
                login(request, user)
                return redirect('/App-Elevator/')
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/App-Elevator/')
    else:
        form = UserCreationForm()
    return render(request, "registro.html", {"form": form})

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            messages.success(request, "Perfil actualizado con éxito")
            return redirect('inicio')
    else:
        form = UserEditForm(instance=request.user)
    return render(request, "editarPerfil.html", {"form": form})

@login_required
def agregar_avatar(request):
    if request.method == 'POST':
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            avatar = form.save(commit=False)
            avatar.user = request.user
            avatar.save()
            messages.success(request, "Avatar actualizado con éxito")
            return redirect('inicio')
    else:
        form = AvatarFormulario()
    return render(request, "agregarAvatar.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('/App-Elevator/')
