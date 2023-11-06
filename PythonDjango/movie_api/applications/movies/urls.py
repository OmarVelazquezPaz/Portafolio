from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import MovieViewSet,ActionViewSet,ComedyViewSet

app_name = 'movies'

router = routers.SimpleRouter()
router.register('movies',MovieViewSet)
router.register('action',ActionViewSet)
router.register('comedy',ComedyViewSet)

urlpatterns = [
    path('',include(router.urls)),
]