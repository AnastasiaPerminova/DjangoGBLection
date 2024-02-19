import datetime

from django import forms
from .models import Author, Article


class GameForm(forms.Form):
    game = forms.ChoiceField(choices=[('c', 'coin'), ('d', 'dice'), ('n', 'numbers')])
    attempts = forms.IntegerField(min_value=1, max_value=64)


class AuthorForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':
                                                                             'form-control',
                                                                         'placeholder': 'Введите имя автора'}))
    surname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':
                                                                                'form-control',
                                                                            'placeholder': 'Введите фамилию автора'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':
                                                                'form-control',
                                                            'placeholder': 'user@mail.ru'}))
    biography = forms.CharField(max_length=1000, widget=forms.Textarea)

    birthday = forms.DateField(initial=datetime.date.today,
                               widget=forms.DateInput(attrs={'class': 'form-control', 'type':
                                   'date'}))


# class AuthorForm(forms.ModelForm):
#     class Meta:
#         model = Author
#         fields = ['name', 'surname', 'email', 'biography', 'birthday']

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':
                                                                                             'form-control',
                                                                                         'placeholder': 'Введите название статьи.'}))
    content = forms.CharField(max_length=1000, widget=forms.Textarea)
    article_author = forms.ModelChoiceField(queryset=Author.objects.all())
    category = forms.CharField(max_length=100)


class CommentForm(forms.Form):
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    comment = forms.CharField(max_length=1000,widget=forms.Textarea)
