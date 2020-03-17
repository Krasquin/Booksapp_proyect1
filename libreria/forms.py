from django import forms
from .models import Libro, Autor, Genero, Prestamo

class LibroForm(forms.ModelForm): #Definicion del formulario para Libros
    class Meta:
        model = Libro
        fields = ['titulo','autor','genero','resumen','portada']

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre','apellido',]

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['genero',]

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['libro','fechaDev','usuario','status',]
     