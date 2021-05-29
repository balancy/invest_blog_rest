import pytest
from django.contrib.auth import get_user_model
from django.test import TestCase


@pytest.mark.django_db
class UserTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user_model = get_user_model()

    def test_create_user(self):
        default_user = self.user_model.objects.create(
            first_name='user1',
            email='user1@gmail.com',
            username='user1',
            password='pass'
        )

        self.assertEqual('user1@gmail.com', default_user.email)
        assert default_user.is_active
        assert not default_user.is_staff
        assert not default_user.is_superuser

    def test_create_wrong_user(self):
        with pytest.raises(TypeError):
            self.user_model.objects.create_user()
        with pytest.raises(TypeError):
            self.user_model.objects.create_user(email='')
        with pytest.raises(TypeError):
            self.user_model.objects.create_user(
                first_name='Someone',
                email='', password='pass'
            )

    def test_create_superuser(self):
        self.admin_user = self.user_model.objects.create_superuser(
            first_name='SuperAdmin',
            email='admin@gmail.com',
            username='admin',
            password='pass'
        )

        assert self.admin_user.email == 'admin@gmail.com'
        assert self.admin_user.is_active
        assert self.admin_user.is_staff
        assert self.admin_user.is_superuser

    def test_create_wrong_superuser(self):
        with pytest.raises(TypeError):
            self.user_model.objects.create_superuser(
                first_name='Super1',
                email='', password='pass')

