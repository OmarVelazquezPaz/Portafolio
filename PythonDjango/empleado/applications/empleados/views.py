from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,DetailView,CreateView,TemplateView,UpdateView,DeleteView
    )
from .models import Empleado
from .forms import EmpleadoForm
# Create your views here.

class InicioView(TemplateView):
    """ Vista que carga la pagina de Inicio"""
    template_name = 'inicio.html'

class ListAllEmpleados(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering ='first_name'
    context_object_name = 'lista'
    

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword","")
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave
        )
        return lista

class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 10
    ordering ='first_name'
    context_object_name = 'lista'
    model = Empleado



class ListByArea(ListView):
    template_name = 'persona/list_by_area.html'
    model = Empleado
    """queryset = Empleado.objects.filter(
        #departamento__name = 'Area Contable' 
        departamento__short_name = 'contabilidad'
    )"""
    context_object_name = 'lista'

    def get_queryset(self) :
        area = self.kwargs['shortname'] # Por url
        lista =Empleado.objects.filter(
        #departamento__name = 'Area Contable' 
        departamento__short_name = area
        )
        return lista
        

class ListEmpleadosByKword(ListView):
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword","")
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        return lista
    
class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
         empleado = Empleado.objects.get(id=8)
         return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs) :
        context = super(EmpleadoDetailView,self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context


class SuccessView(TemplateView):
    template_name = 'persona/success.html'


class EmpleadoCreateView(CreateView):
    template_name = 'persona/add.html'
    model = Empleado
    #fields = ['first_name','last_name','job','departamento','habilidades','avatar']
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self,form):
        empleado = form.save()
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView,self).form_invalid(form)
    
class EmpleadoUpdateView(UpdateView):
    template_name = 'persona/update.html'
    model = Empleado
    fields = ['first_name','last_name','job','departamento','habilidades']
    success_url = reverse_lazy('persona_app:empleados_admin')

class EmpleadoDeleteView(DeleteView):
    template_name = 'persona/delete.html'
    model = Empleado
    success_url = reverse_lazy('persona_app:empleados_admin')