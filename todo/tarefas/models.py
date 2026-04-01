from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tarefa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=250)
    data = models.DateTimeField()
    concluida = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo