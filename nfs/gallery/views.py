from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Car


class CarListView(ListView):
    model = Car
    template_name = 'gallery/car_list.html'
