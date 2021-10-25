from django import template
from ..models import Category

register = template.Library()

@register.inclusion_tag("blog/partials/categories.html")
def cat_tags():
    return {
        "categories": Category.objects.filter(status=True)
    }
