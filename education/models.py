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
