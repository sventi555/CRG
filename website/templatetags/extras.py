from django import template
from django.utils.safestring import mark_safe

import markdown2


register = template.Library()


@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    """
    :param markdown_text: markdown formatted string
    :return: safe html content from markdown
    """
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)
