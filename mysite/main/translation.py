from modeltranslation.translator import translator, TranslationOptions
from main.models import *


class PartsTranslationOptions(TranslationOptions):
    fields = ('parts',)


class CategoryTranslationOptions(TranslationOptions):
    fields = ('category',)


# class ModelTranslationOptions(TranslationOptions):
#     fields = ('model',)


translator.register(Parts, PartsTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
# translator.register(Model, ModelTranslationOptions)
