import pytest
from django.test import TestCase

from education.factories.course_factory import CourseFactory


@pytest.mark.django_db
class EducationTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        self.status_tuple = 'The Great', 'The Terrible'
        self.courses = CourseFactory.create_batch(3)

    def test_courses_titles_are_not_empty(self):
        for course in self.courses:
            self.assertIsNotNone(course.title)

    def test_courses_responsibles_are_different(self):
        responsibles = [course.responsible for course in self.courses]
        self.assertEqual(len(set(responsibles)), len(responsibles))

    def test_responsibles_are_staff(self):
        are_staff = [
            course.responsible.user.is_staff for course in self.courses
        ]
        self.assertTrue(all(are_staff))

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
