from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import ContextMixin

from .forms import NewsForm
from .models import News, Category


class BaseMixin(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['category'] = categories
        return context


def get_category(request, category_id):
    news = News.objects.filter(category=category_id, is_published=True)
    category = Category.objects.all()
    title = Category.objects.filter(pk=category_id)[0]
    data = {'news': news, 'category': category, 'title': title}
    return render(request, 'news/news_category.html', data)


class NewsListView(BaseMixin, ListView):
    model = News
    context_object_name = "news"
    paginate_by = 99

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class NewsDetailView(BaseMixin, DetailView):
    model = News
    context_object_name = "news"


class NewsCreateView(BaseMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/news_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NewsCreateView, self).form_valid(form)


class NewsUpdateView(BaseMixin, UpdateView):
    form_class = NewsForm
    model = News
    template_name = 'news/news_update.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NewsUpdateView, self).form_valid(form)


class NewsDeleteView(BaseMixin, DeleteView):
    model = News
    template_name = 'news/news_delete.html'
    context_object_name = 'news'

    def get_success_url(self):
        return reverse_lazy('news_list')
