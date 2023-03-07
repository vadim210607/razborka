from django import template
from main.models import *

register = template.Library()

@register.simple_tag
def get_all_categories():
    return Category.objects.all()

@register.simple_tag
def get_all_model():
    return Auto.objects.all()

