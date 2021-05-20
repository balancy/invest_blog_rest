from django.http import HttpRequest
from django.shortcuts import render

from education.models import Category, Tag
from education.utils import serialize_category, serialize_tag_with_count


def articles_list(request: HttpRequest):
    categories = Category.objects.order_by("-title")
    popular_tags = Tag.objects.popular()[:5]

    context = {
        "categories": [serialize_category(category) for category in categories],
        "title": "Список статей",
        "tags": [serialize_tag_with_count(tag) for tag in popular_tags],
    }
    return render(request, "education/articles_list.html", context=context)
