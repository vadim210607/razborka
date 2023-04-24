from modeltranslation.translator import translator, TranslationOptions
from main.models import *


class PartsTranslationOptions(TranslationOptions):
    fields = ('title',)


class CategoryTranslationOptions(TranslationOptions):
    fields = ('category',)


class AutoTranslationOptions(TranslationOptions):
    fields = ('auto',)


translator.register(Parts, PartsTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Auto, AutoTranslationOptions)
