from django import forms
from .models import TodoList, TodoItem, User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']
    
    def validate_unique(self):
        pass

    def clean_email(self):
        return self.cleaned_data.get('email')

class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['nome', 'dia']

class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['descricao', 'concluido', 'hora']
