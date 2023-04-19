# from django import template
# from pokemon.models import *
#
# register = template.Library()
#
# menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]
#
#
# @register.simple_tag(name='getcats')
# def get_categories(filter=None):
#     if not filter:
#         return Category.objects.all()
#     else:
#         return Category.objects.filter(pk=filter)
#
#
# @register.inclusion_tag('pokemon/list_categories.html')
# def show_categories(sort=None, cat_selected=0):
#     if not sort:
#         cats = Category.objects.all()
#     else:
#         cats = Category.objects.order_by(sort)
#
#     return {"cats": cats, "cat_selected": cat_selected}
#
#
# @register.inclusion_tag('pokemon/menu.html')
# def show_menu():
#     return {'menu': menu}
