from django.urls import path
from .views import *

app_name = "website"
urlpatterns = [
    path('', home, name="home"),
    path('article=<int:pk>&page=<int:previous_page>', article_detail, name="article_detail"),
    path('category=<int:pk>/', list_articles, name="list_articles"),
    path('subcategory=<int:pk>/', list_sub_articles, name="list_sub_articles"),
    path('fields=<str:fields>/', list_searched_articles, name="list_searched_articles"),
]