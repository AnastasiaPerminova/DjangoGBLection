from django.db import models


# Create your models here


class Coin(models.Model):
    side = models.CharField(choices=(('орёл', 'орёл'), ('решка', 'решка')), max_length=5)
    game_time = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f'{self.pk} - {self.side}'

    def __str__(self):
        return f'{self.pk} - {self.side}'

    @staticmethod
    def count_thrown():
        coins = Coin.objects.all()
        coins_dict = {'орёл': 0, 'решка': 0}

        for item in coins:
            print(item.side)
            if item.side == 'Орёл':
                coins_dict['орёл'] += 1
            else:
                coins_dict['решка'] += 1
        return coins_dict


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateField()

    def full_name(self):
        return f'{self.surname} {self.name}'

    def __repr__(self):
        return f'{self.pk} - {self.name} - {self.surname}- {self.email}'

    def __str__(self):
        return f'{self.surname} {self.name}'


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    article_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views_count = models.IntegerField(default=0)
    published = models.BooleanField(default=False)

    def __repr__(self):
        return f'{self.pk} - {self.title} - {self.article_author.full_name()}'

    def __str__(self):
        return f'{self.article_author.full_name()} - {self.title} - {self.category}'


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(null=True)

    def __repr__(self):
        return f'{self.pk} - {self.author.full_name()} - {self.article} - {self.comment}'

    def __str__(self):
        return f'{self.author.full_name()} - {self.article} - {self.comment}'
