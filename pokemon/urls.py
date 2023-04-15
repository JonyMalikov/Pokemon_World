from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('cats/<slug:cat>/', categories, name='cat'),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive, name='archive'),
    path('about/', about, name='about'),
    path('category/<int:cat_id>/', show_category, name='category'),
]
