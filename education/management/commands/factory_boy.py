from django.core.management import BaseCommand

from education.factories.course_factory import CourseFactory


def create_all():
    courses = CourseFactory.create_batch(3)
    print(courses)


class Command(BaseCommand):
    help = "Create data using factory-boy"

    def handle(self, *args, **options):
        create_all()