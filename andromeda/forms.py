from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from andromeda.models import *


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = usuario

        fields = [
            'nombre',
            'password',
            'nikname',
        ]
        labels = {
            'nombre':'Nombre',
            'password': 'Contaseña',
            'nikname':'nickname',
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'input'}),
            'password':forms.PasswordInput(attrs={'class':'input'}),
            'nikname':forms.TextInput(attrs={'class':'input'}),
        }

class LoginForm(forms.Form):
    name_user = forms.CharField(max_length=20,required=True,label='',
    widget=(forms.TextInput(attrs={'placeholder':'Nombre de Usuario','class':''})))

    password_user = forms.CharField(max_length=20,required=True,label='',
    widget=(forms.PasswordInput(attrs={'placeholder':'Contraseña','class':''})))

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username':'Nombre de Usuario',
            'first_name':'Nombre',
            'last_name':'Apellidos',
            'email':'correo',
        }
