from datetime import datetime

from django.core.management.base import BaseCommand
from myapp.models import Comment


class Command(BaseCommand):
    help = "Update comment title by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Comment ID')
        parser.add_argument('comment', type=str, help='Article title')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        comment_text = kwargs.get('comment')
        comment = Comment.objects.filter(pk=pk).first()
        comment.comment = comment_text
        comment.update_date = datetime.now()
        comment.save()
        self.stdout.write(f'{comment}')
