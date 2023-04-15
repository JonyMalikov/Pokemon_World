from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Pokemon_World import settings
from pokemon.views import *
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pokemon.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound
