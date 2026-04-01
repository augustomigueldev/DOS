from django.db import models
from django.contrib.auth.models import User

class Tarefa(models.Model):
    PRIORIDADE_CHOICES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=500)
    data = models.DateTimeField()
    concluida = models.BooleanField(default=False)
    prioridade = models.CharField(max_length=10, choices=PRIORIDADE_CHOICES, default='media')

    def __str__(self):
        return self.titulo