from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Добро пожаловать в API!</h1><p>Доступные эндпоинты:</p><ul>"
                        "<li><a href='/todos/'>/todos/</a> - Список задач</li>"
                        "<li><a href='/admin/'>/admin/</a> - Админ-панель</li>"
                        "</ul>")

urlpatterns = [
    path("", home, name="home"),  # Главная страница
    path("admin/", admin.site.urls),
    path("todos/", include("todos.urls")),
]
