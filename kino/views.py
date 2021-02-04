from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from django.contrib.auth.forms import UserChangeForm

from kino.models import Film, Cinema, News, Shares
from register.models import Client

from kino.forms import FilmForm, CinemaForm, NewsForm, SharesForm
from register.forms import EditProfileForm

from django.contrib.auth.models import User
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


class HomeView(ListView):
    model = Film
    template_name = 'kino/home.html'

class PosterView(ListView):
    model = Film
    template_name = 'kino/poster.html'

class FilmDetailView(DetailView):
    model = Film
    template_name = 'kino/film_detail.html'

class PremiereView(ListView):
    model = Film
    template_name = 'kino/premiere.html'

class CinemasView(ListView):
    model = Cinema
    template_name = 'kino/cinemas.html'

class CinemaDetailView(DetailView):
    model = Cinema
    template_name = 'kino/cinema_detail.html'

class SharesView(ListView):
    model = Shares
    template_name = 'kino/shares.html'

class NewsView(ListView):
    model = News
    template_name = 'kino/news.html'

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
    ordering = ['-id']

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

# Shares views
class AdminSharesView(ListView):
    model = Shares
    template_name = 'admin_panel/shares/shares.html'
    ordering = ['-id']

class AdminSharesDetailView(DetailView):
    model = Shares
    template_name = 'admin_panel/shares/shares_detail.html'

class AdminSharesAddView(CreateView):
    model = Shares
    form_class = SharesForm
    template_name = 'admin_panel/shares/shares_add.html'

class AdminSharesUpdateView(UpdateView):
    model = Shares
    form_class = SharesForm
    template_name = 'admin_panel/shares/shares_update.html'

class AdminSharesDeleteView(DeleteView):
    model = Shares
    template_name = 'admin_panel/shares/shares_delete.html'
    success_url = reverse_lazy('admin_shares')
# Shares -----


class AdminPagesView(TemplateView):
    template_name = 'admin_panel/pages.html'

# User views
class AdminUsersView(ListView):
    model = Client
    template_name = 'admin_panel/users/users.html'
    ordering = ['-id']
    

class AdminUsersUpdateView(UpdateView):
    model = Client
    form_class = EditProfileForm
    template_name = 'admin_panel/users/user_update.html'

    def get_success_url(self):
        return reverse('admin_users')

class AdminUserDeleteView(DeleteView):
    model = Client
    template_name = 'admin_panel/users/user_delete.html'
    success_url = reverse_lazy('admin_users')

    def get_success_url(self):
        return reverse('admin_users')
# User -----

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
