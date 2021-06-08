from django.urls import path, include
from rest_framework.routers import DefaultRouter

from education import views

router = DefaultRouter()
router.register('lessons', views.LessonsViewSet)
router.register('mentors', views.MentorsViewSet)
router.register('courses', views.CoursesViewSet)
router.register('categories', views.CategoriesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
