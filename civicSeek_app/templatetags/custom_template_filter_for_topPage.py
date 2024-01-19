from django import template

register = template.Library()


@register.filter
def tag_limit(value, limit):
    return value[:limit]
