from django import template
from gallery.models import CarNote, CarImage

register = template.Library()


@register.simple_tag
def get_notes_and_images(article_pk):
    notes = CarNote.objects.filter(note_id=article_pk)
    images = CarImage.objects.filter(note_id=article_pk)
    object_list = list(notes) + list(images)
    sorted_list = sorted(object_list, key=lambda x: x.position)
    return sorted_list
