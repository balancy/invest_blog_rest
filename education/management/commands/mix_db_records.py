from django.core.management import BaseCommand
from faker import Faker
from mixer.backend.django import mixer

from education.models import Course

fake = Faker()


class Command(BaseCommand):
    def handle(self, *args, **options):
        mixer.cycle(3).blend(
            Course,
            title=fake.word,
            description=fake.text,
            category__title=fake.word,
            responsible__status=fake.sentence
        )
