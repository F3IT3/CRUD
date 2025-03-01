from django.urls import path
from .views import *

app_name = 'app'

urlpatterns = [
    path('criar/', criar_view, name='criar'),
    path('listar/', listar_view, name='listar'),
    path('atualizar/<int:pk>', atualizar_view, name='atualizar'),
    path('deletar/<int:pk>', deletar_view, name='deletar'),
    path('detalhes/<int:pk>', detalhes_view, name='detalhes'),
]