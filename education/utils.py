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
            in category.articles.filter(published_at__isnull=False)
        ],
    }
