from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from kino.models import Film, Cinema, News

from .forms import FilmForm, CinemaForm, NewsForm, SignInForm, SignUpForm #UserForm

from django.contrib.auth.models import User
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


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

class AdminStatisticsView(TemplateView):
    template_name = 'admin_panel/statistics.html'

class AdminBannersSlidersView(TemplateView):
    template_name = 'admin_panel/banners_sliders.html'


# NEWS views
class AdminNewsView(ListView):
    model = News
    template_name = 'admin_panel/news/news.html'

class AdminNewsDetailView(DetailView):
    model = News
    template_name = 'admin_panel/news/news_detail.html'

class AdminNewsAddView(CreateView):
    model = News
    form_class = NewsForm
    template_name = 'admin_panel/news/news_add.html'

class AdminNewsUpdateView(UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'admin_panel/news/news_update.html'

class AdminNewsDeleteView(DeleteView):
    model = News
    template_name = 'admin_panel/news/news_delete.html'
    success_url = reverse_lazy('admin_news')
# NEWS-----


class AdminSharesView(TemplateView):
    template_name = 'admin_panel/shares.html'

class AdminPagesView(TemplateView):
    template_name = 'admin_panel/pages.html'

class AdminUsersView(TemplateView):
    template_name = 'admin_panel/users.html'

class AdminMailingView(TemplateView):
    template_name = 'admin_panel/mailing.html'



#FILM views
class AdminFilmsView(ListView):
    model = Film
    template_name = 'admin_panel/film/films.html'
    ordering = ['-id']

class AdminFilmDetailView(DetailView):
    model = Film
    template_name = 'admin_panel/film/film_detail.html'

class AdminFilmAddView(CreateView):
    model = Film
    form_class = FilmForm
    template_name = 'admin_panel/film/film_add.html'

class AdminFilmUpdateView(UpdateView):
    model = Film
    form_class = FilmForm
    template_name = 'admin_panel/film/film_update.html'

class AdminFilmDeleteView(DeleteView):
    model = Film
    template_name = 'admin_panel/film/film_delete.html'
    success_url = reverse_lazy('admin_films')
#-----

#CINEMA views
class AdminCinemasView(ListView):
    model = Cinema
    template_name = 'admin_panel/cinema/cinemas.html'

class AdminCinemaDetailView(DetailView):
    model = Cinema
    template_name = 'admin_panel/cinema/cinema_detail.html'

class AdminCinemaAddView(CreateView):
    model = Cinema
    form_class = CinemaForm
    template_name = 'admin_panel/cinema/cinema_add.html'

class AdminCinemaUpdateView(UpdateView):
    model = Cinema
    form_class = CinemaForm
    template_name = 'admin_panel/cinema/cinema_update.html'

class AdminCinemaDeleteView(DeleteView):
    model = Cinema
    template_name = 'admin_panel/cinema/cinema_delete.html'
    success_url = reverse_lazy('admin_cinemas')
#-----




def dashboard_view(request):
    return render(request, 'admin_panel/dashboard.html')
