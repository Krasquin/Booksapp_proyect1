from django.shortcuts import render
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.db.models import Q 
from .models import Libro, Autor, Genero, Prestamo
from .forms import LibroForm, AutorForm, PrestamoForm

def index(request):
    """
    Función para index.
    """
    num_libros = Libro.objects.all().count()

    num_prestamos = Prestamo.objects.all().count()
    #num_libros_disponibles = Prestamo.objects.filter(status__exact='d').count()  # Libros disponibles (status = 'd')
    num_libros_disponibles = num_libros - num_prestamos
    num_autores = Autor.objects.count()  # El 'all()' esta implícito por defecto.
    
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_libros':num_libros,'num_autores':num_autores,'num_prestamos':num_prestamos,'num_libros_disponibles':num_libros_disponibles},
    )   

class CrearLibro(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libreria/crear_libro.html'
    success_url = reverse_lazy('index')

class ActualizarLibro(UpdateView):                      #Es igual a CrearAutor, pero en las urls se llama con el parametro pk para que lea los datos y llene el form
    model = Libro
    form_class = LibroForm
    template_name = 'libreria/crear_libro.html'
    success_url = reverse_lazy('index')

class ListarLibro(ListView):
    model = Libro
    template_name = 'libreria/listar_libro.html'
    #paginate_by = 5
    context_object_name = 'libros'                     #la consulta del queryset la retorna como objectos. Con context_object_name pasamos ese objecto a una lista

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query != None:
            object_list = Libro.objects.filter(
                Q(titulo__icontains=query) | Q(autor__apellido__icontains=query) | Q(autor__nombre__icontains=query)
            )
            return object_list

class VistaLibro(DetailView):
    model = Libro
    template_name = 'libreria/ver_libro.html'

class EliminarLibro(DeleteView):                        #Por defecto busca un template _confirm_delete.html, que es una pagina de confirmacion
    model = Libro
    success_url = reverse_lazy('libreria:listar_libro')

class CrearAutor(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'libreria/crear_autor.html'
    success_url = reverse_lazy('index')

class ListarAutor(ListView):
    model = Autor
    template_name = 'libreria/listar_autor.html'
    #paginate_by = 10

class PrestarLibro(CreateView):
    model = Prestamo
    form_class = PrestamoForm
    template_name = 'libreria/prestar_libro.html'
    success_url = reverse_lazy('index')

class ListarPrestado(ListView):
    model = Prestamo
    template_name = 'libreria/listar_prestados.html'

class EditarPrestamo(UpdateView):
    model = Prestamo
    form_class = PrestamoForm
    template_name = 'libreria/prestar_libro.html'
    success_url = reverse_lazy('index')
