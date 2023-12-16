from django.shortcuts import render
#
from .models import PropertyModel
#
from .serializer import PropertySerializer,PropertyPagination
from rest_framework.generics import (ListAPIView,CreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView)
# Create your views here.

class HeyHomListView(ListAPIView):
    """
    This view lists all the information avalable, with all the fields.
    """
    queryset = PropertyModel.objects.all()
    serializer_class = PropertySerializer
    pagination_class = PropertyPagination

class HeyHomCreateView(CreateAPIView):
    """
    This view add information.
    """
    serializer_class = PropertySerializer
    

class HeyHomDetailView(RetrieveAPIView):
    """
    This view gives the detail of a specific object, by Id
    """
    queryset = PropertyModel
    serializer_class = PropertySerializer

class HeyHomUpdateView(RetrieveUpdateAPIView):
    """
    This view update information but shows the information that
    is going to be updated, it retrieves the info by Id.
    """
    queryset = PropertyModel
    serializer_class = PropertySerializer

class HeyHomDelete(RetrieveDestroyAPIView):
    """
    This view deetes an object by Id.
    """
    queryset = PropertyModel
    serializer_class = PropertySerializer
