from django.urls import path
from . import views


app_name = 'property'


urlpatterns = [
    path('api/list/',views.HeyHomListView.as_view()),
    path('api/create/',views.HeyHomCreateView.as_view()),
    path('api/detail/<pk>',views.HeyHomDetailView.as_view()),
    path('api/update/<pk>',views.HeyHomUpdateView.as_view()),
    path('api/delete/<pk>',views.HeyHomDelete.as_view()),
    
]