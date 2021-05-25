from django.urls import path

from education import views

urlpatterns = [
    path('', views.CategoriesList.as_view(), name='categories_list'),
    path('courses/<int:course_id>/', views.CourseDetailView.as_view(),
         name='course_detail'),
    path('courses/add/', views.CourseAddView.as_view(), name='course_add'),
    path('courses/update/<int:pk>/', views.CourseUpdateView.as_view(),
         name='course_update'),
]
