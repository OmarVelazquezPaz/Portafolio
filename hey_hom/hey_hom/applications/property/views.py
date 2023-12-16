from django.shortcuts import render
#
from .models import PropertyModel
#
from .serializer import PropertySerializer,PropertyPagination
from rest_framework.generics import (ListAPIView,CreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView)
# Create your views here.

class HeyHomListView(ListAPIView):
    queryset = PropertyModel.objects.all()
    serializer_class = PropertySerializer
    pagination_class = PropertyPagination

class HeyHomCreateView(CreateAPIView):
    
    serializer_class = PropertySerializer
    

class HeyHomDetailView(RetrieveAPIView):
    queryset = PropertyModel
    serializer_class = PropertySerializer

class HeyHomUpdateView(RetrieveUpdateAPIView):
    queryset = PropertyModel
    serializer_class = PropertySerializer

class HeyHomDelete(RetrieveDestroyAPIView):
    queryset = PropertyModel
    serializer_class = PropertySerializer
