from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *

ARTICLES_PER_PAGE = 10


def home(request):
    latest = []
    for category in Category.objects.all():
        article = Article.objects.filter(subcategory__category=category).exclude(featured=False)[0:1]
        if article:
            latest.append(article[0])

    status_updates = StatusUpdate.objects.all()[0:10]
    submission_request = SubmissionRequest.objects.all()[0]
    return render(request, 'website/home.html', {
        'articles': latest,
        'status_updates': status_updates,
        'submission_request': submission_request,
    })


def list_articles(request, pk):
    category = Category.objects.get(pk=pk)
    article_list = Article.objects.filter(subcategory__category=category)
    feature_article = Article.objects.filter(subcategory__category=category).exclude(featured=False)
    if feature_article:
        feature_article = feature_article[0]
    else:
        feature_article = None

    paginator = Paginator(article_list, ARTICLES_PER_PAGE)

    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'website/list_articles.html', {
        'articles': articles,
        'feature_article': feature_article,
        'category': category,
    })


def list_sub_articles(request, pk):
    subcategory = Subcategory.objects.get(pk=pk)
    category = subcategory.category

    article_list = Article.objects.filter(subcategory=subcategory)
    feature_article = Article.objects.filter(subcategory__category=category).exclude(featured=False)
    if feature_article:
        feature_article = feature_article[0]
    else:
        feature_article = None

    paginator = Paginator(article_list, ARTICLES_PER_PAGE)

    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'website/list_articles.html', {
        'articles': articles,
        'category': category,
        'subcategory': subcategory,
        'feature_article': feature_article,
    })


def list_searched_articles(request, fields):
    article_list = (Article.objects.filter(title__contains=fields) |
                    Article.objects.filter(content__contains=fields) |
                    Article.objects.filter(author__name__contains=fields))

    paginator = Paginator(article_list, ARTICLES_PER_PAGE)

    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'website/list_articles.html', {
        'articles': articles,
        'fields': fields,
    })


def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'website/article_detail.html', {
        'article': article,
    })


def introductions(request):
    return render(request, 'website/introductions.html')


def our_team(request):
    return render(request, 'website/our_team.html')


def to_publish(request):
    return render(request, 'website/to_publish.html')
