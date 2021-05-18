from django.http import HttpRequest
from django.shortcuts import render

from education.models import Author


def articles_list(request: HttpRequest):
    articles = Article.objects.all()

    context = {
        "article": articles,
    }
    return render(request, "education/articles_list.html", context=context)
