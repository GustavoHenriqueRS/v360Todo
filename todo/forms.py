from django import forms
from .models import TodoList, TodoItem, User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'appearance-none border rounded w-full py-4 px-4 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-xl tracking-wider',
                'placeholder': 'Digite seu email',
            }),
        }
    
    def validate_unique(self):
        pass

    def clean_email(self):
        return self.cleaned_data.get('email')

class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['nome', 'dia']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'appearance-none border rounded w-full py-4 px-4 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-xl tracking-widest',
                'placeholder': 'Digite o nome da lista',
            }),
            'dia': forms.DateInput(
                format='%d/%m/%Y',  
                attrs={
                    'class': 'appearance-none border rounded w-full py-4 px-4 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-xl tracking-widest',
                    'placeholder': 'Digite a data da lista',
                    'type': 'date', 
                }
            ),
        }

class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['descricao', 'concluido', 'hora']
        widgets = {
            'descricao': forms.TextInput(attrs={
                'class': 'appearance-none border rounded w-full py-4 px-4 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-xl tracking-wider',
                'placeholder': 'Digite o item',
            }),
            'concluido': forms.CheckboxInput(attrs={
                'class': 'appearance-none focus:outline-none focus:ring-0 border rounded p-3 text-gray-700 leading-tight outline-none focus:shadow-outline text-xl tracking-widest',
                'placeholder': 'Digite o item',
            }),
            'hora': forms.TimeInput(
                format='%H:%M',
                attrs={
                'class': 'appearance-none border rounded w-full py-4 px-4 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-xl tracking-widest',
                'placeholder': 'Digite a hora do item',
                'type': 'time',
                "step": "60",
                "placeholder": "00:00",
                "lang": "pt-BR",
            }),
        }
