"""
post/views.py
"""
from django.shortcuts import render, get_object_or_404, redirect
from .models import Thread, Post
from .forms import ThreadForm, PostForm

def home(request):
    # Перенаправляем на список тем
    return redirect('thread_list')

def thread_list(request):
    # Выводим все Thread + форма создания Thread
    threads = Thread.objects.all()
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thread_list')
    else:
        form = ThreadForm()
    return render(request, 'post/thread_list.html', {'threads': threads, 'form': form})

def thread_detail(request, id):
    # Детальная страница Thread + список Post
    thread = get_object_or_404(Thread, pk=id)
    posts = Post.objects.filter(thread=thread)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.thread = thread
            new_post.save()
            return redirect('thread_detail', id=id)
    else:
        form = PostForm()
    return render(request, 'post/thread_detail.html', {
        'thread': thread,
        'posts': posts,
        'form': form
    })

def thread_edit(request, id):
    # Редактирование Thread
    thread = get_object_or_404(Thread, pk=id)
    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('thread_detail', id=thread.id)
    else:
        form = ThreadForm(instance=thread)
    return render(request, 'post/thread_edit.html', {'form': form, 'thread': thread})

def thread_delete(request, id):
    # Удаление Thread
    thread = get_object_or_404(Thread, pk=id)
    thread.delete()
    return redirect('thread_list')

def post_edit(request, id):
    # Редактирование Post
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('thread_detail', id=post.thread.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'post/post_edit.html', {'form': form, 'post': post})

def post_delete(request, id):
    # Удаление Post
    post = get_object_or_404(Post, pk=id)
    thread_id = post.thread.id
    post.delete()
    return redirect('thread_detail', id=thread_id)
