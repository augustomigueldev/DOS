from django.urls import path
from .views import listarTarefas, cadastrarTarefa

urlpatterns = [
    path('listartarefas', listarTarefas),
    path('cadastrarTarefa', cadastrarTarefa),
]
