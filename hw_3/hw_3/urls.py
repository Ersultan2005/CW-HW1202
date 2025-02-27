from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def home(request):
    return render(request, "home.html")   # Тут важно, чтобы путь был таким

urlpatterns = [
    path("", home, name="home"),
    path("todos/", include("todos.urls")),
    path("admin/", admin.site.urls),
]
