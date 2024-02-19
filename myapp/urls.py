from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('game_1/<int:number>', views.game_1, name='game_1'),
    path('game_2/', views.game_2, name='game_2'),
    path('game_3/', views.game_3, name='game_3'),
    path('static_game/', views.static_game, name='st_g'),
    path('full_name/', views.full_name, name='st_g'),
    path('show_posts/<int:author_id>', views.show_posts, name='show_posts'),
    path('article/<int:article_id>/', views.article_full, name='article_full'),
    path('choice_games/', views.choice_games, name='choice_games'),
    path('author_form/', views.author_form, name='author_form'),
    path('add_article/', views.add_article, name='add_article')
]
