from django.urls import path, include
from .views import listarTarefas, cadastrarTarefa, cadastrarUsuario

urlpatterns = [
    path('listartarefas', listarTarefas, name='listarTarefas'),
    path('cadastrarTarefa', cadastrarTarefa, name='cadastrarTarefa'),
    path('cadastrarUsuario', cadastrarUsuario, name='cadastrarUsuario'),
    path('contas/', include('django.contrib.auth.urls')),
]
