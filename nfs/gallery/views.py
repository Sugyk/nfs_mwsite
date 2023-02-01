from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.conf import settings
from .models import Car


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
