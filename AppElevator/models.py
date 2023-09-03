from django.db import models

# Create your models here.

class autor (models.Model):
    nombre = models.CharField(max_length=30)
    apellido =  models.CharField(max_length=50)
    edad = models.IntegerField(5)
    email= models.EmailField(max_length=254)
    pais = models.CharField(max_length=50)

class productor (models.Model):
    nombre = models.CharField(max_length=30)
    apellido =  models.CharField(max_length=50)
    edad = models.IntegerField(5)
    email = models.EmailField(max_length=254)
    pais = models.CharField(max_length=50)

class productora_audiovisual (models.Model):
    nombre = models.CharField(max_length=30)
    pag_web =  models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    pais = models.CharField(max_length=50)


class Proyecto(models.Model):
    nombre = models.CharField(max_length=50)
    logline = models.CharField(max_length=1000)
    plot = models.CharField(max_length=5000)
    genero = models.CharField(max_length=50)