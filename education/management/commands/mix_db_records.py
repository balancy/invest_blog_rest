from django.core.management import BaseCommand
from mixer.backend.django import mixer

from education.models import Category, Course, Mentor


class Command(BaseCommand):
    def handle(self, *args, **options):
        mentor = mixer.blend(
            Mentor,
            bio="Новая биография",
            status="Огнерожденый",
        )

        category = Category.objects.first()

        course = mixer.blend(
            Course,
            category=category,
            responsible=mentor,
            title="Новый курс",
        )
        print(course)
        print(vars(course))

