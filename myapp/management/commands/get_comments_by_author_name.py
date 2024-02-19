from django.core.management.base import BaseCommand
from myapp.models import Author, Comment


class Command(BaseCommand):
    help = "Get all comments by author name"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Author name')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        author = Author.objects.filter(name=name).first()
        if author is not None:
            comments = Comment.objects.filter(author=author)
            intro = f'All comments of {author.name}\n'
            text = ''
            for comment in comments:
                intro_2 = f'{comment.article.title}'
                comment = comment.comment
                text += f'\n{intro_2} - {comment}'

            self.stdout.write(f'{intro}{text}')
