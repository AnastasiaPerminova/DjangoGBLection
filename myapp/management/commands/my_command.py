from random import randint, choice

from django.core.management.base import BaseCommand
from myapp.models import Author, Article, Comment


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count):
            author = Author(name=f'name{i}',
                            surname=f'surname{i}',
                            email=f'user{i}@mail.com',
                            biography=f"My Name{i}'s biography",
                            birthday=f'2000-01-{i+1}')
            author.save()

            for j in range(randint(10, 15)):
                article = Article(title=f'Title{j}',
                                  content=f'Content{j}: "Lorem ipsum dolor sit amet, consectetur adipiscing elit,'
                                          f' sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
                                          f' Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris'
                                          f' nisi ut aliquip ex ea commodo consequat. '
                                          f'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum '
                                          f'dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,'
                                          f' sunt in culpa qui officia deserunt mollit anim id est laborum."',
                                  article_author=author,
                                  category=f'{choice(["документальная","историческая","политическая"])}',
                                  published=choice([True, False]))
                article.save()


