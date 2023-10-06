from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from .models import Prueba
from .forms import PruebaForms
# Create your views here.

class IndexView(TemplateView):
    template_name = 'home/home.html'

class ResumenFoundationView(TemplateView):
    template_name = 'home/resumen_foundation.html'

class PruebaListView(ListView):
    template_name = 'home/lista.html'
    queryset = ['a','b','c']
    context_object_name = 'lista_prueba'

class ModeloPruebaListView(ListView):
    model = Prueba
    template_name = 'home/pruebas.html'
    context_object_name = 'lista_prueba'

class PruebaCreateView(CreateView):
    template_name = 'home/add.html'
    model = Prueba
    form_class = PruebaForms
    success_url = '/'