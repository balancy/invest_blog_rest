from rest_framework import serializers

from .models import Category, Course, Lesson, Mentor


class LessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lesson
        fields = "id", "mentor", "course", "title", "description", "text"
        view_name = "lessons"


class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = "id", "user", "status", "bio"
        view_name = "mentors"


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = "id", "responsible", "category", "title", "description"
        view_name = "courses"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "id", "title"
        view_name = "categories"
