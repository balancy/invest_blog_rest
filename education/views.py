from django.http import HttpRequest
from django.shortcuts import render

from education.models import Article, Category, Tag


def serialize_tag_with_count(tag):
    return {
        "title": tag.title,
        "articles_count":
            tag.articles_count if hasattr(tag, "articles_count") else 0,
    }


def serialize_tag(tag):
    return {
        "title": tag.title,
    }


def serialize_article(article):
    return {
        "title": article.title,
        "published_at": article.published_at,
        "author": article.author,
        "text": article.text,
        "tags": [serialize_tag(tag) for tag in article.tags.all()],
    }


def serialize_category(category):
    return {
        "title": category.title,
        "articles": [
            serialize_article(article) for article
            in Article.objects.filter(
                category=category,
                published_at__isnull=False,
            )
        ],
    }


def articles_list(request: HttpRequest):
    categories = Category.objects.order_by("-title")
    popular_tags = Tag.objects.popular()[:5]

    context = {
        "categories": [serialize_category(category) for category in categories],
        "title": "Список статей",
        "tags": [serialize_tag_with_count(tag) for tag in popular_tags],
    }
    return render(request, "education/articles_list.html", context=context)
