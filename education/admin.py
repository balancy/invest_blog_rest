from django.contrib import admin
from education.models import Article, Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = "id", "user", "status"


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass
