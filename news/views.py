from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from .forms import NewsForm
from .models import News, Category

from rest_framework import generics, viewsets

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import NewsSerializer


class NewsListView(ListView):
    model = News
    # template_name = "news/news_list.html"  # переопределяем имя шаблона по-умолчанию, хотя в данном случае он так и называется
    # template_name по-умолчаию фомаируется так: назавание приложения в django/название модели в нижнем регистре_list.html
    context_object_name = "news"  # переопределяем object-name, по-умолчинию - 'object_list'
    # extra_context = {'title': 'Новости'}  # Только для статичных данных
    paginate_by = 99  # определяем ограничитель количества выводимых объектов
    # ordering = ["-created_at"]  # определяем порядок сортировки, но у нас он уже задан в models.py
    # allow_empty = False  # по-умолчанию стоит в True, запрещаем показ пустых списков и вместо ошибки 500 выводится 404

    def get_context_data(self, **kwargs):  # Тоже передает данные в шаблон
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['title'] = 'Новости'  # можено передавать данные в шаблон и не только статические
        context['category'] = categories
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)  # Задаем условия фильтрации, при необходимости


def get_category(request, category_id):
    news = News.objects.filter(category=category_id, is_published=True)
    category = Category.objects.all()
    title = Category.objects.filter(pk=category_id)[0]
    data = {'news': news, 'category': category, 'title': title}
    return render(request, 'news/category.html', data)


class NewsDetailView(DetailView):
    model = News
    # template_name = "news/news_detail.html"  # переопределяем имя шаблона по-умолчанию, хотя в данном случае он так и называется
    context_object_name = "news"  # переопределяем object-name, по-умолчинию - 'object'
    # вот - все что нужно для использования данного класса - это задать модель


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            new_news = News.objects.create(**form.cleaned_data)  # Распаковка словаря
            return redirect(new_news)
    else:
        form = NewsForm()
    category = Category.objects.all()
    data = {'form': form, 'category': category}
    return render(request, 'news/add_news.html', data)

# Ниже указаны представления для API


# class NewsListAPIView(generics.ListAPIView):  # Обычное представление для API
#     queryset = News.objects.all()             # без указания прав доступа
#     serializer_class = NewsSerializer
#
#
# class NewsViewSet(viewsets.ModelViewSet):  # Представление для API
#     queryset = News.objects.all()          # с подключением routers в url
#     serializer_class = NewsSerializer      # для автоматической подстановки адреса в url


class NewsAPIList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class NewsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsOwnerOrReadOnly, )  # this class include IsAdminUser class


class NewsAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAdminOrReadOnly, )
