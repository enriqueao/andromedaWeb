from django import forms
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
            'password':forms.TextInput(attrs={'class':'input'}),
            'nikname':forms.TextInput(attrs={'class':'input'}),
        }
