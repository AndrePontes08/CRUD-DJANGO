from django.urls import path
from .views import index,create,refresh,delete

urlpatterns = [
    path('',index,name='inicio'),
    path('criar/',create,name='criar'),
    path('modificar/<int:user_id>',refresh,name='modificar'),
    path('deletar/<int:user_id>',delete,name='deletar'),
]