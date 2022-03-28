from django.test import TestCase
from django.urls import reverse, resolve

from .views import *


global category
category = Category.objects.all()[0].id


class TestUrls(TestCase):

    def test_category_resolved(self):
        url = reverse('category', kwargs={'category_id': category})
        self.assertEquals(resolve(url).func, get_category)

    def test_news_list_resolved(self):
        url = reverse('news_list')
        self.assertEquals(resolve(url).func.view_class, NewsListView)

    def test_news_add_resolved(self):
        url = reverse('news_create')
        self.assertEquals(resolve(url).func.view_class, NewsCreateView)
