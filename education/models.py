from django.contrib.auth import get_user_model
from django.db import models


class Author(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.PROTECT,
        null=False,
        verbose_name="Пользователь",
    )

    status = models.CharField(
        max_length=200,
        null=False,
        default="",
        blank=True,
        verbose_name="Статус",
    )

    bio = models.TextField(
        null=False,
        default="",
        blank=True,
        verbose_name="Биография",
    )

    def __str__(self):
        return f"{self.__class__.__name__} <{self.user}>"


class Category(models.Model):
    title = models.CharField(
        max_length=150,
        null=False,
        default="",
        blank=False,
        verbose_name="Название",
    )

    def __str__(self):
        return f"{self.__class__.__name__} <{self.title}>"


class Article(models.Model):
    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        verbose_name="Автор",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Категория",
    )

    title = models.CharField(
        max_length=150,
        null=False,
        default="",
        blank=False,
        verbose_name="Заголовок",
    )
    text = models.TextField(
        null=False,
        default="",
        blank=True,
        verbose_name="Текст статьи",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    published_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Дата публикации",
    )

    def __str__(self):
        return f"{self.__class__.__name__} <{self.title}> by {self.author}"

