import factory
from django.contrib.auth.models import User
from factory.django import DjangoModelFactory


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker("email")
    username = factory.Faker("user_name")
    password = factory.PostGenerationMethodCall(
        'set_password',
        str(factory.Faker("word")),
    )

    is_superuser = False
    is_staff = True
    is_active = True
