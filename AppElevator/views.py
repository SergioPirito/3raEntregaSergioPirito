from django.shortcuts import render
from django.http import HttpResponse
from .models import Proyecto, productora_audiovisual, autor, productor 

# Create your views here.

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

def lista_productor(request):
    listas_productor = productor.objects.all()
    return render(request, 'listas_productor.html', {"listas_productor": listas_productor})



def lista_proyecto(request):
    listas_proyecto = Proyecto.objects.all()
    return render(request, 'listas_proyecto.html', {"listas_proyecto": listas_proyecto})

def lista_productora(request):
    listas_productora = productora_audiovisual.objects.all()
    return render(request, 'listas_productora.html', {"listas_productora": listas_productora})

def lista_autor(request):
    listas_autor = autor.objects.all()
    return render(request, 'listas_autor.html', {"listas_autor": listas_autor})


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

def formulario_proyecto (request):
    return render (request,'formulario_proyecto.html')

def formulario_autores (request):
    return render (request,'formulario_autores.html')

def formulario_productores (request):
    return render (request,'formularioProductores.html')

def formulario_productoras (request):
    return render (request,'formularioProductoras.html')

