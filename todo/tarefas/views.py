from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Tarefa

@login_required
def listarTarefas(request):
    tarefas = Tarefa.objects.filter(usuario=request.user).order_by('data')

    return render(
        request, 
        "listarTarefas.html", 
        {'tarefas' : tarefas}
    )

@login_required
def cadastrarTarefa(request):

    if(request.method == "POST"):
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        ano = int(request.POST.get('data').split('-')[0])
        mes = int(request.POST.get('data').split('-')[1])
        dia = int(request.POST.get('data').split('-')[2])
        data = datetime(ano, mes, dia)

        nova_tarefa = Tarefa(
            usuario=request.user,
            titulo=titulo,
            descricao=descricao,
            data=data
        )
        nova_tarefa.save()
        return redirect('listarTarefas')

    return render(request, "cadastroTarefa.html")

def cadastrarUsuario(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('listarTarefas')
    else:
        form = UserCreationForm()
    return render(request, 'cadastroUsuario.html', {'form': form})