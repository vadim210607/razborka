from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from .models import *


#           _________PARTS________

class PartsImageInline(admin.TabularInline):
    fk_name = 'parts'
    model = PartsImage

# class PartsAdmin(TranslationAdmin):
#     pass

class PartsAdmin(TranslationAdmin):
    list_display = ('id', 'parts', 'price', 'active')
    list_display_links = ('parts',)
    search_fields = ('parts', 'content')
    list_editable = ("active",)
    list_filter = ("category", "model")
    prepopulated_fields = {'slug': ('parts',)}
    inlines = [PartsImageInline, ]

#           ______CATEGORY________


class CategoryAdmin(TranslationAdmin):
    list_display = ('id', 'category', 'slug')
    list_display_links = ('category',)
    prepopulated_fields = {'slug': ('category',)}


class ModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'slug')
    list_display_links = ('model',)
    prepopulated_fields = {'slug': ('model',)}


admin.site.register(Parts, PartsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Model, ModelAdmin)
