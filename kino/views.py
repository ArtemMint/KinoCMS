from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from kino.models import Film, FilmGallery, Cinema, CinemaGallery

from .forms import FilmForm, CinemaForm, SignInForm, SignUpForm #UserForm

from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class HomeView(ListView):
    model = Film
    template_name = 'kino/home.html'

# def home_view(request):
#     films = Film.objects.all()
#     return render(
#         request, 
#         'kino/home.html',
#         {'films':films})

def sign_up_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/home/')
    else:
        form = SignUpForm()
    return render(request, 'register/sign_up.html', {'form': form})


def sign_in_view(request):
    error = ''
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=str(username), password=str(password))
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/home/')
                else:
                    error = "The password is valid, but the account has been disabled!"
            else:
                error = "The username and password were incorrect."
    else:
        form = SignInForm()
    return render(request, 
                'register/sign_in.html',
                {'form': form,
                'error': error})


def logout_view(request):
    logout(request)
    return render(request, 
                'register/logout.html')


# ADMIN VIEWS
def admin_view(request):
    return render(request, 'admin_panel/admin.html')

#Film views
class AdminFilmsView(ListView):
    model = Film
    template_name = 'admin_panel/films.html'
    ordering = ['-id']

class AdminFilmDetailView(DetailView):
    model = Film
    template_name = 'admin_panel/film_detail.html'

    def get_context_data(self, **kwargs):
        context = super(AdminFilmDetailView, self).get_context_data(**kwargs)
        context['gallery_list'] = FilmGallery.objects.filter()
        # And so on for more models
        return context

class AdminFilmAddView(CreateView):
    model = Film
    form_class = FilmForm
    template_name = 'admin_panel/film_add.html'

class AdminFilmUpdateView(UpdateView):
    model = Film
    form_class = FilmForm
    template_name = 'admin_panel/film_update.html'

class AdminFilmDeleteView(DeleteView):
    model = Film
    template_name = 'admin_panel/film_delete.html'
    success_url = reverse_lazy('admin_films')
#-----

#Cinema views
class AdminCinemasView(ListView):
    model = Cinema
    template_name = 'admin_panel/cinemas.html'

class AdminCinemaDetailView(DetailView):
    model = Cinema
    template_name = 'admin_panel/cinema_detail.html'

    def get_context_data(self, **kwargs):
        context = super(AdminCinemaDetailView, self).get_context_data(**kwargs)
        context['gallery_list'] = CinemaGallery.objects.filter()
        # And so on for more models
        return context

class AdminCinemaAddView(CreateView):
    model = Cinema
    form_class = CinemaForm
    template_name = 'admin_panel/cinema_add.html'

class AdminCinemaUpdateView(UpdateView):
    model = Cinema
    form_class = CinemaForm
    template_name = 'admin_panel/cinema_update.html'

class AdminCinemaDeleteView(DeleteView):
    model = Cinema
    template_name = 'admin_panel/cinema_delete.html'
    success_url = reverse_lazy('admin_cinemas')

#-----


def dashboard_view(request):
    return render(request, 'admin_panel/dashboard.html')
