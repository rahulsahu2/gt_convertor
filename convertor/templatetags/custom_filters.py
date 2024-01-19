# custom_filters.py
from django import template

register = template.Library()

@register.filter(name='replace_str')
def replace_str(value, old_str, new_str):
    return value.replace(old_str, new_str)
