from django.urls import path
from . import views

urlpatterns = [
    # b. /threads - список тем (GET), + форма для создания Thread (POST) в модальном окне
    path('threads', views.thread_list, name='thread_list'),

    # c. /threads/<int:id> - детали Thread (GET), + посты; форма для создания Post (POST)
    path('threads/<int:thread_id>', views.thread_detail, name='thread_detail'),

    # d. /threads/<int:id>/delete
    path('threads/<int:thread_id>/delete', views.thread_delete, name='thread_delete'),

    # e. /threads/<int:id>/edit (GET, POST)
    path('threads/<int:thread_id>/edit', views.thread_edit, name='thread_edit'),

    # f. /posts/<int:post_id>/delete
    path('posts/<int:post_id>/delete', views.post_delete, name='post_delete'),

    # g. /posts/<int:post_id>/edit (GET, POST)
    path('posts/<int:post_id>/edit', views.post_edit, name='post_edit'),
]
