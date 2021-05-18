from django.urls import path
from education import views

urlpatterns = [
    path('', views.articles_list),
]
