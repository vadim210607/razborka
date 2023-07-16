from django import template
from main.models import *

register = template.Library()


@register.simple_tag
def get_all_categories():
    return Category.objects.all()


@register.simple_tag
def get_all_model():
    return Model.objects.all()


@register.simple_tag
def get_auto_list():
    return Parts.objects.all()

@register.inclusion_tag('main/tags/side_filter.html')
def side_filter(selected_option_auto=0, selected_option_category=0):
    return {"selected_option_auto": selected_option_auto, "selected_option_category": selected_option_category,}

@register.inclusion_tag('main/tags/side_content.html')
def side_content(selected_option_auto=0, selected_option_category=0):
    return {"selected_option_auto": selected_option_auto, "selected_option_category": selected_option_category,}

