from django.core.management.base import BaseCommand
from myapp.models import Article


class Command(BaseCommand):
    help = "Get all users."

    def handle(self, *args, **kwargs):
        articles = Article.objects.all()
        self.stdout.write(f'{articles}')
