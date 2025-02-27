from django.urls import path
from .views import todo_list, todo_detail, todo_create, todo_delete

urlpatterns = [
    path("", todo_list, name="todo-list"),
    path("<int:id>/", todo_detail, name="todo-detail"),
    path("create/", todo_create, name="todo-create"),
    path("<int:id>/delete/", todo_delete, name="todo-delete"),
]
