from django import template

register = template.Library()

@register.filter
def extension(value):
    return value.split('.')[-1]
