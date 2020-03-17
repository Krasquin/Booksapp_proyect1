from django.db import models
from django.urls import reverse
import uuid # Requerida para las instancias de libros únicos


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 100)

    class Meta:
        verbose_name_plural = 'Autores'
        ordering = ['apellido', 'nombre']

    def get_absolute_url(self):
        return reverse('detalle de autor', args=[str(self.id)])     #Devuelve la url para aceder a una instancia de autor en particular

    def __str__(self):
        return '{0}, {1}'.format(self.apellido, self.nombre)

class Genero(models.Model):
    genero = models.CharField(max_length = 250 , help_text = 'Ingrese género')

    def __str__(self):
        return self.genero

class Libro(models.Model):
    titulo = models.CharField(max_length = 200)
    autor = models.ForeignKey(Autor, on_delete = models.SET_NULL, null = True)
    # Foreign Key (uno a muchos) un autor puede tener varios libros
    # on_delete= en caso de borrar refencia (autor) la relacion queda nula
    genero = models.ForeignKey(Genero, on_delete = models.SET_NULL, null = True)
    # ManyToManyField (muchos a mucho) un libro puede tener muchos generos, y vivecersa
    resumen = models.TextField(blank = True, help_text='Resumen del libro')
    portada = models.ImageField(blank = True)

    #Metadatos
    class Meta:
        verbose_name_plural = 'Libros'  #nombre en plural para admin
        ordering = ['autor']            #ordena por autor

    def __str__(self):
        return self.titulo              #muestra el titulo como texto, en lugar del object
 
    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('ver_libro', args=[str(self.id)])

 
class Usuario(models.Model):
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 50)
    telefono = models.CharField(max_length = 25)
    ci = models.CharField(max_length = 8)

    def __str__(self):
        return self.ci           
  

class Prestamo(models.Model):
    """
    Modelo que representa una copia específica de un libro (i.e. que puede ser prestado por la biblioteca).
    """
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para este libro particular en toda la biblioteca")
    libro = models.ForeignKey(Libro, on_delete=models.SET_NULL, null=True) 
    fechaDev = models.DateField(null=True, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete = models.SET_NULL, null = True , blank = True)

    ESTADO = (
        ('m', 'Mantenimiento'),
        ('p', 'Prestado'),
        ('d', 'Disponible'),
        ('r', 'Reservado'),
    )

    status = models.CharField(max_length=1, choices=ESTADO, blank=True, default='m', help_text='Disponibilidad del libro')

    class Meta:
        ordering = ["fechaDev"]
        

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s (%s)' % (self.id,self.libro.titulo)
