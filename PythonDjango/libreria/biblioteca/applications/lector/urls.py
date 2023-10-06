from django.contrib import admin
from django.urls import path
from . import views

app_name = 'lector'

urlpatterns = [
    path("prestamo/add/", views.RegistrarPrestamo2.as_view(), name='prestamo-add'),
    path('prestamo/multiple-add/',views.AddMultiplePrestamo.as_view(),name='prestamos_add_multiple'),
]
