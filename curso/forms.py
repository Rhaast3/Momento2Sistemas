from django import forms
from .models import curso  

class CursoForm(forms.ModelForm):
    class Meta:
        model = curso
        fields = ['nombre', 'capacidad_max', 'profesor'] 