from django.apps import AppConfig
from django.db.models.signals import post_save, pre_delete


class GalleryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gallery'

    def ready(self):
        from .signals import note_deleting, profile_create, profile_save
