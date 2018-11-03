from django import template
from django.utils.safestring import mark_safe

import markdown2

from website.models import Category


register = template.Library()


@register.inclusion_tag('website/menu_bar.html')
def menu_bar():
    """
    :return: a queryset of all categories
    """
    return {'categories': Category.objects.all()}


@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    """
    :param markdown_text: markdown formatted string
    :return: safe html content from markdown
    """
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)


@register.filter('category_parse')
def category_parse(subcategory):
    """
    :param category: a subcategory name
    :return: the name with the parent category parsed out
    """
    return subcategory[subcategory.find('-') + 1:]
