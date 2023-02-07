from django.forms import inlineformset_factory
from .models import Profile
from django.conf import settings
from django import forms
from django.contrib.auth.models import User


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('profile', )