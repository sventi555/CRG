from django.urls import path
from .views import *

app_name = "website"
urlpatterns = [
    path('', home, name="home"),
    path('category=<str:category_name>/', list_articles, name="list_articles"),
    path('subcategory=<str:subcategory_name>/', list_sub_articles, name="list_sub_articles"),
    path('fields=<str:fields>/', list_searched_articles, name="list_searched_articles"),
]