from django import template
import volleyball.views as views

register = template.Library()


@register.simple_tag()
def get_categories():
    return views.cats_db


@register.inclusion_tag('volleyball/list_categories.html')
def show_categories(cat_selected=0):
    cats = views.cats_db
    return {"cats": cats, "cat_selected": cat_selected}
