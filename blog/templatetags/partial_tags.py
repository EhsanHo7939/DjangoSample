from django import template
from ..models import Category

register = template.Library()

@register.inclusion_tag("blog/partials/categories.html")
def cat_tags():
    return {
        "categories": Category.objects.filter(status=True)
    }


@register.inclusion_tag("registration/partials/active_link.html")
def active_link(request, link_name, content, classes):
    return {
        "request": request,
        "link_name": link_name,
        "link": "account:{0}".format(link_name),
        "classes": classes,
        "content": content,
    }
