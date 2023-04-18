from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView

from .forms import AddPostForm
from .models import *


class PokemonHome(ListView):
    model = Pokemon
    template_name = 'pokemon/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Pokemon.objects.filter(is_published=True)


class PokemonCategory(ListView):
    model = Pokemon
    template_name = 'Pokemon/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context

    def get_queryset(self):
        return Pokemon.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


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


class ShowPost(DetailView):
    model = Pokemon
    template_name = 'pokemon/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        return context


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'pokemon/addpage.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        return context


def about(request):
    return render(request, 'pokemon/about.html', {'title': 'О сайте'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
