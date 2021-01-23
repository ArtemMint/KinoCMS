from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from kino.views import HomeView, sign_in_view, sign_up_view, logout_view, admin_view, AdminFilmsView, AdminCinemasView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # path('', home_view, name='home'),
    path('sign_in/', sign_in_view, name='sign_in'),
    path('sign_up/', sign_up_view, name='sign_up'),
    path('logout/', logout_view, name='logout'),
    path('admin/', admin_view, name='admin_home'),
    path('admin/films/', AdminFilmsView.as_view(), name='admin_films'),
    path('admin/cinemas/', AdminCinemasView.as_view(), name='admin_cinemas'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)