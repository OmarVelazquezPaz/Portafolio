from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad

# Create your models here.

class Empleado(models.Model):
    """Modelo para tabla empleado"""
    JOB_CHOICES = (
        ('0','CONTADOR'),
        ('1','ADMINISTRADOR'),
        ('2','ECONOMISTA'),
        ('3','OTRO')
    )

    first_name = models.CharField('Nombres',max_length=50)
    last_name = models.CharField('Apellidos',max_length=50)
    full_name = models.CharField('Nombre Completo', max_length=120,blank=True)
    job = models.CharField('Trabajo', max_length=1,choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True,null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()


    class Meta:
        verbose_name:'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['last_name']
        unique_together = ('last_name','first_name')

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name
