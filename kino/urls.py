from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from kino.views import HomeView, sign_in_view, sign_up_view, logout_view
from kino.views import admin_view, AdminFilmsView, AdminFilmDetailView, AdminFilmAddView, AdminFilmUpdateView, AdminFilmDeleteView
from kino.views import AdminCinemasView, AdminCinemaDetailView, AdminCinemaAddView, AdminCinemaUpdateView, AdminCinemaDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # path('', home_view, name='home'),
    path('sign_in/', sign_in_view, name='sign_in'),
    path('sign_up/', sign_up_view, name='sign_up'),
    path('logout/', logout_view, name='logout'),

    #Admin
    path('admin/', admin_view, name='admin_home'),
    
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