from datetime import datetime
from django.shortcuts import render
from .models import Tarefa

def listarTarefas(request):
    tarefas = Tarefa.objects.all()

    return render(
        request, 
        "listarTarefas.html", 
        {'tarefas' : tarefas}
    )

def cadastrarTarefa(request):

    if(request.method == "POST"):
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        ano = int(request.POST.get('data').split('-')[0])
        mes = int(request.POST.get('data').split('-')[1])
        dia = int(request.POST.get('data').split('-')[2])
        data = datetime(ano, mes, dia)

        nova_tarefa = Tarefa(titulo=titulo,
                             descricao=descricao,
                             data = data
                             )
        nova_tarefa.save()

    return render(request, "cadastroTarefa.html")