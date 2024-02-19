from django.core.management.base import BaseCommand
from myapp.models import Article


class Command(BaseCommand):
    help = "Get Article by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Article ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        article = Article.objects.filter(pk=pk).first()
        self.stdout.write(f'{article}')
