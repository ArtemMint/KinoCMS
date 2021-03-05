from django.urls import path
from register.views.user import *
from register.views.password import PasswordChangeView, PasswordSuccessView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('register/',
         user_register_view,
         name='register'
         ),
    path('login/',
         user_login_view,
         name='login'
         ),
    path('update/',
         user_update_view,
         name='edit_profile'
         ),
    path('password/',
         PasswordChangeView.as_view()
         ),
    path('password/success/',
         PasswordSuccessView.as_view(),
         name='password_success'
         ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
