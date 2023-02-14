from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView

from django.urls import reverse_lazy

from django.shortcuts import render, redirect

from django.conf import settings

from .models import Car, Profile, CarInfo, CarNote, CarImage
from .forms import ProfileEditForm, ArticleCreateForm, NotesFormset


class CarView(DetailView):
    model = Car
    template_name = 'gallery/car.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['articles'] = CarInfo.objects.all().order_by('-created_at')[:4]
        return data


class CarListView(ListView):
    model = Car
    template_name = 'gallery/car_list.html'


class BrandListView(ListView):
    template_name = 'gallery/car_list.html'
    
    def get_queryset(self):
        return Car.objects.filter(brand=self.kwargs.get('brand_id'))


class ProfileView(DetailView):
    template_name = 'gallery/profile.html'
    model = User


class ProfileEdit(UpdateView):
    form_class = ProfileEditForm
    model = Profile
    template_name = 'gallery/profile_update.html'

    def get_object(self, *args, **kwargs):
        return Profile.objects.get(profile=self.request.user)

    def get_success_url(self):
        success_url = reverse_lazy('profile', args=[self.request.user.pk])
        return success_url


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'gallery/registration.html'
    success_url = reverse_lazy('car_list')


class LoginUser(LoginView):
    template_name = 'gallery/login.html'
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    next_page = reverse_lazy('car_list')


class LogoutUser(LogoutView):
    template_name = 'gallery/logout.html'


class ArticleCreateView(CreateView):
    model = CarInfo
    form_class = ArticleCreateForm
    success_url = reverse_lazy('car_list')
    template_name = 'gallery/article_create.html'

    def get_form_kwargs(self):
        data = super().get_form_kwargs()
        if self.request.method in ('POST', 'PUT'):
            car = Car.objects.get(pk=self.kwargs.get('pk'))
            is_published = True
            author = self.request.user
            qdict = data['data'].copy()
            qdict['car'] = car
            qdict['is_published'] = is_published
            qdict['author'] = author
            data['data'] = qdict
        return data
    
    def get_success_url(self):
        url = reverse_lazy('article', args=[self.object.pk])
        return url


class ArticleView(DetailView):
    model = CarInfo
    template_name = 'gallery/article.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['form'] = NotesFormset(queryset=CarNote.objects.filter(note_id=self.kwargs.get('pk')))
        return data


class ArticleEditView(UpdateView):
    template_name = 'gallery/article_edit.html'
    form_class = NotesFormset

    def get_object(self):
        pk = self.kwargs.get('pk')
        return CarInfo.objects.get(pk=pk)

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        queryset = CarNote.objects.filter(note_id=pk)
        return queryset
    
    def get_form_kwargs(self):
        data = super().get_form_kwargs()
        data.pop('instance')
        data.update({'queryset': self.get_queryset()})
        return data

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        object = CarInfo.objects.get(pk=pk)
        data['object'] = object
        return data
    
    def get_success_url(self):
        pk = self.kwargs.get('pk')
        return reverse_lazy('article_edit', args=[pk])

