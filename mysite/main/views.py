from django.shortcuts import render
from django.http import HttpResponse

from .models import *


def index(request):
    return render(request, "main/index.html", {"title": "Головна сторінка",})

def about(request):
    return render(request, "main/about.html")

def item(request, item_id):
    return HttpResponse(f'Відображення статті з ID = {item_id}')

def parts(request):
    allparts = Parts.objects.all()
    cats = Category.objects.all()
    data = {
        "title": "Каталог запчастин Renault",
        "description": "Переглянути каталог всі запчатини description",
        "content": "content",
        "allparts": allparts,
        "cats": cats,
        'cat_selected': 0,
    }
    return render(request, "main/parts.html", context=data)

def show_category(request, cat_id):
    allparts = Parts.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    data = {
        "title": "Каталог запчастин Category",
        "description": "Переглянути каталог category",
        "content": "content",
        "allparts": allparts,
        "cats": cats,
        'cat_selected': cat_id,
    }
    return render(request, "main/parts.html", context=data)

