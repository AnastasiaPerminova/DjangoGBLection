from random import randint, choice

from django.core.management.base import BaseCommand
from myapp.models import Author, Article, Comment


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        articles = Article.objects.all()
        authors = Author.objects.all()
        for article in articles:
            for i in range(randint(2, 7)):
                comment = Comment(
                    author=choice(authors),
                    article=article,
                    comment=f"Comment{i}:Sed ut perspiciatis unde omnis iste natus error "
                            f"sit voluptatem accusantium doloremque laudantium, totam rem aperiam,"
                            f" eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae "
                            f"dicta sunt explicabo. ")
                comment.save()
