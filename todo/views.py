from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoList, TodoItem
from .forms import TodoListForm, TodoItemForm

def index(request):
    """Exibe todas as listas de TO DO."""
    lists = TodoList.objects.all()
    return render(request, 'todo/index.html', {'lists': lists})

def create_list(request):
    """Cria uma nova lista de TO DO."""
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoListForm()
    return render(request, 'todo/create_list.html', {'form': form})

def list_detail(request, list_id):
    """Exibe os detalhes de uma lista específica e seus itens."""
    todo_list = get_object_or_404(TodoList, id=list_id)
    items = todo_list.itens.all()  # 'itens' é o related_name definido no modelo
    return render(request, 'todo/list_detail.html', {'todo_list': todo_list, 'items': items})

def create_item(request, list_id):
    """Cria um novo item para uma lista específica."""
    todo_list = get_object_or_404(TodoList, id=list_id)
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            todo_item = form.save(commit=False)
            todo_item.lista = todo_list
            todo_item.save()
            return redirect('list_detail', list_id=list_id)
    else:
        form = TodoItemForm()
    return render(request, 'todo/create_item.html', {'form': form, 'todo_list': todo_list})

def edit_item(request, item_id):
    """Edita um item existente."""
    todo_item = get_object_or_404(TodoItem, id=item_id)
    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=todo_item)
        if form.is_valid():
            form.save()
            return redirect('list_detail', list_id=todo_item.lista.id)
    else:
        form = TodoItemForm(instance=todo_item)
    return render(request, 'todo/edit_item.html', {'form': form, 'todo_item': todo_item})

def delete_item(request, item_id):
    """Exclui um item existente."""
    todo_item = get_object_or_404(TodoItem, id=item_id)
    list_id = todo_item.lista.id
    if request.method == 'POST':
        todo_item.delete()
        return redirect('list_detail', list_id=list_id)
    return render(request, 'todo/delete_item.html', {'todo_item': todo_item})
