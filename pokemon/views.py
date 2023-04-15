from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render

from .models import *


def index(request):
    posts = Pokemon.objects.all()
    return render(request, 'pokemon/index.html', {'posts': posts,
                                                  'cat_selected': 0,
                                                  'title': 'Главная страница'})


def categories(request, cat):
    if (request.POST):
        print(request.POST)
    return HttpResponse(f"<h1>Статьи по категориям</h1>{cat}</p>")


def show_category(request, cat_id):
    posts = Pokemon.objects.filter(cat_id=cat_id)
    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'title': 'Главная страница',
        'cat_selected': cat_id,
    }

    return render(request, 'pokemon/index.html', context=context)


def about(request):
    return render(request, 'pokemon/about.html', {'title': 'О сайте'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def archive(request, year):
    if (int(year) > 2020):
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1>Архив по годам</h1>{year}</p>")
