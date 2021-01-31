from django.urls import path
from django.contrib.auth import views as auth_views

from register.views import UserRegisterView, UserEditView, PasswordChangeView, PasswordSuccessView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordChangeView.as_view()),
    path('password_success/', PasswordSuccessView.as_view(), name='password_success'),
]