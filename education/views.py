from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from education.models import Category, Course, Lesson, Mentor
from education.permissions import IsAdminUserOrReadOnlyPermission
from education.serializers import (
    CategorySerializer,
    CourseSerializer,
    LessonSerializer,
    MentorSerializer,
)


class IsAdminOrReadOnlyViewSet:
    permission_classes = [
        IsAdminUserOrReadOnlyPermission,
    ]


class LessonsViewSet(ModelViewSet, IsAdminOrReadOnlyViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['mentor', 'course', 'tags', 'title']
    ordering_fields = ['title', 'id']


class MentorsViewSet(ModelViewSet, IsAdminOrReadOnlyViewSet):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer


class CoursesViewSet(ModelViewSet, IsAdminOrReadOnlyViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['responsible', 'category', 'title']
    ordering_fields = ['title', 'id']


class CategoriesViewSet(ModelViewSet, IsAdminOrReadOnlyViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
