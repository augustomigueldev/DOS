from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Tarefa


@login_required
def listarTarefas(request):
    filtro = request.GET.get('filtro', 'todas')
    tarefas = Tarefa.objects.filter(usuario=request.user)

    if filtro == 'pendentes':
        tarefas = tarefas.filter(concluida=False)
    elif filtro == 'concluidas':
        tarefas = tarefas.filter(concluida=True)

    tarefas = tarefas.order_by('concluida', 'data')

    return render(request, "listarTarefas.html", {'tarefas': tarefas, 'filtro': filtro})


@login_required
def cadastrarTarefa(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        data_str = request.POST.get('data')
        prioridade = request.POST.get('prioridade', 'media')

        ano, mes, dia = map(int, data_str.split('-'))
        data = datetime(ano, mes, dia)

        Tarefa.objects.create(
            usuario=request.user,
            titulo=titulo,
            descricao=descricao,
            data=data,
            prioridade=prioridade,
        )
        return redirect('listarTarefas')

    return render(request, "cadastroTarefa.html")


@login_required
def detalharTarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk, usuario=request.user)
    return render(request, "detalharTarefa.html", {'tarefa': tarefa})


@login_required
def editarTarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk, usuario=request.user)

    if request.method == "POST":
        tarefa.titulo = request.POST.get('titulo')
        tarefa.descricao = request.POST.get('descricao')
        tarefa.prioridade = request.POST.get('prioridade', 'media')
        tarefa.concluida = request.POST.get('concluida') == 'on'

        data_str = request.POST.get('data')
        ano, mes, dia = map(int, data_str.split('-'))
        tarefa.data = datetime(ano, mes, dia)

        tarefa.save()
        return redirect('detalharTarefa', pk=tarefa.pk)

    return render(request, "editarTarefa.html", {'tarefa': tarefa})


@login_required
def concluirTarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk, usuario=request.user)
    tarefa.concluida = True
    tarefa.save()
    return redirect('listarTarefas')


@login_required
def reabrirTarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk, usuario=request.user)
    tarefa.concluida = False
    tarefa.save()
    return redirect('listarTarefas')


@login_required
def excluirTarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk, usuario=request.user)
    tarefa.delete()
    return redirect('listarTarefas')


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