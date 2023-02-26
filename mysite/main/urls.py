from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('about', about, name='about'),
    path('renault-parts/', parts, name="catalog"),
    path('renault-parts/q/<int:item_id>/', item, name="item"),
    path('renault-parts/<int:cat_id>/', show_category, name="category"),
]
