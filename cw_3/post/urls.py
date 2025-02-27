from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('threads/', thread_list, name='thread_list'),
    path('threads/<int:id>/', thread_detail, name='thread_detail'),
    path('threads/<int:id>/delete/', thread_delete, name='thread_delete'),
    path('threads/<int:id>/edit/', thread_edit, name='thread_edit'),
    path('posts/<int:id>/delete/', post_delete, name='post_delete'),
    path('posts/<int:id>/edit/', post_edit, name='post_edit'),
]
