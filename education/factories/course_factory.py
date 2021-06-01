import factory
from factory.django import DjangoModelFactory

from education.factories.category_factory import CategoryFactory
from education.factories.mentor_factory import MentorFactory
from education.models import Course


class CourseFactory(DjangoModelFactory):
    class Meta:
        model = Course

    category = factory.SubFactory(CategoryFactory)
    responsible = factory.SubFactory(MentorFactory)
    title = factory.Faker("sentence")
    description = factory.Faker("text")
