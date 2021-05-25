from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from education.forms import CourseForm
from education.models import Category, Course


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


class CourseTitleMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


@method_decorator(staff_member_required, name='dispatch')
class CourseAddView(CourseTitleMixin, CreateView):
    model = Course
    form_class = CourseForm
    title = 'Добавить курс'
    success_url = reverse_lazy('categories_list')


@method_decorator(staff_member_required, name='dispatch')
class CourseUpdateView(CourseTitleMixin, UpdateView):
    model = Course
    form_class = CourseForm
    title = 'Обновить курс'
    success_url = reverse_lazy('categories_list')


@method_decorator(staff_member_required, name='dispatch')
class CourseDeleteView(CourseTitleMixin, DeleteView):
    model = Course
    title = 'Удалить курс'
    success_url = reverse_lazy('categories_list')
    template_name_suffix = '_delete'
