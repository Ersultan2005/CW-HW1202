from django.urls import path
from .views import index, login_view, authenticate_user, logout_view, todos_list, todo_detail, create_todo, delete_todo

urlpatterns = [
    path('', index, name='index'),  # Теперь пустой URL будет работать
    path('login/', login_view, name='login'),
    path('authenticate/', authenticate_user, name='authenticate'),
    path('logout/', logout_view, name='logout'),
    path('todos/', todos_list, name='todos_list'),
    path('todos/<int:todo_id>/', todo_detail, name='todo_detail'),
    path('todos/add/', create_todo, name='create_todo'),
    path('todos/<int:todo_id>/delete/', delete_todo, name='delete_todo'),
]
