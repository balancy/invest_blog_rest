from rest_framework.viewsets import ModelViewSet

from education.models import Category, Course, Lesson, Mentor
from education.serializers import (
    CategorySerializer,
    CourseSerializer,
    LessonSerializer,
    MentorSerializer,
)


class LessonsViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class MentorsViewSet(ModelViewSet):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer


class CoursesViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CategoriesViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
