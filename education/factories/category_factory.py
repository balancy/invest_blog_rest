import factory
from factory.django import DjangoModelFactory

from education.models import Category


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    title = factory.Faker("word")
