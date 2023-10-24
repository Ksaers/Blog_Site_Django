from django.shortcuts import render, redirect
import requests
from .models import Article


def create_article(request):
    if request.method == 'POST':
        # Получите данные из формы
        title = request.POST.get('articleTitle', '')
        content = request.POST.get('articleContent', '')

        # Создайте новую статью и сохраните её
        article = Article(title=title, content=content)
        article.save()

        # После успешного сохранения, перенаправление на главную страницу
        return redirect('exchange')

    # Остальной код представления для GET-запроса
    context = {
        # Контекст для отображения главной страницы
    }
    return render(request, 'exchange_app/index.html', context)


def article_list(request):
    articles = Article.objects.all()[:1]  # Получаем первые две статьи
    context = {'articles': articles}
    return render(request, 'exchange_app/article_list.html', context)


def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return redirect('article_list')


def exchange(request):
    response = requests.get(url='https://api.exchangerate-api.com/v4/latest/USD').json()
    currencies = response.get('rates')

    if request.method == 'GET':
        context = {
            'currencies': currencies
        }
        return render(request=request, template_name='exchange_app/index.html', context=context)

    if request.method == 'POST':
        # Получите данные из формы
        title = request.POST.get('articleTitle', '')  # Здесь 'articleTitle' - имя поля для заголовка
        content = request.POST.get('articleContent', '')  # Здесь 'articleContent' - имя поля для содержания

        # Создайте новую статью и сохраните её
        article = Article(title=title, content=content)
        article.save()

        # После успешного сохранения, перенаправление на главную страницу
        return redirect('article_list')
