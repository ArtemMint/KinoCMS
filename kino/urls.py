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
from kino.views.admin_panel.schedule import *
from kino.views.site.cinema import *
from kino.views.site.film import *
from kino.views.site.home import *
from kino.views.site.news import *
from kino.views.site.schedule import *
from kino.views.site.poster import *
from kino.views.site.shares import *
from kino.views.site.children_room import *
from kino.views.site.cafe_bar import *
from kino.views.site.vip_hall import *
from kino.views.site.advertising import *

urlpatterns = [
    # Site KinoCMS.
    path('', home_page_view, name='home'),
    path('schedule/', schedule_page_view, name='schedule'),
    path('poster/', poster_view, name='poster'),
    path('premiere/', premiere_view, name='premiere'),
    path('film/<int:film_id>', film_detail_view, name='film_detail'),
    path('cinemas/', ciname_view, name='cinemas'),
    path('cinema/<int:cinema_id>',
         cinema_detail_view, name='cinema_detail'),
    path('cinema/<int:cinema_id>/hall/<int:cinemahall_id>',
         cinemahall_detail_view, name='cinemahall_detail'),
    path('shares/', shares_view, name='shares'),
    path('shares/<int:shares_id>',
         shares_detail_view, name='shares_detail'),
    path('news/', news_view, name='news'),
    path('news/<int:news_id>', news_detail_view, name='news_detail'),
    path('children-room/', children_room_page_view, name='children_room'),
    path('cafe-bar/', cafe_bar_page_view, name='cafe_bar'),
    path('vip-hall/', vip_hall_page_view, name='vip_hall'),
    path('advertising/', advertising_page_view, name='advertising'),
    path('contacts/', children_room_page_view, name='contacts'),
    path('mobile-app/', children_room_page_view, name='mobile_app'),
    path('about/', children_room_page_view, name='about'),

    # Admin schedule.
    path('admin/schedule/', admin_schedule_view, name='admin_schedule'),
    path('admin/schedule/add/', admin_schedule_create_view,
         name='admin_create_schedule'),
    path('admin/schedule/<int:schedule_id>/update/',
         admin_schedule_update_view, name='admin_update_schedule'),
    path('admin/schedule/<int:pk>/delete/',
         AdminScheduleDeleteView.as_view(), name='admin_delete_schedule'),

    # Admin users.
    path('admin/users/', adminUserListView, name='admin_users'),
    path('admin/users/create/', adminUserCreateView, name='admin_create_users'),
    path('admin/users/edit/<int:user_id>',
         adminUserUpdateView, name='admin_update_users'),
    path('admin/users/<int:user_id>/delete',
         adminUserDeleteView, name='admin_delete_user'),
    path('admin/users/', adminUserListView, name='admin_users'),

    # Admin sidebar.
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
    path('admin/pages/', admin_pages_view,
         name='admin_pages'),
    path('admin/pages/home/', admin_home_page_view,
         name='admin_homepage'),
    path('admin/pages/contacts/', admin_contacts_page_view,
         name='admin_contacts_page'),
    path('admin/pages/about/', admin_about_page_view,
         name='admin_about_page'),
    path('admin/pages/cafe-bar/', admin_cafe_bar_page_view,
         name='admin_cafe-bar_page'),
    path('admin/pages/vip-hall/', admin_vip_hall_page_view,
         name='admin_vip-hall_page'),
    path('admin/pages/advertising/', admin_advertising_page_view,
         name='admin_advertsing_page'),
    path('admin/pages/children_room/', admin_children_room_page_view,
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
