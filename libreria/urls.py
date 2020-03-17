from django.urls import path
from .views import index, CrearLibro, ActualizarLibro, ListarLibro, EliminarLibro, VistaLibro
from .views import CrearAutor, ListarAutor, PrestarLibro, ListarPrestado, EditarPrestamo

urlpatterns = [
    #path('',Inicio.as_view(), name='index'),                    #index es el nombre asociado a la url, para poder llamarla atravez de ese nombre
    path('crear_libro/',CrearLibro.as_view(), name = 'crear_libro'),
    path('editar_libro/<int:pk>',ActualizarLibro.as_view(), name = 'editar_libro'),
    path('listar_libro/',ListarLibro.as_view(), name = 'listar_libro'),
    path('ver_libro/<int:pk>',VistaLibro.as_view(), name = 'ver_libro'),
    path('eliminar_libro/<int:pk>',EliminarLibro.as_view(), name = 'eliminar_libro'),
    path('crear_autor/',CrearAutor.as_view(), name = 'crear_autor'),
    path('listar_autor/',ListarAutor.as_view(), name = 'listar_autor'),
    path('prestar_libro',PrestarLibro.as_view(), name = 'prestar_libro'),
    path('listar_prestados',ListarPrestado.as_view(), name = 'listar_prestados'),
    path('prestar_libro/<int:pk>',EditarPrestamo.as_view(), name = 'prestar_libro'),
]
