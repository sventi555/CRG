from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *


def home(request):
    latest = []
    for category in Category.objects.all():
        article = Article.objects.filter(subcategory__category=category)[0:1]
        if article:
            latest.append(article[0])

    status_updates = StatusUpdate.objects.all()[0:50]
    return render(request, 'website/home.html', {
        'articles': latest,
        'status_updates': status_updates,
    })


def list_articles(request, pk):
    category = Category.objects.get(pk=pk)
    article_list = Article.objects.filter(subcategory__category=category)

    paginator = Paginator(article_list, 20)

    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'website/list_articles.html', {
        'articles': articles,
        'category': category,
    })


def list_sub_articles(request, pk):
    article_list = Article.objects.filter(subcategory__pk=pk)

    paginator = Paginator(article_list, 20)

    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'website/list_articles.html', {
        'articles': articles,
    })


def list_searched_articles(request, fields):
    article_list = (Article.objects.filter(title__contains=fields) |
                    Article.objects.filter(content__contains=fields) |
                    Article.objects.filter(author__name__contains=fields))

    paginator = Paginator(article_list, 20)

    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'website/list_articles.html', {
        'articles': articles,
    })


def article_detail(request, pk, previous_page=1):
    article = Article.objects.get(pk=pk)
    return render(request, 'website/article_detail.html', {
        'article': article,
        'previous_page': previous_page,
    })
