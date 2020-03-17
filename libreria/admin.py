from django.contrib import admin
from.models import Libro, Autor, Genero, Usuario, Prestamo

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo','autor',)
    ordering = ['autor']

admin.site.register(Autor)
admin.site.register(Libro,LibroAdmin)
admin.site.register(Genero)
admin.site.register(Usuario)
admin.site.register(Prestamo)