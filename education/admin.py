from django.contrib import admin
from education.models import Article, Author, Category, Tag


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = "id", "user", "status"


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "category", "created_at",
                    "published_at")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "id", "title"


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = "id", "title"
