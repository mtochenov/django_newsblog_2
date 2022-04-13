from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import ContextMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import NewsForm
from .models import News, Category


class BaseMixin(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['category'] = categories
        return context


class BasePermission(UserPassesTestMixin):
    """Using UserPassesTestMixin to provide access for author or admin"""
    def test_func(self):
        news = self.get_object()
        return news.user == self.request.user or self.request.user.is_superuser


def get_category(request, category_id):
    news = News.objects.filter(category=category_id, is_published=True)
    category = Category.objects.all()
    title = Category.objects.filter(pk=category_id)[0]
    data = {'news': news, 'category': category, 'title': title}
    return render(request, 'news/news_category.html', data)


class NewsListView(BaseMixin, ListView):  # Заменяем get_context_data на класс BaseMixin где и
    model = News                          # используем метод get_context_data, а дальше наследуемся от BaseMixin

    # template_name = "news/news_list.html"  # переопределяем имя шаблона по-умолчанию, хотя в данном случае он так и называется
    # template_name по-умолчаию фомаируется так: назавание приложения в django/название модели в нижнем регистре_list.html
    context_object_name = 'news'  # переопределяем object-name, по-умолчинию - 'object_list'
    # extra_context = {'title': 'Новости'}  # Только для статичных данных
    paginate_by = 99  # определяем ограничитель количества выводимых объектов

    # ordering = ["-created_at"]  # определяем порядок сортировки, но у нас он уже задан в models.py
    # allow_empty = False  # по-умолчанию стоит в True, запрещаем показ пустых списков и вместо ошибки 500 выводится 404

    # def get_context_data(self, **kwargs):  # Тоже передает данные в шаблон
    #     context = super().get_context_data(**kwargs)
    #     categories = Category.objects.all()
    #     context['title'] = 'Новости'  # можено передавать данные в шаблон и не только статические
    #     context['category'] = categories
    #     return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)  # Задаем условия фильтрации, при необходимости


class NewsDetailView(BaseMixin, DetailView):
    model = News
    # template_name = "news/news_detail.html"  # переопределяем имя шаблона по-умолчанию, хотя в данном случае он так и называется
    context_object_name = 'news'  # переопределяем object-name, по-умолчинию - 'object'
    # вот - все что нужно для использования данного класса - это задать модель


class NewsCreateView(LoginRequiredMixin, BaseMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/news_create.html'
    login_url = reverse_lazy('registration')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NewsCreateView, self).form_valid(form)


class NewsUpdateView(BasePermission, BaseMixin, UpdateView):  # LoginRequiredMixin
    form_class = NewsForm
    model = News
    template_name = 'news/news_update.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NewsUpdateView, self).form_valid(form)


class NewsDeleteView(BasePermission, BaseMixin, DeleteView):  # LoginRequiredMixin
    model = News
    template_name = 'news/news_delete.html'
    context_object_name = 'news'

    def get_success_url(self):
        return reverse_lazy('news_list')
