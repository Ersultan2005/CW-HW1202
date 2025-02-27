from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.views import View
from .models import Article


class ArticleListView(View):
    def get(self, request):
        articles = list(Article.objects.values())
        return JsonResponse(articles, safe=False, json_dumps_params={'indent': 4})


class ArticleListHTMLView(View):
    def get(self, request):
        articles = Article.objects.all()
        return render(request, "article_list.html", {"articles": articles})


class ArticleDetailView(View):
    def get(self, request, id):
        article = get_object_or_404(Article, id=id)
        return JsonResponse({
            "id": article.id,
            "title": article.title,
            "text": article.text,
            "author": article.author
        }, json_dumps_params={'indent': 4})
