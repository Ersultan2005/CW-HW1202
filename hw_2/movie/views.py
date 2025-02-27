from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.views import View
from .models import Movie


class MovieListView(View):
    def get(self, request):
        movies = list(Movie.objects.values())
        return JsonResponse(movies, safe=False, json_dumps_params={'indent': 4})


class MovieListHTMLView(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, "movie/movie_list.html", {"movies": movies})

class MovieDetailView(View):
    def get(self, request, id):
        movie = get_object_or_404(Movie, id=id)
        return JsonResponse({
            "id": movie.id,
            "title": movie.title,
            "description": movie.description,
            "producer": movie.producer,
            "duration": movie.duration
        }, json_dumps_params={'indent': 4})
