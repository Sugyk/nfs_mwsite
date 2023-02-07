from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView

from django.urls import reverse_lazy

from django.shortcuts import render

from django.conf import settings

from .models import Car, Profile
from .forms import ProfileEditForm


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
        print(success_url)
        return success_url


# def ProfileEdit(request):
#     if request.method == 'GET':
#         print(ProfileEditForm(instance=request.user))
#         return render(request, 'gallery/profile_update.html', context={'form': ProfileEditForm(instance=request.user)})


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
