from django.db.models.signals import post_save, pre_delete
from django.db.models import F

from django.dispatch import receiver

from django.conf import settings

from .models import Profile, CarNote



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def profile_create(sender, instance, created, **kwargs):
    if created:
        print('Creating profile')
        Profile.objects.create(email = instance.email, profile=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def profile_save(sender, instance, **kwargs):
    print('Saving profile', sender)
    instance.profile.save()


@receiver(pre_delete, sender=CarNote)
def note_deleting(*args, **kwargs):
    instance = kwargs.get('instance')
    CarNote.objects.filter(position__gt=instance.position, note_id=instance.note_id).update(position=F('position') - 1)
