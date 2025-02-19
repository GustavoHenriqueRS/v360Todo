from django.db import models
import datetime

class User(models.Model):
    email = models.EmailField(max_length=255, unique=True)

    def __str__(self):
        return self.email

class TodoList(models.Model):
    user = models.ForeignKey(User, related_name='todo_lists', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    dia = models.DateField(default=datetime.date.today())

    def __str__(self):
        return self.nome

class TodoItem(models.Model):
    lista = models.ForeignKey(TodoList, related_name='itens', on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    concluido = models.BooleanField(default=False)
    hora = models.TimeField(default=datetime.time(hour=0, minute=0))

    def __str__(self):
        return self.descricao
