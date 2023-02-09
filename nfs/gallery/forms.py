from django import forms

from .models import Profile, CarInfo

from django.contrib.auth.models import User


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('profile', )


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = CarInfo
        fields = ('title', 'car', 'author')
