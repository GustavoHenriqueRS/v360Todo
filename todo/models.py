from django.db import models

class TodoList(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class TodoItem(models.Model):
    lista = models.ForeignKey(TodoList, related_name='itens', on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    concluido = models.BooleanField(default=False)

    def __str__(self):
        return self.descricao
