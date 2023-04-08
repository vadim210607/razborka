from django.urls import path

from .views import *

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name='home'),
    path('about', about, name='about'),
    path('renault-parts/', catalog, name="all_catalog"),
    path('renault-parts/<slug:model_slug>/', show_category, name="model_catalog"),
    # path('renault-parts/', SearchResult.as_view(), name="catalog"),
    path('renault-parts/item/<slug:item_slug>/', item, name="item"),

    path('postuser/', postuser),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# if settings.DEBUG:
#     urlpatterns += [
#         re_path(r'^media/(?P<path>.*)$', serve, {
#             'document_root': settings.MEDIA_ROOT,
#         }),
#     ]
