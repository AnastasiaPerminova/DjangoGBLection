from random import randint, choice

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import logging

from .form import GameForm, AuthorForm, ArticleForm, CommentForm
from .models import Coin, Author, Article, Comment

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def index(request):
    return render(request, "myapp/index.html")


def about(request):
    return render(request, "myapp/about.html")


# Create your views here.


def game_1(request, number):
    for _ in range(number):
        answer = choice(['Орёл', 'Решка'])
        coin = Coin(side=answer)
        coin.save()
        context = {'number': number,
                   'name': 'Орёл/решка',
                   'result': answer}
        logger.info(f"Answer: {answer}")
    return render(request, "myapp/game.html", context)


def static_game(request):
    result = Coin.count_thrown()
    return HttpResponse(f'Орёл: {result["орёл"]}. Решка: {result["решка"]} ')


def game_2(request):
    answer = randint(1, 6)
    context = {'name': 'Игральный кубик',
               'result': answer}
    logger.info(f"Answer: {answer}")
    return render(request, "myapp/game.html", context)


def game_3(request):
    answer = randint(0, 100)
    context = {'name': 'Случайное число до 100',
               'result': answer}
    logger.info(f"Answer: {answer}")
    return render(request, "myapp/game.html", context)


def show_posts(request, author_id):
    author = Author.objects.filter(pk=author_id).first()
    if author is not None:
        articles = Article.objects.filter(article_author=author)
        context = {"author": author.full_name(),
                   "articles": articles}

        return render(request, "myapp/articles_by_author.html", context)


def article_full(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    author = None
    if article is not None:
        author = article.article_author.full_name()
    article.views_count += 1
    article.save()
    comments = Comment.objects.filter(article=article)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            comment = form.cleaned_data['comment']
            new_comment = Comment(author=author, article=article, comment=comment)
            new_comment.save()

    return render(request, 'myapp/article_full.html',
                  {'form': form, 'article': article, 'author': author, 'comments': comments})


def full_name(request):
    authors = Author.objects.all()
    result = ''
    for author in authors:
        result += f'{author.full_name()}<br>'
    return HttpResponse(result)


def choice_games(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.cleaned_data['game']
            attempts = form.cleaned_data['attempts']

            if game == 'c':
                return game_1(request, attempts)
            elif game == 'd':
                return game_2(request)
            elif game == 'n':
                return game_3(request)

    else:
        form = GameForm()
    return render(request, 'myapp/choice_games.html', {'form': form})


def author_form(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            email = form.cleaned_data['email']
            biography = form.cleaned_data['biography']
            birthday = form.cleaned_data['birthday']
            author = Author(name=name, surname=surname, email=email, biography=biography, birthday=birthday)
            author.save()
            message = 'Автор сохранён'
    else:
        form = AuthorForm()
        message = 'Заполните форму'
    return render(request, 'myapp/author_form.html', {'form': form, 'message': message})


def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            article_author = form.cleaned_data['article_author']
            category = form.cleaned_data['category']
            article = Article(title=title, content=content, article_author=article_author, category=category)
            article.save()
            message = 'Cтатья сохранена'
    else:
        form = ArticleForm()
        message = 'Заполните форму'
    return render(request, 'myapp/add_article.html', {'form': form, 'message': message})
