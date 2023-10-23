from django.urls import path
from .views import exchange, create_article, article_list
from . import views

urlpatterns = [
    path('', exchange, name='exchange'),
    path('articles/', views.article_list, name='article_list'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),  # Создайте этот URL-шаблон
    path('create/', create_article, name='create_article'),  # Страница создания статьи
]