from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Todo
from .forms import TodoForm


def todo_list(request):
    todos = list(Todo.objects.values())
    response = JsonResponse(todos, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
    response['Content-Type'] = 'application/json; charset=utf-8'
    return response

def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id)
    response = JsonResponse({
        "id": todo.id,
        "title": todo.title,
        "description": todo.description,
        "due_date": str(todo.due_date),
        "status": todo.status
    }, json_dumps_params={'ensure_ascii': False, 'indent': 4})
    response['Content-Type'] = 'application/json; charset=utf-8'
    return response

def todo_create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo-list")
    else:
        form = TodoForm()
    return render(request, "todos/todo_form.html", {"form": form})

def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect("todo-list")

def todo_list(request):
  todos = Todo.objects.all()
  return render(request, "todos/todo_list.html", {"todos": todos})