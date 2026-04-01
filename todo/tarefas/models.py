from django.db import models

# Create your models here.
class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=250)
    data = models.DateTimeField()

    def __str__(self):
        return self.titulo