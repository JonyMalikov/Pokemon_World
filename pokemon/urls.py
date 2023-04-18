from django.contrib.auth import login
from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', PokemonHome.as_view(), name='home'),
    path('cats/<slug:cat>/', PokemonCategory.as_view(), name='cat'),
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive, name='archive'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    # path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('about/', about, name='about'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),
]
