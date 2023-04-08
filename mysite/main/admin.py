from django.contrib import admin

from .models import *

class PartsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo', 'price', 'active')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ("active",)
    list_filter = ("category", "auto")
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'slug')
    list_display_links = ('id', 'category')
    prepopulated_fields = {'slug': ('category',)}

class AutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'auto', 'slug')
    list_display_links = ('id', 'auto')
    prepopulated_fields = {'slug': ('auto',)}

admin.site.register(Parts, PartsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Auto, AutoAdmin)
