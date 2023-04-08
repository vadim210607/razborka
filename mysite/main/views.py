from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *

from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.shortcuts import redirect
from django.views.decorators.cache import cache_control, never_cache


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>PAGE not found</h1>')


#           НЕПОНЯТНО ЧОГО ТУДИ ПЕРЕДАЄТЬСЯ АВТО І КАТЕГОРІЯ
def index(request):
    # auto = Auto.objects.all()
    # category = Category.objects.all()
    data = {
        "title": "Головна сторінка",
        # "auto": auto,
        # "category": category,
    }
    return render(request, "main/index.html", context=data)

def about(request):
    return render(request, "main/about.html")

def item(request, item_slug):
    item_data = get_object_or_404(Parts, slug=item_slug)

    selected_option_auto = item_data.auto.all() # Походу можна через цикли і перевірку, та чи треба
    selected_option_category = item_data.category_id

    data = {
        "item_data": item_data,
        "selected_option_auto": selected_option_auto,
        "selected_option_category": int(selected_option_category),
    }
    return render(request, "main/item.html", context=data)

def catalog(request):
    data = {

    }
    return render(request, "main/catalog.html", context=data)
# ---------------------- CATALOG -------------------------- #
def cataloggggggggg(request):

    category_active = "@"
    model_active = "@"

    model_select = request.POST.get("model_select")
    category_select = request.POST.get("category_select")

    query_search = request.GET.get("query_search")

    model_select_id = request.POST.get("model_select_ID")

    parts_list = Parts.objects.all()

    method = "DIRECT"  # ?????????

    if request.method == "POST":
        if model_select != "all" and model_select:
            parts_list = parts_list.filter(auto__slug=model_select)  # Приходить SLUG
            for model_active_filter in Auto.objects.filter(slug=model_select):
                model_active = model_active_filter.auto
        if category_select != "all" and category_select:
            parts_list = parts_list.filter(category_id=category_select)
            for category_active_filter in Category.objects.filter(id=category_select):
                category_active = category_active_filter.category
        method = "POST post"

# Перехід в каталог через GET
    if request.method == "GET":
        if model_select == "all" or model_select == None:
            model_active = "всі моделі"
        if category_select == "all" or category_select == None:
            category_active = "всі категорії запчастин"
        method = "GET filter"

#   Пошук через GET запит
    if request.method == "GET" and query_search:
        parts_list = parts_list.filter(title__icontains=query_search)
        method = "GET search"

#   Текст після каталогу знизу
    after_parts = "Якщо Ви не знайшли потрібну деталь, залиште запит і наш працівник Вас проконсультує"
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
        "method": method,
        "cookie": category_active,
        "model_select": model_select,
        "category_select": category_select,
        "model_select_ID": model_select_id,
    }
    return render(request, "main/catalog.html", context=data)





# parts_list = get_object_or_404(Parts, slug=post_slug)


def show_category(request, model_slug):

# перевірка СЛАГА і визов ошибки 404
# можливо прискорить через декоратор

    list_slug_auto = []
    for exempl in Auto.objects.all():
        list_slug_auto.append(exempl.slug)
    if model_slug not in list_slug_auto:
        raise Http404

    parts_list = Parts.objects.all()
    selected_option_category = request.POST.get("category_select")
    selected_option_auto = model_slug

    method = "DIRECT"

    parts_list = parts_list.filter(auto__slug=model_slug)
    # parts_list = get_list_or_404(Parts, auto__slug=model_slug)

    if request.method == "POST":
        if selected_option_category and selected_option_category != "0":
            parts_list = parts_list.filter(category__id=selected_option_category)

        method = "POST"
        if model_slug:
            method = "POST & SLUG"

    after_parts = "Якщо Ви не знайшли потрібну деталь, залиште запит і наш працівник Вас проконсультує"
    if len(parts_list) == 0:
        after_parts = "Тут на ланий момнт нічого не має, каталог в процесі наповнення, залиште запит і наш працівник Вас проконсультує"



    data = {
        "title": "Каталог запчастин Category",
        "description": "Переглянути каталог category",
        "content": "content",
        "parts_list": parts_list,
        "method": method,   # FOR DEBUG
        "model_slug": model_slug,  # FOR DEBUG
        "selected_option_auto": selected_option_auto,
        "selected_option_category": int(selected_option_category),
        "after_parts": after_parts,

    }

    return render(request, "main/catalog.html", context=data)



def postuser(request):

    # получаем из данных запроса GET отправленные через форму данные
    name = request.POST.get("name", "Undefined")
    response = HttpResponse(f"<h3>Name:{name}</h3>")

    return response


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

# CATALOG cookie
# category_select_cookie = request.COOKIES.get('cat_select')
#
# if category_select_cookie is None:
#     pass
#     # Cookie is not set
#
# # OR
#
# try:
#     category_select_cookie = request.COOKIES['cat_select']
# except KeyError:
#     pass
# # Cookie is not set
# ЗНИЗУ
# response.set_cookie("cat_select", category_active)