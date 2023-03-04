from django import template
from gallery.forms import AddRecordForm

register = template.Library()


@register.simple_tag
def populate_record_form(position):
    return AddRecordForm(initial={'position': position})
