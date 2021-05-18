from django.contrib.auth import get_user_model
from django.db import models


class Author(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.PROTECT,
        null=False,
    )

    status = models.CharField(
        max_length=200,
        null=False,
        default="",
        blank=True,
    )

    bio = models.TextField(null=False, default="", blank=True)

    def __str__(self):
        return f"{self.__class__.__name__} <{self.user}>"


class Category(models.Model):
    title = models.CharField(max_length=150, null=False, default="", blank=False)

    def __str__(self):
        return f"{self.__class__.__name__} <{self.title}>"


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=150, null=False, default="", blank=False)
    text = models.TextField(null=False, default="", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.__class__.__name__} <{self.title}> by {self.author}"

