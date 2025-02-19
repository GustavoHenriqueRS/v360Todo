from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList, TodoItem, User
from .forms import TodoListForm, TodoItemForm, UserForm

def user_email_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user, created = User.objects.get_or_create(email=email)
            return redirect(f'/user_todo_lists/?email={email}')
    else:
        form = UserForm()
    
    return render(request, 'todo/user_email.html', {'form': form})

def user_todo_lists(request):
    email = request.GET.get('email')
    
    if not email:
        return render(request, 'todo/user_todo_lists.html', {
            'error': 'Por favor, forneça um email para a busca.'
        })
    
    user, created = User.objects.get_or_create(email=email)
    
    lists = user.todo_lists.all()
    
    return render(request, 'todo/user_todo_lists.html', {
        'user': user,
        'lists': lists,
    })

def create_list(request):
    email = request.GET.get('email')
    if not email:
        return redirect('user_email')
    
    user, created = User.objects.get_or_create(email=email)
    
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            todo_list = form.save(commit=False)
            todo_list.user = user  
            todo_list.save()
            return redirect('list_detail', list_id=todo_list.id)
    else:
        form = TodoListForm()
    
    return render(request, 'todo/create_list.html', {'form': form, 'user_email': user.email})

def list_detail(request, list_id):
    todo_list = get_object_or_404(TodoList, id=list_id)
    items = todo_list.itens.all()  
    return render(request, 'todo/list_detail.html', {'todo_list': todo_list, 'items': items})

def delete_list(request, list_id):
    todo_list = get_object_or_404(TodoList, id=list_id)
    if request.method == 'POST':
        todo_list.delete()
        return redirect(f'/user_todo_lists/?email={todo_list.user.email}')
    return render(request, 'todo/delete_list.html', {'todo_list': todo_list})

def create_item(request, list_id):
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
    todo_item = get_object_or_404(TodoItem, id=item_id)
    list_id = todo_item.lista.id
    if request.method == 'POST':
        todo_item.delete()
        return redirect('list_detail', list_id=list_id)
    return render(request, 'todo/delete_item.html', {'todo_item': todo_item})
