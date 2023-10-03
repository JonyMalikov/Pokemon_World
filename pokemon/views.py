from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, FormView, ListView

from .forms import AddPostForm, ContactForm, LoginUserForm, RegisterUserForm
from .utils import *


class PokemonHome(DataMixin, ListView):
    """Главная страница"""

    model = Pokemon
    template_name = "pokemon/index.html"
    context_object_name = "posts"

    def get_context_data(self, *, object_list=None, **kwargs):
        """Получение контекста"""
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        """Запрос к базе данных"""
        return Pokemon.objects.filter(is_published=True).select_related("cat")


class PokemonCategory(DataMixin, ListView):
    """Категория"""

    model = Pokemon
    template_name = "pokemon/index.html"
    context_object_name = "posts"
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        """Получение контекста"""
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Категория - " + str(context["posts"][0].cat),
            cat_selected=context["posts"][0].cat_id,
        )

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        """Запрос к базе данных"""
        return Pokemon.objects.filter(
            cat__slug=self.kwargs["cat_slug"], is_published=True
        ).select_related("cat")


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    """Добавление статьи"""

    form_class = AddPostForm
    template_name = "pokemon/addpage.html"
    success_url = reverse_lazy("home")
    login_url = reverse_lazy("home")
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        """Получение контекста"""
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление статьи")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class ShowPost(DataMixin, DetailView):
    """Просмотр статьи"""

    model = Pokemon
    template_name = "pokemon/post.html"
    slug_url_kwarg = "post_slug"
    context_object_name = "post"

    def get_context_data(self, *, object_list=None, **kwargs):
        """Получение контекста"""
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context["post"])
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    """Регистрация"""

    form_class = RegisterUserForm
    template_name = "pokemon/register.html"
    success_url = reverse_lazy("login")

    def get_context_data(self, *, object_list=None, **kwargs):
        """Получение контекста"""
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        """Сохранение формы"""
        user = form.save()
        login(self.request, user)
        return redirect("home")


class LoginUser(DataMixin, LoginView):
    """Авторизация"""

    form_class = LoginUserForm
    template_name = "pokemon/login.html"

    def get_success_url(self):
        """Перенаправление"""
        return reverse_lazy("home")

    def get_context_data(self, *, object_list=None, **kwargs):
        """Получение контекста"""
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))


class ContactFormView(DataMixin, FormView):
    """Обратная связь"""

    form_class = ContactForm
    template_name = "pokemon/contact.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, *, object_list=None, **kwargs):
        """Получение контекста"""
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обратная связь")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        """Сохранение формы"""
        print(form.cleaned_data)
        return redirect("home")


def about(request):
    """О сайте"""
    contact_list = Pokemon.objects.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "pokemon/about.html",
        {"page_obj": page_obj, "menu": menu, "title": "О сайте"},
    )


def pageNotFound(request, exception):
    """Страница не найдена"""
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def show_category(request, cat_id):
    """Просмотр категории"""
    posts = Pokemon.objects.filter(cat_id=cat_id)
    if len(posts) == 0:
        raise Http404()

    context = {
        "posts": posts,
        "title": "Главная страница",
        "cat_selected": cat_id,
    }

    return render(request, "pokemon/index.html", context=context)


def logout_user(request):
    """Выход"""
    logout(request)
    return redirect("login")
