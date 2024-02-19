from django.core.management.base import BaseCommand
from myapp.models import Author, Article


class Command(BaseCommand):
    help = "Get all posts by author name"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Author name')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        author = Author.objects.filter(name=name).first()
        if author is not None:
            articles = Article.objects.filter(article_author=author)
            intro = f'All articles of {author.name}\n'
            text = '\n'.join(article.title for article in articles)
            self.stdout.write(f'{intro}{text}')
