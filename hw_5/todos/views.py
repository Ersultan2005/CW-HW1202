from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Todo
from .forms import TodoForm
from django.shortcuts import redirect

def index(request):
    return redirect('login')  # Или 'todos_list', если пользователь уже авторизован

# Страница логина
def login_view(request):
    return render(request, 'todos/login.html')

# Аутентификация пользователя
def authenticate_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('todos_list')
    return redirect('login')

# Выход пользователя
def logout_view(request):
    logout(request)
    return redirect('login')

# Список todo (только для авторизованного пользователя)
@login_required
def todos_list(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todos/todos_list.html', {'todos': todos})

# Просмотр одного todo
@login_required
def todo_detail(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    return render(request, 'todo_detail.html', {'todo': todo})

# Добавление todo
@login_required
def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todos_list')
    else:
        form = TodoForm()
    return render(request, 'todos/create_todo.html', {'form': form})  # Добавьте `todos/`

# Удаление todo
@login_required
def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.delete()
    return redirect('todos_list')
