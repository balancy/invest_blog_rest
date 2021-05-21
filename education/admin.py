from django.contrib import admin

from education.models import Article, Mentor, Category, Comment, Tag


@admin.register(Mentor)
class AuthorAdmin(admin.ModelAdmin):
    list_display = "id", "user", "status"


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "category", "created_at",
                    "published_at")
    raw_id_fields = "author", "category", "tags"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "id", "title"


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = "id", "title"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = "id", "author", "article", "published_at"
    raw_id_fields = "author", "article"
