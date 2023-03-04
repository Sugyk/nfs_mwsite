from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib import messages

from django.urls import reverse_lazy


from django.shortcuts import get_object_or_404

from django.db.models import F

from .models import Car, Profile, CarInfo, CarNote
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


@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
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


@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class ArticleCreateView(CreateView):
    model = CarInfo
    form_class = ArticleCreateForm
    success_url = reverse_lazy('car_list')
    template_name = 'gallery/article_create.html'

    def get_form_kwargs(self):
        data = super().get_form_kwargs()
        if self.request.method in ('POST', 'PUT'):
            car = get_object_or_404(Car, pk=self.kwargs.get('pk'))
            is_published = True
            author = self.request.user
            qdict = data['data'].copy()
            qdict['car'] = car
            qdict['is_published'] = is_published
            qdict['author'] = author
            data['data'] = qdict
        return data

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['object'] = get_object_or_404(Car, pk=self.kwargs.get('pk'))
        return data
    
    def get_success_url(self):
        url = reverse_lazy('article', args=[self.object.pk])
        return url
    

class ArticleList(ListView):
    template_name = 'gallery/article_list.html'
    
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Car, pk=pk)

    def get_queryset(self):
        object = self.get_object()
        queryset = CarInfo.objects.filter(car=object).order_by('-created_at')
        return queryset

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['object'] = self.get_object()
        return data


class ArticleView(DetailView):
    model = CarInfo
    template_name = 'gallery/article.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['form'] = NotesFormset(queryset=CarNote.objects.filter(note_id=self.kwargs.get('pk')))
        return data


@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class ArticleEditView(UpdateView):
    template_name = 'gallery/article_edit.html'
    form_class = NotesFormset

    def get_object(self):
        pk = self.kwargs.get('pk')
        return CarInfo.objects.get(pk=pk)

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        queryset = CarNote.objects.filter(note_id=pk).order_by('-position')
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


class AddNoteView(ListView):
    template_name = 'gallery/article_add_record.html'

    def get_object(self):
        pk = self.kwargs.get('pk')
        object = CarInfo.objects.get(pk=pk)
        return object

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return CarNote.objects.filter(note_id=pk).order_by('position')

    def post(self, *args, **kwargs):
        position = int(self.request.POST.get('position'))
        queryset = self.get_queryset()
        if position in range(len(queryset) + 1):
            object = self.get_object()
            queryset.filter(position__gte=position).update(position=F('position') + 1)
            CarNote.objects.create(position=position, note_id=object)
            messages.success(self.request, 'Record created succesfully!')
        else:
            messages.error(self.request, 'Record creating failed.')
        return self.get(self.request)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        data['object'] = self.get_object()
        data['last_pos'] = len(self.get_queryset())
        return data

# def add(request, pk):
#     object = CarInfo.objects.get(pk=pk)
#     if request.method == 'POST':
#         position = int(request.POST.get('position'))
#         queryset = CarNote.objects.filter(note_id=pk)
#         if position in range(len(queryset) + 1):
#             CarNote.objects.filter(position__gte=position).update(position=F('position') + 1)
#             CarNote.objects.create(position=position, note_id=object)
#             messages.success(request, 'Record created succesfully!')
#         else:
#             messages.error(request, 'Document deleted.')
#     context = {'object': object}
#     queryset = CarNote.objects.filter(note_id=pk).order_by('position')
#     last_pos = len(queryset)
#     context['last_pos'] = last_pos
#     context['queryset'] = queryset
#     return render(request, 'gallery/article_add_record.html', context=context)