from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView

from education.forms import CourseCreateForm
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


@method_decorator(staff_member_required, name='dispatch')
class CourseAddView(CreateView):
    model = Course
    form_class = CourseCreateForm
    success_url = reverse_lazy('categories_list')
    template_name_suffix = '_create_form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить курс'
        return context
