from django.core.management.base import BaseCommand
from myapp.models import Article


class Command(BaseCommand):
    help = "Update article title by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Article ID')
        parser.add_argument('title', type=str, help='Article title')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        title = kwargs.get('title')
        article = Article.objects.filter(pk=pk).first()
        article.title = title
        article.save()
        self.stdout.write(f'{article}')
