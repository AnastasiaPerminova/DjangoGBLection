from django.core.management.base import BaseCommand
from myapp.models import Article, Comment


class Command(BaseCommand):
    help = "Get all comments by article title"

    def add_arguments(self, parser):
        parser.add_argument('title', type=str, help='Article title')

    def handle(self, *args, **kwargs):
        title = kwargs.get('title')
        article = Article.objects.filter(title=title).first()
        if article is not None:
            comments = Comment.objects.filter(article=article)
            intro = f'All comments of {article.title}\n'
            text = '\n'.join(comment.comment for comment in comments)
            self.stdout.write(f'{intro}{text}')