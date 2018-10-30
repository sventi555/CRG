from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *


def home(request):
    latest = []
    for category in Category.objects.all():
        article = Article.objects.filter(subcategory__category=category)[0:1]
        latest.append(article)

    status_updates = StatusUpdate.objects.all()[0:50]
    return render(request, 'website/home.html', {
        'articles': latest,
        'status_updates': status_updates,
    })


def list_articles(request, category_name):
    article_list = Article.objects.filter(category__name=category_name)

    paginator = Paginator(article_list, 20)

    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'website/list_articles.html', {
        'articles': articles,
    })


def list_sub_articles(request, subcategory_name):
    article_list = Article.objects.filter(subcategory__name=subcategory_name)

    paginator = Paginator(article_list, 20)

    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'website/list_articles.html', {
        'articles': articles,
    })


def list_searched_articles(request, fields):
    article_list = (Article.objects.filter(title__contains=fields) |
                    Article.objects.filter(content__contains=fields) |
                    Article.objects.filter(author__contains=fields))

    paginator = Paginator(article_list, 20)

    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'website/list_articles.html', {
        'articles': articles,
    })


def article_detail(request, article_id, previous_page=1):
    article = Article.objects.get(pk=article_id)
    return render(request, 'website/article_detail.html', {
        'article': article,
        'previous_page': previous_page,
    })
