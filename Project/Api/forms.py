from .models import *
from django import forms

class FormularioRegistro(forms.ModelForm):
    class Meta:
        model=Alumnos
        fields='__all__'