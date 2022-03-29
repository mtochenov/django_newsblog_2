from django.test import TestCase
from django.urls import reverse, resolve
from .models import News, Category
from .views import *


class TestUrls(TestCase):

    def test_category_resolved(self):
        url = reverse('category', kwargs={'category_id': 1})
        self.assertEquals(resolve(url).func, get_category)

    def test_news_list_resolved(self):
        url = reverse('news_list')
        self.assertEquals(resolve(url).func.view_class, NewsListView)

    def test_news_detail_resolved(self):
        url = reverse('news_detail', kwargs={'pk': 25})
        self.assertEquals(resolve(url).func.view_class, NewsDetailView)

    def test_news_add_resolved(self):
        url = reverse('news_create')
        self.assertEquals(resolve(url).func.view_class, NewsCreateView)

    def test_news_update_resolved(self):
        url = reverse('news_update', kwargs={'pk': 25})
        self.assertEquals(resolve(url).func.view_class, NewsUpdateView)

    def test_news_update_resolved(self):
        url = reverse('news_update', kwargs={'pk': 25})
        self.assertEquals(resolve(url).func.view_class, NewsUpdateView)
