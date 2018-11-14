from django.urls import path
from .views import *

app_name = "website"
urlpatterns = [
    path('', home, name="home"),
    path('article=<int:pk>', article_detail, name="article_detail"),
    path('category=<int:pk>/', list_articles, name="list_articles"),
    path('subcategory=<int:pk>/', list_sub_articles, name="list_sub_articles"),
    path('fields=<str:fields>/', list_searched_articles, name="list_searched_articles"),
    path('introductions', introductions, name="introductions"),
    path('our_team', our_team, name="our_team"),
    path('to_publish', to_publish, name="to_publish"),
]