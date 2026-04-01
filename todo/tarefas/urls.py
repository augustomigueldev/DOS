from django.urls import path, include
from .views import (
    listarTarefas, cadastrarTarefa, detalharTarefa,
    editarTarefa, concluirTarefa, reabrirTarefa,
    excluirTarefa, cadastrarUsuario
)

urlpatterns = [
    path('listartarefas', listarTarefas, name='listarTarefas'),
    path('cadastrarTarefa', cadastrarTarefa, name='cadastrarTarefa'),
    path('tarefa/<int:pk>/', detalharTarefa, name='detalharTarefa'),
    path('tarefa/<int:pk>/editar/', editarTarefa, name='editarTarefa'),
    path('tarefa/<int:pk>/concluir/', concluirTarefa, name='concluirTarefa'),
    path('tarefa/<int:pk>/reabrir/', reabrirTarefa, name='reabrirTarefa'),
    path('tarefa/<int:pk>/excluir/', excluirTarefa, name='excluirTarefa'),
    path('cadastrarUsuario', cadastrarUsuario, name='cadastrarUsuario'),
    path('contas/', include('django.contrib.auth.urls')),
]
