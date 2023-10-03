from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from pokemon.views import *
from Pokemon_World import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("captcha/", include("captcha.urls")),
    path("", include("pokemon.urls")),
]

if settings.DEBUG:
    """Для отладки"""
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

handler404 = pageNotFound
