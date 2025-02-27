from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),                     
    path('<int:id>/', views.post_detail, name='post_detail'),    
    path('<int:id>/delete/', views.post_delete, name='post_delete'),  
]
