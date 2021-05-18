from django.http import HttpRequest
from django.shortcuts import render

from education.models import Article


def articles_list(request: HttpRequest):
    articles = Article.objects.all()

    context = {
        "articles": articles,
        "title": "Список статей",
    }
    return render(request, "education/articles_list.html", context=context)
