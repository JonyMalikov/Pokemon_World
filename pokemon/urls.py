from django.contrib.auth import login
from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('cats/<slug:cat>/', categories, name='cat'),
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive, name='archive'),
    path('addpage/', addpage, name='add_page'),
    # path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('about/', about, name='about'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),
]
