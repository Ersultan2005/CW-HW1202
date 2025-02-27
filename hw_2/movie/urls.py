from django.urls import path
from .views import MovieListView, MovieDetailView, MovieListHTMLView

urlpatterns = [
    path('', MovieListView.as_view(), name='movie-list'),  
    path('html/', MovieListHTMLView.as_view(), name='movie-list-html'),  
    path('<int:id>/', MovieDetailView.as_view(), name='movie-detail'), 
]
