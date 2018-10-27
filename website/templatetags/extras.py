from django import template
from django.utils.safestring import mark_safe

import markdown2

from website.models import *

register = template.Library()


@register.simple_tag
def all_articles():
    """
    :return: all article objects
    """
    return Article.objects.all()


@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    """
    :param markdown_text: markdown formatted string
    :return: safe html content from markdown
    """
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)
