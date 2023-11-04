from . import views
from django.urls import path

app_name = 'food'

urlpatterns =[
    # Index
    # path('',views.index,name='index'),
    path('',views.IndexClassView.as_view(),name='index'),
    path('item/',views.item,name='item'),
    # Detail
    # food/1
    # path('<int:item_id>/',views.detail,name='detail'),
    path('<int:pk>/',views.FoodDetailView.as_view(),name='detail'),
    # add items
    # path('add',views.create_item,name='create_item'),
    path('add',views.CreateItemVire.as_view(),name='create_item'),
    # edit
    path('update/<int:id>/',views.update_item,name='update_item'),
    # delete
    path('delete/<int:id>',views.delete_item,name='delete_item'),
]