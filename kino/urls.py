from django.urls import path
from django.conf import settings

from django.conf.urls.static import static

from kino.views.admin_panel.banners import *
from kino.views.admin_panel.cinema import *
from kino.views.admin_panel.film import *
from kino.views.admin_panel.home import *
from kino.views.admin_panel.mailing import *
from kino.views.admin_panel.news import *
from kino.views.admin_panel.pages import *
from kino.views.admin_panel.shares import *
from kino.views.admin_panel.statistics import *
from kino.views.admin_panel.user import *
from kino.views.site.cinema import *
from kino.views.site.film import *
from kino.views.site.home import *
from kino.views.site.news import *
from kino.views.site.poster import *
from kino.views.site.shares import *


urlpatterns = [
    # Site KinoCMS.
    path('', homePageView, name='home'),
    path('poster/', posterView, name='poster'),
    path('premiere/', premiereView, name='premiere'),
    path('film/<int:pk>', FilmDetailView.as_view(), name='film_detail'),
    path('cinemas/', cinameView, name='cinemas'),
    path('cinema/<int:cinema_id>', cinemaDetailView, name='cinema_detail'),
    path('cinema/<int:cinema_id>/hall/<int:cinemahall_id>',
         cinemahallDetailView, name='cinemahall_detail'),
    path('shares/', sharesView, name='shares'),
    path('shares/<int:shares_id>', sharesDetailView, name='shares_detail'),
    path('news/', newsView, name='news'),
    path('news/<int:news_id>', newsDetailView, name='news_detail'),

    # Admin users.
    path('admin/users/', adminUserListView, name='admin_users'),
    path('admin/users/create/',
         adminUserCreateView, name='admin_create_users'),
    path('admin/users/edit/<int:user_id>',
         adminUserUpdateView, name='admin_update_users'),
    path('admin/users/<int:user_id>/delete',
         adminUserDeleteView, name='admin_delete_user'),
    path('admin/users/', adminUserListView, name='admin_users'),

    # Admin sidebar,
    path('admin/', admin_view, name='admin_home'),
    path('admin/statistics/', adminStatisticsView,
         name='admin_statistics'),
    path('admin/banners/sliders/', slider_banners_update,
         name='admin_banners_sliders'),
    path('admin/banners/background/', back_banners_update,
         name='admin_banners_back'),
    path('admin/banners/shares/', shares_banners_update,
         name='admin_banners_shares'),
    path('admin/shares/', AdminSharesView.as_view(),
         name='admin_shares'),
    path('admin/pages/', adminPagesView,
         name='admin_pages'),
    path('admin/pages/home/', adminHomePageView,
         name='admin_homepage'),
    path('admin/pages/contacts/', adminContactsPageView,
         name='admin_contacts_page'),
    path('admin/pages/about/', adminAboutPageView,
         name='admin_about_page'),
    path('admin/pages/cafe-bar/', adminCafeBarPageView,
         name='admin_cafe-bar_page'),
    path('admin/pages/vip-hall/', adminVipHallPageView,
         name='admin_vip-hall_page'),
    path('admin/pages/advertising/', adminAdvertisingPageView,
         name='admin_advertsing_page'),
    path('admin/pages/children_room/', adminChildrenRoomPageView,
         name='admin_children_room_page'),

    # Mailing of users.
    path('admin/mailing/all/', mailing_all_users,
         name='mailing_all_users'),
    path('admin/mailing/group/', mailing_group_of_users,
         name='mailing_group_of_users'),

    # Admin films.
    path('admin/films/', AdminFilmsView.as_view(),
         name='admin_films'),
    path('admin/films/create/', admin_film_create_view,
         name='admin_create_film'),
    path('admin/films/<int:film_id>',
         admin_film_detail_view, name='admin_film_detail'),
    path('admin/films/<int:film_id>/update/',
         admin_film_update_view, name='admin_update_film'),
    path('admin/films/<int:pk>/delete',
         AdminFilmDeleteView.as_view(), name='admin_delete_film'),

    # Admin cinemas.
    path('admin/cinemas/', AdminCinemasView.as_view(),
         name='admin_cinemas'),
    path('admin/cinemas/create/', admin_cinema_create_view,
         name='admin_create_cinema'),
    path('admin/cinemas/<int:cinema_id>/',
         admin_cinema_detail_view, name='admin_cinema_detail'),
    path('admin/cinemas/<int:cinema_id>/update/',
         admin_cinema_update_view, name='admin_update_cinema'),
    path('admin/cinemas/<int:pk>/delete/',
         AdminCinemaDeleteView.as_view(), name='admin_delete_cinema'),

    # Admin cinema hall.
    path('admin/cinemas/<int:cinema_id>/cinemahall/create/',
         admin_cinemahall_create_view, name='admin_add_cinemahall'),
    path('admin/cinemas/<int:cinema_id>/cinemahall/<int:cinemahall_id>/',
         admin_cinemahall_detail_view, name='admin_cinemahall_detail'),
    path(
        'admin/cinemas/<int:cinema_id>/cinemahall/<int:cinemahall_id>/update/',
        admin_cinemahall_update_view, name='admin_update_cinemahall'),
    path(
        'admin/cinemas/<int:cinema_id>/cinemahall/<int:cinemahall_id>/delete/',
        admin_cinemahall_delete_view, name='admin_delete_cinemahall'),

    # Admin news.
    path('admin/news/', AdminNewsView.as_view(), name='admin_news'),
    path('admin/news/create/', admin_news_create_view,
         name='admin_create_news'),
    path('admin/news/<int:news_id>', admin_news_detail_view,
         name='admin_news_detail'),
    path('admin/news/<int:news_id>/update/',
         admin_news_update_view, name='admin_update_news'),
    path('admin/news/<int:pk>/delete',
         AdminNewsDeleteView.as_view(), name='admin_delete_news'),

    # Admin shares.
    path('admin/shares/', AdminSharesView.as_view(),
         name='admin_shares'),
    path('admin/shares/create/', admin_shares_create_view,
         name='admin_create_shares'),
    path('admin/shares/<int:shares_id>', admin_shares_detail_view,
         name='admin_shares_detail'),
    path('admin/shares/<int:shares_id>/update/',
         admin_shares_update_view, name='admin_update_shares'),
    path('admin/shares/<int:pk>/delete',
         AdminSharesDeleteView.as_view(), name='admin_delete_shares'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
