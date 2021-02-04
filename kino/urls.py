from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views.admin_panel.banners import AdminBannersSlidersView
from .views.admin_panel.cinema import *
from .views.admin_panel.film import *
from .views.admin_panel.home import admin_view
from .views.admin_panel.mailing import AdminMailingView
from .views.admin_panel.news import *
from .views.admin_panel.pages import AdminPagesView
from .views.admin_panel.shares import *
from .views.admin_panel.statistics import AdminStatisticsView
from .views.admin_panel.user import *
from .views.site.cinema import *
from .views.site.film import *
from .views.site.home import HomeView
from .views.site.news import NewsView
from .views.site.poster import PosterView
from .views.site.shares import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('poster/', PosterView.as_view(), name='poster'),
    path('premiere/', FilmPremiereView.as_view(), name='premiere'),
    path('film/<int:pk>', FilmDetailView.as_view(),
         name='film_detail'),
    path('cinemas/', CinemasView.as_view(), name='cinemas'),
    path('cinema/<int:pk>', CinemaDetailView.as_view(),
         name='cinema_detail'),
    path('shares/', SharesView.as_view(), name='shares'),
    path('news/', NewsView.as_view(), name='news'),

    path('admin/users/', AdminUsersView.as_view(),
         name='admin_users'),
    path('admin/users/edit/<int:pk>',
         AdminUsersUpdateView.as_view(), name='admin_update_users'),
    path('admin/users/<int:pk>/delete',
         AdminUserDeleteView.as_view(), name='admin_delete_user'),
    path('admin/users/<int:pk>/delete',
         AdminUserDeleteView.as_view(), name='admin_delete_user'),

    # Admin
    path('admin/', admin_view, name='admin_home'),
    path('admin/statistics/', AdminStatisticsView.as_view(),
         name='admin_statistics'),
    path('admin/banners_sliders/', AdminBannersSlidersView.as_view(),
         name='admin_banners_sliders'),
    path('admin/banners_sliders/', AdminBannersSlidersView.as_view(),
         name='admin_banners_sliders'),
    path('admin/shares/', AdminSharesView.as_view(),
         name='admin_shares'),
    path('admin/pages/', AdminPagesView.as_view(),
         name='admin_pages'),
    path('admin/users/', AdminUsersView.as_view(),
         name='admin_users'),
    path('admin/mailing/', AdminMailingView.as_view(),
         name='admin_mailing'),


    # FILMS
    path('admin/films/', AdminFilmsView.as_view(),
         name='admin_films'),
    path('admin/films/<int:pk>',
         AdminFilmDetailView.as_view(), name='admin_film_detail'),
    path('admin/films/edit/<int:pk>',
         AdminFilmUpdateView.as_view(), name='admin_update_film'),
    path('admin/films/<int:pk>/delete',
         AdminFilmDeleteView.as_view(), name='admin_delete_film'),
    path('admin/films/<int:pk>/delete',
         AdminFilmDeleteView.as_view(), name='admin_delete_film'),
    path('admin/new_film/', AdminFilmAddView.as_view(),
         name='admin_add_film'),

    # CINEMA
    path('admin/cinemas/', AdminCinemasView.as_view(),
         name='admin_cinemas'),
    path('admin/cinemas/<int:pk>',
         AdminCinemaDetailView.as_view(), name='admin_cinema_detail'),
    path('admin/cinemas/edit/<int:pk>',
         AdminCinemaUpdateView.as_view(), name='admin_update_cinema'),
    path('admin/cinemas/<int:pk>/delete',
         AdminCinemaDeleteView.as_view(), name='admin_delete_cinema'),
    path('admin/new_cinemas/', AdminCinemaAddView.as_view(),
         name='admin_add_cinema'),
    path('admin/cinemas/<int:pk>/delete',
         AdminCinemaDeleteView.as_view(), name='admin_delete_cinema'),
    path('admin/new_cinemas/', AdminCinemaAddView.as_view(),
         name='admin_add_cinema'),

    # News
    path('admin/news/', AdminNewsView.as_view(), name='admin_news'),
    path('admin/news/<int:pk>', AdminNewsDetailView.as_view(),
         name='admin_news_detail'),
    path('admin/news/edit/<int:pk>',
         AdminNewsUpdateView.as_view(), name='admin_update_news'),
    path('admin/news/<int:pk>/delete',
         AdminNewsDeleteView.as_view(), name='admin_delete_news'),
    path('admin/news/<int:pk>/delete',
         AdminNewsDeleteView.as_view(), name='admin_delete_news'),
    path('admin/new_news/', AdminNewsAddView.as_view(), name='admin_add_news'),

    # Shares
    path('admin/shares/', AdminSharesView.as_view(),
         name='admin_shares'),
    path('admin/shares/<int:pk>', AdminSharesDetailView.as_view(),
         name='admin_shares_detail'),
    path('admin/shares/edit/<int:pk>',
         AdminSharesUpdateView.as_view(), name='admin_update_shares'),
    path('admin/shares/<int:pk>/delete',
         AdminSharesDeleteView.as_view(), name='admin_delete_shares'),
    path('admin/shares/<int:pk>', AdminSharesDetailView.as_view(),
         name='admin_shares_detail'),
    path('admin/shares/edit/<int:pk>',
         AdminSharesUpdateView.as_view(), name='admin_update_shares'),
    path('admin/shares/<int:pk>/delete',
         AdminSharesDeleteView.as_view(), name='admin_delete_shares'),
    path('admin/new_shares/', AdminSharesAddView.as_view(), name='admin_add_shares'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
