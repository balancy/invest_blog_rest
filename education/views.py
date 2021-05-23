from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from education.models import Category, Course, Tag
from education.utils import serialize_category, serialize_tag_with_count


def articles_list(request: HttpRequest):
    categories = Category.objects.order_by("-title")
    popular_tags = Tag.objects.popular()[:5]

    context = {
        "categories": [serialize_category(category) for category in categories],
        "title": "Список статей",
        "tags": [serialize_tag_with_count(tag) for tag in popular_tags],
    }
    return render(request, "education/articles_list.html", context=context)


class CategoriesList(ListView):
    model = Category
    title = 'Список курсов'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class CourseDetailView(DetailView):
    model = Course
    pk_url_kwarg = 'course_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = kwargs['object'].title
        return context
