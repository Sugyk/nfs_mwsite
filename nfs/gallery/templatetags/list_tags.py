from gallery.models import Brand
from django import template

register = template.Library()


@register.simple_tag
def get_brands():
    return Brand.objects.filter(car__gt=0)

