from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Autor, Productor, Productora_audiovisual, Proyecto
from .models import Avatar

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'logline', 'plot', 'genero', 'Autor']

class ProductoraForm(forms.ModelForm):
    class Meta:
        model = Productora_audiovisual
        fields = ['nombre', 'pag_web', 'email', 'pais', 'Productor']

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido', 'edad', 'email', 'pais']

class ProductorForm(forms.ModelForm):
    class Meta:
        model = Productor
        fields = ['nombre', 'apellido', 'edad', 'email', 'pais']

class UserEditForm (UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_password2(self):

        print(self.cleaned_data)

        password2 = self.cleaned_data["password2"]
        if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2
    
class AvatarFormulario(forms.ModelForm):

    class Meta:
        model=Avatar
        fields=('imagen',)