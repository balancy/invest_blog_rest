import pytest
from django.test import TestCase
from mixer.backend.django import mixer

from education.models import Mentor


@pytest.mark.django_db
class EducationTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        self.number_of_mentors = 2
        self.status_tuple = 'The Great', 'The Terrible'
        self.mentors = mixer.cycle(self.number_of_mentors).blend(
            Mentor,
            status=(status for status in self.status_tuple),
            bio="New bio",
        )

    def test_mentors_bio(self):
        for mentor in self.mentors:
            self.assertEqual("New bio", mentor.bio)

    def test_mentors_status(self):
        for mentor in self.mentors:
            self.assertIn(mentor.status, self.status_tuple)

    def test_mentors_number(self):
        self.assertTrue(self.number_of_mentors, len(self.mentors))

    def test_mentors_are_different_users(self):
        self.assertNotEqual(self.mentors[0].user, self.mentors[1].user)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
