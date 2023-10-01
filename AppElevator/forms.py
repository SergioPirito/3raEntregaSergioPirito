from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import autor, productor, productora_audiovisual, Proyecto

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'logline', 'plot', 'genero', 'Autor']

class ProductoraForm(forms.ModelForm):
    class Meta:
        model = productora_audiovisual
        fields = ['nombre', 'pag_web', 'email', 'pais', 'Productor']

class AutorForm(forms.ModelForm):
    class Meta:
        model = autor
        fields = ['nombre', 'apellido', 'edad', 'email', 'pais']

class ProductorForm(forms.ModelForm):
    class Meta:
        model = productor
        fields = ['nombre', 'apellido', 'edad', 'email', 'pais']
