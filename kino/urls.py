from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from kino.views import HomeView, sign_in_view, sign_up_view, logout_view
from kino.views import admin_view, AdminStatisticsView, AdminBannersSlidersView, AdminNewsView, AdminSharesView, AdminPagesView, AdminUsersView, AdminMailingView
#FILM
from kino.views import AdminFilmsView, AdminFilmDetailView, AdminFilmAddView, AdminFilmUpdateView, AdminFilmDeleteView
#CINEMA
from kino.views import AdminCinemasView, AdminCinemaDetailView, AdminCinemaAddView, AdminCinemaUpdateView, AdminCinemaDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # path('', home_view, name='home'),
    path('sign_in/', sign_in_view, name='sign_in'),
    path('sign_up/', sign_up_view, name='sign_up'),
    path('logout/', logout_view, name='logout'),

    #Admin
    path('admin/', admin_view, name='admin_home'),
    path('admin/statistics/', AdminStatisticsView.as_view(), name='admin_statistics'),
    path('admin/banners_sliders/', AdminBannersSlidersView.as_view(), name='admin_banners_sliders'),
    path('admin/news/', AdminNewsView.as_view(), name='admin_news'),
    path('admin/shares/', AdminSharesView.as_view(), name='admin_shares'),
    path('admin/pages/', AdminPagesView.as_view(), name='admin_pages'),
    path('admin/users/', AdminUsersView.as_view(), name='admin_users'),
    path('admin/mailing/', AdminMailingView.as_view(), name='admin_mailing'),
    
    
    #FILMS
    path('admin/films/', AdminFilmsView.as_view(), name='admin_films'),
    path('admin/films/<int:pk>', AdminFilmDetailView.as_view(), name='admin_film_detail'),
    path('admin/films/edit/<int:pk>', AdminFilmUpdateView.as_view(), name='admin_update_film'),
    path('admin/films/<int:pk>/delete', AdminFilmDeleteView.as_view(), name='admin_delete_film'),
    path('admin/new_film/', AdminFilmAddView.as_view(), name='admin_add_film'),
    
    #CINEMA
    path('admin/cinemas/', AdminCinemasView.as_view(), name='admin_cinemas'),
    path('admin/cinemas/<int:pk>', AdminCinemaDetailView.as_view(), name='admin_cinema_detail'),
    path('admin/cinemas/edit/<int:pk>', AdminCinemaUpdateView.as_view(), name='admin_update_cinema'),
    path('admin/cinemas/<int:pk>/delete', AdminCinemaDeleteView.as_view(), name='admin_delete_cinema'),
    path('admin/new_cinemas/', AdminCinemaAddView.as_view(), name='admin_add_cinema'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)