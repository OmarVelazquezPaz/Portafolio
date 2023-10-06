from django.db import models
from django.db.models.signals import post_save
from applications.autor.models import Autor
from .managers import LibroManager,CategoriaManager

from PIL import Image

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    objects = CategoriaManager()

    def __str__(self) :
        return str(self.id) + '-' + self.nombre
    
class Libro(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,related_name='categoria_libro')
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField(max_length=50)
    fecha = models.DateField('Fecha de lanzamiento')
    portada = models.ImageField(upload_to='portadas')
    visitas = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=0)

    objects = LibroManager()

    class Meta:
        verbose_name = 'Libro'
        ordering = ['titulo']

    def __str__(self) :
        return str(self.id) + '-' + self.titulo
    
def optimize_image(sender,instance,**kwargs):
    if instance.portada:
        portada = Image.open(instance.portada.path)
        portada.save(instance.portada.path,quality=20,optimize=True)

post_save.connect(optimize_image,sender=Libro)
    
"""
usar la shell de django
python manage.py shell
"""