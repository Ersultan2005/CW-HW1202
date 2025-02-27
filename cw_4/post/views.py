from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Thread, Post

# --- Thread --- #

def thread_list(request):
    """
    b. /threads
    GET - отображает список Thread
    POST - создание нового Thread
    """
    if request.method == 'POST':
        # Обработка формы для создания новой темы
        name = request.POST.get('name')
        description = request.POST.get('description')
        if name:
            Thread.objects.create(name=name, description=description)
        return redirect('thread_list')

    threads = Thread.objects.all()
    return render(request, 'thread_list.html', {'threads': threads})


def thread_detail(request, thread_id):
    """
    c. /threads/:id
    GET - детали Thread и список его постов
    POST - создание Post в данной Thread
    """
    thread = get_object_or_404(Thread, pk=thread_id)

    if request.method == 'POST':
        # Создание поста
        title = request.POST.get('title')
        description = request.POST.get('description')
        author = request.POST.get('author')
        picture = request.FILES.get('picture')  # файл из формы
        if title and author:
            Post.objects.create(
                title=title,
                description=description,
                author=author,
                picture=picture,
                thread=thread
            )
        return redirect('thread_detail', thread_id=thread_id)

    posts = thread.posts.all()  # благодаря related_name='posts'
    return render(request, 'thread_detail.html', {
        'thread': thread,
        'posts': posts
    })


def thread_delete(request, thread_id):
    """
    d. /threads/:id/delete
    Удаление Thread
    """
    thread = get_object_or_404(Thread, pk=thread_id)
    thread.delete()
    return redirect('thread_list')


def thread_edit(request, thread_id):
    """
    e. /threads/:id/edit (GET, POST)
    Редактирование Thread
    """
    thread = get_object_or_404(Thread, pk=thread_id)

    if request.method == 'POST':
        thread.name = request.POST.get('name')
        thread.description = request.POST.get('description')
        thread.save()
        return redirect('thread_detail', thread_id=thread_id)

    return render(request, 'thread_edit.html', {'thread': thread})


# --- Post --- #

def post_delete(request, post_id):
    """
    f. /posts/:id/delete
    Удаление поста, редирект на /threads/:thread_id
    """
    post = get_object_or_404(Post, pk=post_id)
    thread_id = post.thread.id
    post.delete()
    return redirect('thread_detail', thread_id=thread_id)


def post_edit(request, post_id):
    """
    g. /posts/:id/edit (GET, POST)
    Редактирование поста, после -> /threads/:thread_id
    """
    post = get_object_or_404(Post, pk=post_id)
    thread_id = post.thread.id

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.description = request.POST.get('description')
        post.author = request.POST.get('author')

        # Если нужна возможность заменить файл:
        if request.FILES.get('picture'):
            post.picture = request.FILES.get('picture')

        post.save()
        return redirect('thread_detail', thread_id=thread_id)

    return render(request, 'post_edit.html', {'post': post})
