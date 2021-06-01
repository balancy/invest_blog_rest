import factory
from factory.django import DjangoModelFactory

from education.factories.user_factory import UserFactory
from education.models import Mentor


class MentorFactory(DjangoModelFactory):
    class Meta:
        model = Mentor

    status = factory.Faker("sentence")
    user = factory.SubFactory(UserFactory)
    bio = factory.Faker("text")
