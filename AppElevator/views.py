from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .forms import ProyectoForm, AutorForm, ProductorForm, ProductoraForm
from .models import Proyecto, productora_audiovisual, autor, productor 
from django.core.paginator import Paginator


# Base de datos
def proyecto_detalles(request, nombre):
    encontrarProyectoPorNombre = Proyecto(nombre=nombre)

    proyecto = get_object_or_404(Proyecto, nombre=encontrarProyectoPorNombre.nombre)
    return render(request, 'proyecto_detalles.html', {'proyecto': proyecto})


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
            return render(request, 'formulario_autores.html', {"mensaje": "Autor creado con éxito"})
    else:
        form = AutorForm()

    return render(request, 'formulario_autores.html', {'form': form})

def formulario_productores(request):
    if request.method == 'POST':
        form = ProductorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'formularioProductores.html', {"mensaje": "Productor creado con éxito"})
    else:
        form = ProductorForm()

    return render(request, 'formularioProductores.html', {'form': form})

def formulario_productoras(request):
    if request.method == 'POST':
        form = ProductoraForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'formularioProductoras.html', {"mensaje": "Productora Audiovisual creada con éxito"})
    else:
        form = ProductoraForm()

    return render(request, 'formularioProductoras.html', {'form': form})


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




