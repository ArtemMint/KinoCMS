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

    # Admin USERS
    path('admin/users/', adminUserListView, name='admin_users'),
    path('admin/users/create/',
         adminUserCreateView, name='admin_create_users'),
    path('admin/users/edit/<int:user_id>',
         adminUserUpdateView, name='admin_update_users'),
    path('admin/users/<int:user_id>/delete',
         adminUserDeleteView, name='admin_delete_user'),
    path('admin/users/', adminUserListView, name='admin_users'),

    # Admin
    path('admin/', admin_view, name='admin_home'),
    path('admin/statistics/', adminStatisticsView,
         name='admin_statistics'),
    path('admin/banners/sliders', slider_banners_update,
         name='admin_banners_sliders'),
    path('admin/banners/back', back_banners_update,
         name='admin_banners_back'),
    path('admin/banners/shares', shares_banners_update,
         name='admin_banners_shares'),
    path('admin/shares/', AdminSharesView.as_view(),
         name='admin_shares'),
    path('admin/pages/', adminPagesView,
         name='admin_pages'),
    path('admin/pages/home/', adminHomePageView, name='admin_homepage'),
    path('admin/pages/contacts/', adminContactsPageView,
         name='admin_contacts_page'),
    path('admin/pages/about/', adminAboutPageView, name='admin_about_page'),
    path('admin/pages/cafe-bar/', adminCafeBarPageView,
         name='admin_cafe-bar_page'),
    path('admin/pages/vip-hall/', adminVipHallPageView,
         name='admin_vip-hall_page'),
    path('admin/pages/advertising/', adminAdvertisingPageView,
         name='admin_advertsing_page'),
    path('admin/pages/children_room/', adminChildrenRoomPageView,
         name='admin_children_room_page'),
    path('admin/mailing/', AdminMailingView.as_view(),
         name='admin_mailing'),
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
    path('admin/new_film/', AdminFilmAddView.as_view(),
         name='admin_add_film'),

    # CINEMA
    path('admin/cinemas/', AdminCinemasView.as_view(),
         name='admin_cinemas'),
    path('admin/cinemas/<int:cinema_id>/',
         adminCinemaDetailView, name='admin_cinema_detail'),
    path('admin/cinemas/edit/<int:pk>/',
         AdminCinemaUpdateView.as_view(), name='admin_update_cinema'),
    path('admin/cinemas/<int:pk>/delete/',
         AdminCinemaDeleteView.as_view(), name='admin_delete_cinema'),
    path('admin/new_cinemas/', AdminCinemaAddView.as_view(),
         name='admin_add_cinema'),
    path('admin/cinemas/<int:cinema_id>/cinemahall/<int:cinemahall_id>/',
         adminCinemahallDetailView, name='admin_cinemahall_detail'),
    path('admin/cinemas/<int:cinema_id>/cinemahall/<int:cinemahall_id>/update/',
         adminCinemahallUpdateView, name='admin_update_cinemahall'),
    path('admin/cinemas/<int:cinema_id>/cinemahall/<int:cinemahall_id>/delete/',
         adminCinemahallDeleteView, name='admin_delete_cinemahall'),
    path('admin/cinemas/<int:cinema_id>/new_cinemahall/',
         adminCinemahallCreateView, name='admin_add_cinemahall'),

    # News
    path('admin/news/', AdminNewsView.as_view(), name='admin_news'),
    path('admin/news/<int:pk>', AdminNewsDetailView.as_view(),
         name='admin_news_detail'),
    path('admin/news/edit/<int:pk>',
         AdminNewsUpdateView.as_view(), name='admin_update_news'),
    path('admin/news/<int:pk>/delete',
         AdminNewsDeleteView.as_view(), name='admin_delete_news'),
    path('admin/new_news/', AdminNewsAddView.as_view(),
         name='admin_add_news'),

    # Shares
    path('admin/shares/', AdminSharesView.as_view(),
         name='admin_shares'),
    path('admin/shares/<int:pk>', AdminSharesDetailView.as_view(),
         name='admin_shares_detail'),
    path('admin/shares/edit/<int:pk>',
         AdminSharesUpdateView.as_view(), name='admin_update_shares'),
    path('admin/shares/<int:pk>/delete',
         AdminSharesDeleteView.as_view(), name='admin_delete_shares'),
    path('admin/new_shares/', AdminSharesAddView.as_view(),
         name='admin_add_shares'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
