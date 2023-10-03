from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class AddPostForm(forms.ModelForm):
    """Форма добавления статьи"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["cat"].empty_label = "Категория не выбрана"

    def clean_title(self):
        """Проверка длины заголовка"""
        title = self.cleaned_data["title"]
        if len(title) > 200:
            raise ValidationError("Длина превышает 200 символов")

        return title

    class Meta:
        model = Pokemon
        fields = ["title", "slug", "content", "photo", "is_published", "cat"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-input"}),
            "content": forms.Textarea(attrs={"cols": 60, "rows": 10}),
        }


class RegisterUserForm(UserCreationForm):
    """Форма регистрации"""

    username = forms.CharField(
        label="Логин", widget=forms.TextInput(attrs={"class": "form-input"})
    )
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "form-input"}),
    )
    password2 = forms.CharField(
        label="Повтор пароля",
        widget=forms.PasswordInput(attrs={"class": "form-input"}),
    )
    email = forms.EmailField(
        label="Email", widget=forms.EmailInput(attrs={"class": "form-input"})
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class LoginUserForm(AuthenticationForm):
    """Форма авторизации"""

    username = forms.CharField(
        label="Логин", widget=forms.TextInput(attrs={"class": "form-input"})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "form-input"}),
    )


class ContactForm(forms.Form):
    """Форма обратной связи"""

    name = forms.CharField(label="Имя", max_length=255)
    email = forms.EmailField(label="Email")
    content = forms.CharField(
        widget=forms.Textarea(attrs={"cols": 60, "rows": 10})
    )
    captcha = CaptchaField()
