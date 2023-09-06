from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
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

def formulario_proyecto (request:HttpRequest ):
    if request.method=='POST':
        proyecto = Proyecto(nombre=request.POST["nombre"], logline=request.POST["logline"], plot=request.POST["plot"], genero=request.POST["genero"])
        proyecto.save()

    return render (request,'formulario_proyecto.html',{"mensaje":"Proyecto creado con éxito"})

def formulario_autores (request:HttpRequest ):
    if request.method=='POST':
        Autor = autor(nombre=request.POST["nombre"], apellido=request.POST["apellido"] , edad=request.POST["edad"], email=request.POST["email"], pais=request.POST["pais"])
        Autor.save()    
    return render (request,'formulario_autores.html',{"mensaje":"Autor creado con éxito"})

def formulario_productores (request:HttpRequest ):
    if request.method=='POST':
        Productor = productor(nombre=request.POST["nombre"], apellido=request.POST["apellido"], edad=request.POST["edad"], email=request.POST["email"], pais=request.POST["pais"])
        Productor.save()
    return render (request,'formularioProductores.html',{"mensaje":"Productor creado con éxito"})

def formulario_productoras (request:HttpRequest ):
    if request.method=='POST':
        productora = productora_audiovisual (nombre=request.POST["nombre"], pag_web=request.POST["pag_web"], email=request.POST["email"], pais=request.POST["pais"])
        productora.save()
    return render (request,'formularioProductoras.html',{"mensaje":"Productora Audiovisual creada con éxito"})

