from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.



# Modelo que representa a un autor.


class autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    email = models.EmailField(max_length=254)
    pais = models.CharField(max_length=50)

   

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
     


# Modelo que representa a un productor.
class productor (models.Model):
    nombre = models.CharField(max_length=30)
    apellido =  models.CharField(max_length=50)
    edad = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    email = models.EmailField(max_length=254)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    


# Modelo que representa a una productora audiovisual
class productora_audiovisual (models.Model):
    nombre = models.CharField(max_length=30)
    pag_web =  models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    pais = models.CharField(max_length=50)
    Productor =models.ManyToManyField (productor)

    def __str__(self):
        return self.nombre
    
  

# Modelo que representa a un proyecto.
class Proyecto(models.Model):
    nombre = models.CharField(max_length=50)
    logline = models.CharField(max_length=1000)
    plot = models.CharField(max_length=5000)
    genero = models.CharField(max_length=50)
    Autor = models.ForeignKey(autor, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nombre
    
