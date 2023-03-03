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

def show_category(request, category_id):
    allparts = Parts.objects.filter(category_id=category_id).filter(auto_id=1)
    cats = Category.objects.all()

    data = {
        "title": "Каталог запчастин Category",
        "description": "Переглянути каталог category",
        "content": "content",
        "allparts": allparts,
        "cats": cats,
        'cat_selected': category_id,
    }
    return render(request, "main/parts.html", context=data)

def postuser(request):
    # получаем из данных запроса POST отправленные через форму данные
    name = request.POST.get("name", "Undefined")
    age = request.POST.get("age", 1)
    lang = request.POST.get("languages", "AnyOne")
    skil = request.POST.get("skils", "Nothing")
    if len(name) == 0:
        name = "NdsvdvdAE"
    if request.method == "POST":
        return HttpResponse(f""
                        f"<div>Name: {name}  Age: {age}<div>"
                        f"<div>Languages: {lang}</div>"
                        f"<div>Skil:{skil}</div>")
    return HttpResponse("<p>пустий запрос</p>")




