from django import forms
from .models import Category, News


class NewsForm(forms.Form):  # Мы специально не используем ModelForm
    title = forms.CharField(max_length=128, label='Заголовок', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Содержание', required=False, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 5,
    }))
    is_published = forms.BooleanField(label='Опубликовано', initial=True)
    category = forms.ModelChoiceField(empty_label='Выбрать категорию', label='Категория',
                                      queryset=Category.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control'}))
