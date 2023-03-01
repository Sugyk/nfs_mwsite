from django import forms

from .models import Profile, CarInfo, CarNote

from django.contrib.auth.models import User


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('profile', )


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = CarInfo
        fields = ('title', 'car', 'author')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

class NotesForm(forms.ModelForm):
    class Meta:
        model = CarNote
        exclude = ('id',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'note_id': forms.HiddenInput(attrs={'required': False}),
            'position': forms.HiddenInput(attrs={'required': False})
        }

NotesFormset = forms.modelformset_factory(extra=0, model=CarNote, form=NotesForm, can_delete=True)
