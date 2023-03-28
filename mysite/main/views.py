from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from django.db.models import Q
from django.views.generic import TemplateView, ListView


def index(request):
    auto = Auto.objects.all()
    category = Category.objects.all()
    data = {
        "title": "Головна сторінка",
        "auto": auto,
        "category": category,
    }
    return render(request, "main/index.html", context=data)

def about(request):
    return render(request, "main/about.html")

def item(request, item_id):
    return HttpResponse(f'Відображення статті з ID = {item_id}')

def catalog(request):
    model = request.GET.get("model_select")
    category = request.GET.get("category_select")

    model_active = "всі моделі"
    category_active = "всі категорії запчастин"
    after_parts = "Якщо Ви не знайшли потрібну деталь, залиште запит і наш працівник Вас проконсультує"
    # parts_list = Parts.objects.filter(auto_id=model).filter(category_id=category)

    parts_list = Parts.objects.all()

    if model != "all":
        parts_list = parts_list.filter(auto_id=model)
        for model_active_filter in Auto.objects.filter(id=model):
            model_active = model_active_filter.auto

    if category != "all":
        parts_list = parts_list.filter(category_id=category)
        for category_active_filter in Category.objects.filter(id=category):
            category_active = category_active_filter.category

    if len(parts_list) == 0:
        after_parts = "Тут на ланий момнт нічого не має, каталог в процесі наповнення, залиште запит і наш працівник Вас проконсультує"

    data = {
        "title": "Каталог запчастин Renault",
        "description": "Переглянути каталог всі запчатини description",
        "content": "content",
        "parts_list": parts_list,
        "model_active": model_active,
        "category_active": category_active,
        "after_parts": after_parts,
        # "cats": cats, simple tag
        # 'cat_selected': 0,
    }
    return render(request, "main/catalog.html", context=data)




def postuser(request):
    # получаем из данных запроса POST отправленные через форму данные
    name = request.POST.get("name", "Undefined")
    age = request.POST.get("age", 1)
    lang = request.POST.get("languages", "AnyOne")
    skil = request.POST.get("skils", "Nothing")
    if len(name) == 0:
        name = "NdsvdvdAE"
    if request.method == "POST":
        return HttpResponse(
                        f"<div>Name:{name}</div>"
                        f"<div>Age: {age}</div>"
                        f"<div>Languages: {lang}</div>"
                        f"<div>Skil:{skil}</div>")
    return HttpResponse("<p>пустий запрос</p>")


# def show_category(request, category_id):
#     allparts = Parts.objects.filter(category_id=category_id)
#     # cats = Category.objects.all() simple tag
#
#     data = {
#         "title": "Каталог запчастин Category",
#         "description": "Переглянути каталог category",
#         "content": "content",
#         "allparts": allparts,
#         # "cats": cats, simple tag
#         'cat_selected': category_id,
#     }
#     return render(request, "main/catalog.html", context=data)
#

# class SearchResult(ListView):
#     model = Parts
#     template_name = 'main/part.html'
#     data = {
#         "title": "Каталог запчастин Renault",
#         # "cat_selected": category_id,
#         # "category": category,
#         "catregory_id": 0,
#     }
#
#
#     def get_queryset(self, category_id):
#         category = Parts.objects.filter(category_id=category_id)
#         # data = {
#         #     "title": "Каталог запчастин Renault",
#         #     "cat_selected": category_id,
#         #     "category": category,
#         # }
#         return Parts.objects.filter(
#             Q(category_id=category_id)
#         )


