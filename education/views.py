from django.http import HttpRequest
from django.shortcuts import render

from education.models import Author


def articles_list(request: HttpRequest):
    authors = Author.objects.all()

    context = {
        "authors": authors,
    }
    return render(request, "education/authors_list.html", context=context)
