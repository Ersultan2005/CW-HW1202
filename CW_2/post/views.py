from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

def posts(request):
    """
    Обрабатывает два случая:
    - GET-запрос: вывод списка постов и формы для создания нового.
    - POST-запрос: создание нового поста через Django Form.
    """
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')  
    else:
        form = PostForm()
    posts_list = Post.objects.all()
    return render(request, 'post/posts.html', {'posts': posts_list, 'form': form})

def post_detail(request, id):
    """Вывод подробной информации о конкретном посте."""
    post_obj = get_object_or_404(Post, id=id)
    return render(request, 'post/post_detail.html', {'post': post_obj})

def post_delete(request, id):
    """
    Удаление поста.
    Для безопасности удаление выполняется через POST-запрос (HTML-форма с кнопкой Delete).
    После удаления выполняется редирект (здесь на страницу posts – её можно считать страницей todos).
    """
    post_obj = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post_obj.delete()
        return redirect('posts')  # редирект на список постов (страница todos)
    return render(request, 'post/post_confirm_delete.html', {'post': post_obj})
