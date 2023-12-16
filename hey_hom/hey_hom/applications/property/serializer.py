from rest_framework import serializers,pagination
from .models import PropertyModel

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyModel
        fields = '__all__'

class PropertyPagination(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 10